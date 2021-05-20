import flask_user
from app import app


class MyUserDB:
    """
    this is the base of the users data base.
    It's plays main role in the login and other stuff.
    """
    def __init__(self):
        self.dbAdapter = flask_user.DbAdapter()  # todo create instance of this object
