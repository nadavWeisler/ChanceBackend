from database.db import db
from database.user import User
from flask_bcrypt import generate_password_hash, check_password_hash
from assets import errors
import datetime


class Student(User):
    def __init__(self):
        User.__init__(self)
        self.rank = db.NumberField(default=0)
        self.internCandidate = db.ListField(db.NumberField(), default=list)
        self.internComplete = db.ListField(db.NumberField(), default=list)

    def setRank(self, reward):
        self.rank += reward

    def setCandidate(self, internId, remove=False):
        if not remove:
            intern = None  # todo get intern by id
            now = datetime.datetime.now()
            if intern.lastApplyDate < now:
                raise errors.TimeForApplicationPassed
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
