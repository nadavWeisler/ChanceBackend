from flask import request
from flask_restful import Resource
from database.internship import Internship


class ApproveCandidate(Resource):
    candidate_id = request.form['candidate_id']
    internship_id = request.form['internship_id']
    Internship.objects.get(internship_id).approveOffer(candidate_id)


class OfferCandidate(Resource):
    candidate_id = request.form['candidate_id']
    internship_id = request.form['internship_id']
    Internship.objects.get(internship_id).getOffer(candidate_id)


class FinishInternship(Resource):
    internship_id = request.form['internship_id']
    Internship.objects.get(internship_id).finishProject()
