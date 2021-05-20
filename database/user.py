from db import db
from flask_bcrypt import generate_password_hash, check_password_hash
from assets import errors


class User(db.Document):
    def __init__(self):
        self.email = db.EmailField(required=True, unique=True)
        self.password = db.StringField(required=True, min_length=6)
        self.rank = db.NumberField(default=0)
        self.internCandidate = db.ListField(db.NumberField(), default=list)
        self.internComplete = db.ListField(db.NumberField(), default=list)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def setRank(self, reward):
        self.rank += reward
        return True

    def setCandidate(self, internId, remove=False):
        if not remove:
            self.internCandidate.append(internId)
        else:
            if internId not in self.internCandidate:
                raise errors.NoSuchInternship
            self.internCandidate.remove(internId)

    def setComplete(self, internId, remove=False):
        if not remove:
            self.internComplete.append(internId)
        else:
            if internId not in self.internCandidate:
                raise errors.NoSuchInternship
            self.internComplete.remove(internId)
