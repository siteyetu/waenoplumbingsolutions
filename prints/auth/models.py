from application import db




#Chief and staff
class StaffProfiles(db.Document):

    first_name = db.StringField(db_field="first_name", required=True, max_length=50)
    last_name = db.StringField(db_field="last_name", required=True, max_length=50)
    username = db.StringField(db_field="username")
    email = db.StringField(db_field="email")
    tel = db.StringField(db_field="tel")
    

    specialty = db.StringField(db_field="specialty")
    specialty_description = db.StringField(db_field="specialty_description")

    moduleaccesslist =db.StringField(db_field="moduleaccesslist")

    passwordhash = db.StringField(db_field="passwordhash")
    live = db.BooleanField(db_field="live", default=True)
    timeOfRegistration= db.StringField(db_field="timeOfRegistration")

    verification_status = db.BooleanField(db_field="verification_status")
    acceptance_status = db.BooleanField(db_field="acceptance_status")






#Login, request authentication and authorization
class Tokens(db.Document):
    username= db.StringField(db_field="username")
    token= db.StringField(db_field="token")
    pubkey =db.StringField(db_field="pubkey")
    timeofexpiry = db.IntField(db_field="timeofexpiry")
    status = db.BooleanField(db_field="status")
    timeOfRegistration= db.IntField(db_field="timeOfRegistration")



class DailyKeyPairs(db.Document):
    pubkey = db.StringField(db_field="pubkey")
    privkey = db.StringField(db_field="privkey")
    timeOfRegistration= db.IntField(db_field="timeOfRegistration")

class RecoverPassword(db.Document):
    email = db.StringField(db_field="email")
    recoverparams = db.StringField(db_field="recoverparams")
    timeOfRegistration = db.StringField(db_field="timeOfRegistration")
    recoverparamsstatus = db.BooleanField(db_field="recoverparamsstatus", default=False)

