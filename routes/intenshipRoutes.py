from flask import request
from flask_restful import Resource
from mongoengine import NotUniqueError, FieldDoesNotExist

from assets.errors import SchemaValidationError, EmailAlreadyExistsError, InternalServerError
from database.internship import Internship


class GetExperimentApi(Resource):
    def get(self):
        try:
            companyId = request.form["companyId"]
            internships = Internship.objects.get(companyId=companyId, tags=[])
            return {internships}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError

class CreateExperimentApi(Resource):
    def post(self):
        companyId = request.form["companyId"]
        internship = Internship(companyId=companyId)
        internship.save()