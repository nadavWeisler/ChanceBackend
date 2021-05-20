import datetime

from flask import request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist

from assets.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, \
    InternalServerError
from database.student import Student
from database.company import Company


class PersonalSpace(Resource):
    def get(self, email):
        try:
            user = Student.objects(email=email)
            if not user:
                user = Company.objects(email=email)

            return jsonify(user), 200
        except Exception as e:
            print(e)
            raise e
