from db import db


class Internship(db.Document):
    def __init__(self):
        self._companyId = db.NumbrField(required=True)
        self._name = db.StringField(required=True, min_length=6)
        self._duration = db.IntField(required=True)
        self._lastApplyDate = db.StringField(required=True)
        self._tags = db.ListField()