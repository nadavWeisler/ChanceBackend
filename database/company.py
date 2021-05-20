from database.db import db
from database.user import User
from database.internship import Internship


class Company(User):
    linkedIn = db.StringField()
    github = db.StringField()
    internships = db.ListField(db.StringField(), default=list)
    companyName = db.StringField(unique=True)

    def closeInternship(self, internshipId):
        Internship.objects.get(id=internshipId).finishProject()

    def openInternship(self,
                       name,
                       duration,
                       lastApplyDate,
                       dueDate,
                       difficulty,
                       field,
                       tags,
                       description=""):
        internship = Internship(companyName=self.companyName,
                                name=name,
                                duration=duration,
                                lastApplyDate=lastApplyDate,
                                dueDate=dueDate,
                                difficulty=difficulty,
                                description=description,
                                field=field,
                                tags=tags)
        internship.save()
        internship_id = str(internship.id)
        print(type(internship_id))
        self.internships.append(internship_id)
        self.save()
        return internship_id

