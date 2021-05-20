from .db import db
from assets import errors
import datetime as date


class Internship(db.Document):
    def __init__(self,
                 companyId,
                 name,
                 duration,
                 lastApplyDate,
                 dueDate,
                 field,
                 tags,
                 reward):
        # todo change API to FireBase
        self.id = db.NumbrField()  # todo will use id creator?

        # the job details
        self.companyId = db.NumbrField(required=True)
        self.name = db.StringField(required=True, min_length=6)
        self.reward = db.StringField(default=reward)
        self.duration = db.IntField(required=True)
        self.lastApplyDate = db.DateTime(required=True)
        self.dueDate = db.DateTime(required=True)

        # further information
        self.field = db.StringField(default=field)
        self.tags = db.ListField(db.StringField(), default=tags)

        # things we will decide later
        self.workerId = db.NumbrField()
        self.candidates = db.ListField(db.NumbrField(), default=list)
        self.taken = db.BooleanField(default=True)
        self.relevant = db.BooleanField(default=True)

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
