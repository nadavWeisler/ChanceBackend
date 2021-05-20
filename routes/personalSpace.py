import datetime
from dateutil import parser
from flask import request, jsonify, make_response
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist

from assets.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, \
    InternalServerError
from database.internship import Internship
from database.student import Student
from database.company import Company


class CompanyPersonalSpace(Resource):
    def get(self):
        try:
            if 'company_name' not in request.form and 'email' not in request.form:
                return {}, 502
            if 'company_name' in request.form:
                company_name = request.form['company_name']
                user = Company.objects.get(companyName=company_name)
            else:
                email = request.form['email']
                user = Company.objects.get(email=email)
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
            company_name = request.form['company_name']
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
            company = Company.objects.get(companyName=company_name)
            intern_id = company.openInternship(project_name, duration, last_application_date, due_date, difficulty,
                                               field, tags, description)
            return {'name': company.name, 'internship': intern_id}, 200


        except Exception as e:
            print(e)
            raise e


class StudentPersonalSpace(Resource):
    def get(self):
        try:
            email = request.form['email']
            user = Student.objects.get(email=email)
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

    def post(self, status):
        try:
            email = request.form['email']
            data = request.form['data']
            user = Student.objects.get(email=email)
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
