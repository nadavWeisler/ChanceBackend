import datetime
from dateutil import parser
from flask import request, jsonify, make_response
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist

from assets.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, \
    InternalServerError
from database.student import Student
from database.company import Company


class CompanyPersonalSpace(Resource):
    def get(self, email):
        try:
            user = Company.objects(email=email)
            return jsonify(user), 200
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
            company.save()
            return {'name': company.name, 'internship': intern_id}, 200


        except Exception as e:
            print(e)
            raise e
