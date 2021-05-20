from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from mongoengine import NotUniqueError, FieldDoesNotExist

from assets.errors import SchemaValidationError, EmailAlreadyExistsError, InternalServerError
from database.internship import Internship


class GetInternshipsApi(Resource):
    @jwt_required()
    def get(self):
        try:
            company_id = request.form["companyId"]
            internships = Internship.objects.get(companyId=company_id, tags=[])
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
