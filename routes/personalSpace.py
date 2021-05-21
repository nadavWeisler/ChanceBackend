import datetime
from dateutil import parser
from flask import request, jsonify, make_response
from flask_cors import cross_origin
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist

from assets.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, \
    InternalServerError
from database.internship import Internship
from database.student import Student
from database.company import Company
from database.user import User


class GetType(Resource):
    def get(self):
        user = User.objects.get(id=request.form['user_id'])
        return {'user_type': user.user_type}, 200


class CompanyPersonalSpace(Resource):
    def get(self):
        try:
            user_id = request.form['user_id']
            user = Company.objects.get(id=user_id)
            return {'user_name': user.name,
                    'email': user.email,
                    'linkedIn': user.linkedIn,
                    'github': user.github,
                    'internships': user.internships,
                    'company_name': user.companyName
                    }, 200
        except Exception as e:
            print(e)
            raise e

    def post(self):
        try:
            user_id = request.form['user_id']
            project_name = request.form['project_name']
            duration = request.form['duration']
            due_date = parser.parse(request.form['due_date'])
            last_application_date = parser.parse(request.form['last_application_date'])
            difficulty = request.form['difficulty']
            field = request.form['field']
            tags = request.form['tags'].replace(" ", "").split("#")

            description = None
            if 'description' in request.form:
                description = request.form['description']
            company = Company.objects.get(id=user_id)
            intern_id = company.openInternship(project_name, duration, last_application_date, due_date, difficulty,
                                               field, tags, description)
            return {'name': company.name, 'internship': intern_id}, 200


        except Exception as e:
            print(e)
            raise e


class StudentPersonalSpaceGet(Resource):
    def post(self):
        try:
            user_id = request.form['user_id']
            user = Student.objects.get(id=user_id)
            return {'user_name': user.name,
                    'email': user.email,
                    'rank': user.rank,
                    'intern_candidate': user.internCandidate,
                    'intern_complete': user.internComplete,
                    'intern_current': user.internCurrent
                    }, 200
        except Exception as e:
            print(e)
            raise e


class StudentPersonalSpacePost(Resource):
    def post(self, status):
        try:
            user_id = request.form['user_id']
            data = request.form['data']
            user = Student.objects.get(email=user_id)
            if status == 'candidate':
                user.setCandidate(data)
            elif status == 'current':
                user.setCurrent(data)
            elif status == 'complete':
                user.setComplete(data)
            elif status == 'rank':
                user.setRank(data)
            else:
                return {'message': 'invalid status'}, 400
            return {'user_id': user.id}, 200
        except Exception as e:
            print(e)
            raise e
