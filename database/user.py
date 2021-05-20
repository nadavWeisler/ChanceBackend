from database.db import db
from flask_bcrypt import generate_password_hash, check_password_hash

TYPES = ('STUDENT', 'COMPANY')


class User(db.Document):
    name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    user_type = db.StringField(required=True, choices=TYPES)
    meta = {'allow_inheritance': True}

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
