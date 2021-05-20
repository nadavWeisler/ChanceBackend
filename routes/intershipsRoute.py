from flask_restful import Resource
from database.internship import Internship
from flask_mongoengine import MongoEngine
from datetime import datetime


class SearchEngine(Resource):
    def showAll(self):
        return Internship.objects()

    def filterByCompany(self, companyId):
        return Internship.objects(companyId=companyId)

    def filterByRelevance(self):
        return Internship.objects(relevant=True, lastApplicationDate__gte=datetime.today())

    def filterByAvailable(self):
        return Internship.objects(worker=-1, lastApplicationDate__gte=datetime.today())

    def filterByReward(self, desiredReward):
        return Internship.objects(reward__gte=desiredReward)

    def filterByDuration(self, maxTime):
        return Internship.objects(duration__lte=maxTime)

    def filterByField(self, desiredField):
        return Internship.objects(field=desiredField)

    def filterByTags(self, tags):
        result = []
        for tag in tags:
            result.append(Internship.objects(tag_exists=tag))
        return result

    def filterBeforeDueDate(self, date):
        return Internship.objects(dueDate__lte=date)

    def filterAfterDueDate(self, date):
        return Internship.objects(dueDate__gte=date)

    def filterByText(self, text):
        result = []
        result.append(Internship.objects(name_contains=text))
        result.append(Internship.objects(description_contains=text))
        return result
