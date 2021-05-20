from database.db import db
from database.user import User


class Company(User):
    super()
    linkedIn = db.StringField()
    github = db.StringField()
    internships = db.ListField()