from flask_restful import Resource
from database.internship import Internship
from datetime import datetime
from flask import request


class SearchEngine(Resource):
    def get(self):
        results = Internship.objects(relevant=True, worker_not=-1, lastApplicationDate__gte=datetime.today())
        if 'company' in request.form:
            intersection(filterByCompany(request.form["company"]), results)

        if "topic" in request.form:
            intersection(filterByField(), results)

            desiredField = request.form["topic"]

        if "duration" in request.form:
            maxTime = request.form["duration"]

        if "levels" in request.form:
            level = request.form["levels"]

        if "tags" in request.form:
            tags = request.form["company"]
        if "text" in request.form:
            text = request.form["company"]


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def filterByCompany(companyName):
    return Internship.objects(companyName=companyName)


def filterByDuration(maxTime):
    return Internship.objects(duration__lte=maxTime)


def filterByField(desiredField):
    return Internship.objects(field=desiredField)


def filterByTags(tags):
    result = []
    for tag in tags:
        result.append(Internship.objects(tag_exists=tag))
    return result


def filterByDifficultyRange(levels):
    result = []
    for level in levels:
        result += Internship.objects(diffcult__lte=level)
    return result


def filterBeforeDueDate(date=False):
    if not date:
        return Internship.objects()
    return Internship.objects(dueDate__lte=date)


def filterAfterDueDate(date=False):
    if not date:
        return Internship.objects()
    return Internship.objects(dueDate__gte=date)


def filterByText(text=False):
    if not text:
        return Internship.objects()
    result = []
    result += Internship.objects(name_contains=text)
    result += Internship.objects(description_contains=text)
    return result
