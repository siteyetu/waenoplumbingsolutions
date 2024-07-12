from application import db



class ContactUsTable(db.Document):
    name = db.StringField(db_field="first_name", required=True)
    email = db.StringField(db_field="email")
    phone = db.StringField(db_field="phone")
    message = db.StringField(db_field="message")
    timeOfRegistration = db.StringField(db_field="timeOfRegistration")
    replystatus = db.BooleanField(db_field="replystatus", default=False)
    