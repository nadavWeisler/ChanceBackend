import datetime

from flask import request
from flask_cors import cross_origin
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist

from assets.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, \
    InternalServerError
from database.student import Student
from database.company import Company
from database.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity


class SignupApi(Resource):
    def post(self):
        try:
            name = request.form["name"]
            email = request.form["email"]
            password = request.form["password"]
            user_type = request.form['user_type']
            if user_type == 'STUDENT':
                user = Student(name=name, email=email, password=password,
                               user_type=user_type)
            else:
                company_name = request.form['company_name']
                user = Company(name=name, companyName=company_name, email=email, password=password,
                               user_type=user_type)
            user.hash_password()
            user.save()
            print(user.id)
            return {'id': str(user.id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            print(e)
            raise InternalServerError


class LoginApi(Resource):
    def post(self):
        try:
            user = User.objects.get(email=request.form.get('email'))
            authorized = user.check_password(request.form.get('password'))
            if not authorized:
                raise UnauthorizedError

            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)
            refresh_token = create_refresh_token(identity=str(user.id))
            return {'access_token': access_token, 'refresh_token': refresh_token,
                    'user_id': str(user.id)}, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception:
            raise InternalServerError
