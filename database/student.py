from database.user import User
from database.db import db


class Student(User):
    rank = db.NumberField(default=0)
    internCandidate = db.ListField(db.NumberField(), default=list)
    internComplete = db.ListField(db.NumberField(), default=list)

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