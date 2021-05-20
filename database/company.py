from database.db import db
from database.user import User


class Company(User):
    linkedIn = db.StringField()
    github = db.StringField()
    internships = db.ListField()

