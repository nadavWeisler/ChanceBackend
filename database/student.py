import datetime
from database.user import User
from database.db import db
from assets import errors
import datetime
from database.internship import Internship


class Student(User):
    rank = db.IntField(default=0)
    internCandidate = db.ListField(db.ObjectIdField(), default=list)
    internComplete = db.ListField(db.ObjectIdField(), default=list)
    internCurrent = db.ListField(db.ObjectIdField(), default=list)

    def setRank(self, reward):
        self.rank += reward

    def setCandidate(self, internId, remove=False):
        if not remove:
            intern = Internship.objects.get(id=internId)  # todo get intern by id
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

    def setCurrent(self, internId, remove=False):
        if not remove:
            self.internCurrent.append(internId)
        else:
            if internId not in self.internCandidate:
                raise errors.NoSuchInternship
            self.internCurrent.remove(internId)
