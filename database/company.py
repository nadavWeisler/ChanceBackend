from database.db import db
from database.user import User


class Company(User):
    def __init__(self):
        super()
        self.linkedIn = db.StringField()
        self.github = db.StringField()
        self.internships = db.ListField()