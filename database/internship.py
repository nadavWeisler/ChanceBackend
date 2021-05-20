from .db import db
from assets import errors


class Internship(db.Document):
    # the job details
    companyId = db.NumbrField(required=True)
    name = db.StringField(required=True, min_length=6)
    reward = db.StringField(required=True)
    duration = db.IntField(required=True)
    lastApplyDate = db.DateTime(required=True)
    dueDate = db.DateTime(required=True)

    # further information
    field = db.StringField(required=True)
    tags = db.ListField(db.StringField())

    # things we will decide later
    workerId = db.NumbrField()
    candidates = db.ListField(db.NumbrField(), default=list)
    taken = db.BooleanField(default=True)
    relevant = db.BooleanField(default=True)

    def getOffer(self, userId):
        self.candidates.append(userId)

    def approveOffer(self, userId):
        self.taken = True
        if userId not in self.candidates:
            raise errors.NoSuchCandidate
        else:
            self.worker = userId
            for candidate in self.candidates:
                if candidate != userId:
                    self.rejectCandidate(candidate)
            self.candidates.clear()

    def rejectCandidate(self, candidateId):
        candidate = None  # todo get candidate
        candidate.setCandidate(self.id, True)

    def finishProject(self):
        worker = None  # todo get worker
        worker.setComplete(self.id, True)
        worker.setRank(self.reward)
        self.relevant = False
