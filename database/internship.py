from .db import db
from assets import errors
from database.user import User


class Internship(db.Document):
    # the job details
    companyId = db.NumbrField(required=True)
    name = db.StringField(required=True, min_length=6)
    reward = db.StringField()
    duration = db.IntField(required=True)
    lastApplyDate = db.StringField(required=True)
    dueDate = db.StringField(required=True)
    description = db.StringField()

    # further information
    field = db.StringField()
    tags = db.ListField(db.StringField())

    # things we will decide later
    workerId = db.NumbrField(default=-1)
    candidates = db.ListField(db.NumbrField(), default=list)

    relevant = db.BooleanField(default=True)

    def getOffer(self, userId):
        self.candidates.append(userId)

    def approveOffer(self, userId):
        if userId not in self.candidates:
            raise errors.NoSuchCandidate
        else:
            self.workerId = userId
            for candidate in self.candidates:
                if candidate != userId:
                    self.rejectCandidate(candidate)
            self.candidates.clear()

    def rejectCandidate(self, candidateId):
        candidate = User.objects.get(id=candidateId)
        candidate.setCandidate(self.id, True)

    def finishProject(self):
        worker = User.objects.get(id=self.workerId)
        worker.setComplete(self.id, True)
        worker.setRank(self.reward)
        self.relevant = False
