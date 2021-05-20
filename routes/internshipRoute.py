from flask import request
from flask_restful import Resource
from database.internship import Internship


class ApproveCandidate(Resource):
    def get(self):
        candidate_id = request.form['candidate_id']
        internship_id = request.form['internship_id']
        internship = Internship.objects.get(internship_id).approveOffer(candidate_id)
        return {'internship_id': internship.id}, 200


class OfferCandidate(Resource):
    def get(self):
        candidate_id = request.form['candidate_id']
        internship_id = request.form['internship_id']
        Internship.objects.get(internship_id).getOffer(candidate_id)
        return {'internship_id': internship_id}, 200

class FinishInternship(Resource):
    def get(self):
        internship_id = request.form['internship_id']
        Internship.objects.get(internship_id).finishProject()
        return {'internship_id': internship_id}, 200

