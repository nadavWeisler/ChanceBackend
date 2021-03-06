from .db import db
from assets import errors
from database.user import User


class Internship(db.Document):
    # the job details
    companyName = db.StringField(required=True)
    name = db.StringField(required=True, min_length=6)
    duration = db.IntField(required=True)
    lastApplyDate = db.DateTimeField(required=True)
    dueDate = db.DateTimeField(required=True)
    difficulty = db.IntField(required=True, min_value=1, max_value=3)
    description = db.StringField()

    # further information
    field = db.StringField()
    tags = db.ListField(db.StringField())

    # things we will decide later
    workerId = db.ObjectIdField(default=None)
    candidates = db.ListField(db.ObjectIdField(), default=list)

    relevant = db.BooleanField(default=True)

    def getOffer(self, userId):
        self.candidates.append(userId)
        User.objects.get(id=userId).setCandidate(self.id)

    def approveOffer(self, userId):
        if userId not in self.candidates:
            raise errors.NoSuchCandidate
        else:
            self.workerId = userId
            User.objects.get(id=userId).setCurrent(self.id)
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
        worker.setCurrent(self.id, False)
        worker.setRank(self.difficulty)
        self.relevant = False
