# bluprint for apps to get registered and AccessTokens user tokens
from flask_mongoengine.wtf import model_form
from flask.views import MethodView
from flask import request, abort, jsonify, render_template, redirect, url_for, session,send_from_directory, make_response


import uuid, json, importlib
from datetime import datetime, timedelta
#import numpy as np  
#import matplotlib.pyplot as plt  
from time import time as now
from random import randint as r

from prints.auth.models import StaffProfiles, Tokens, DailyKeyPairs, RecoverPassword
from prints.auth.decorators import auth_required, username_fetch, ip_check, categoryfind, gentoken

from mainModules.mailer.mailer import mymailer
from mainModules.crypto.myHasher import hash_text
from mainModules.cronJobs.crontasks import tokenexpiry, create_daily_pair
# from mainModules.mailer.mailer import mailer
import time

#tokenexpiry()
#create_daily_pair()





def Collected_Metadata(**args):
 ...
def FileUnit(**args):
 ...
def FieldCollections (**args):
 ...
# from mainModules.disasterPrevention.mylogger import applogger
################################################################################################################


def build_preflight_response():
    """ Handle browsers that prefight a "complex" POST with OPTIONS  """

    resp = make_response("", 200)
    # Just parrot the origin back for now.
    # If they don't give one, they don't get one.
    resp.headers.add('Access-Control-Allow-Origin', '*')
    # resp.headers["Access-Control-Allow-Origin"] = request.headers.get("Origin", "*")
    # No need for GET with RPC
    resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS, GET"
    # Allow a max age of one day
    resp.headers["Access-Control-Max-Age"] = 24 * 3600
    # Chrome wants this; one may choose to support additional custom
    # headers in a actual application.
    # resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    # return resp, 200

    # decorators =[cross_origin]
    # resp = make_response()
    resp.headers.add('Access-Control-Allow-Headers', '*')
    # resp.headers.add('Access-Control-Allow-Methods', '*')
    # resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp, 200

def corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

#################################################################################################################

# USER REGISTRATION FORM

class StaffRegisterAPI(MethodView):


    def options(self):
        if request.method == 'OPTIONS':
            return build_preflight_response()

        # if (request.method != 'GET' and request.method != 'DELETE') and not request.form or request.form:
        #     abort(400)


    # REGISTRATION ENDPOINT /staff/register
    def get(self):
        try:
            request.headers["username"]
            return StaffProfiles.objects.filter(username=request.headers["username"]).to_json()
        except:
            return StaffProfiles.objects().to_json()

        


    def post(self):
 

        first_name = request.json['first_name']
        last_name = request.json['last_name']
        username = request.json['username']
        #staffid = request.json["staffid"]
        email = request.json['email']
        tel = request.json['tel']

        password = request.json['password'].encode('utf-8')


        
     

      

        # applogger("new signup post request")

        # TODO More Validation to ensure no empty data for all required fields
        if not "username" in request.json and not "email" in request.json:
            error = {
                "USERNAME_OR_EMAIL_IS_MISSING"
            }
            return jsonify({'error': error}), 200



        existing_user = StaffProfiles.objects.filter(username=username).first()
        existing_email = StaffProfiles.objects.filter(email=email).first()
     



        if existing_user:
            error = {
                "code": "USERNAME_IS_TAKEN"
            }
            return jsonify({'error': error}), 200

        elif existing_email:
            error = {
                "code": "EMAIL IS ALREADY IN USE"
            }
            return jsonify({'error': error}), 200



        else:
            # create the StaffProfiles account
          
            hashed_password=hash_text(password)
            newtoken=gentoken(username, password)

            #if chief statusver=True  and statusacc=True else statusver=False and statusacc=False
            StaffProfilesEntry = StaffProfiles(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                tel=tel,
                passwordhash=hashed_password,
                specialty=specialty,
                specialty_description=specialty_description,
                verification_status=verification_status,
                acceptance_status=acceptance_status,
                timeOfRegistration=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(float(time.time()+10800))))
            )
            StaffProfilesEntry.save()
            for items in StaffProfiles.objects.filter(username=username):
                if items.verification_status == True and items.acceptance_status == False:
                        return jsonify({"status":"Contact Administration for further directions"}), 200

                elif items.verification_status == False:
                        return jsonify({"status":"Contact Administration for account verification"}), 200

                elif items.verification_status == True and items.acceptance_status == True:
                    ...

            #send email
    
            
            # session['username']=username
            # message={"success":"registration successful"}
            # dict1={"first_name":first_name, "last_name":last_name,"username":username,"email":email, "specialty":specialty, "specialty_description":specialty_description, "verification_status":verification_status,"acceptance_status":acceptance_status}
            
            #Call homepage variables
            #Call pubkey from daily cert table
            # for items in DailyKeyPairs.objects.order_by("-timeOfRegistration").first():
            #     pubkey=items.pubkey
           
            pubkey=None
            loginbody={"token":newtoken, "pubkey":pubkey, "status":username+" logged in", "specialty" : specialty}
            # resp=Response(jsonify(loginbody))
            # resp.headers.add("Access-Control-Allow-Origin", "*")
            # resp.headers.add("Access-Control-Allow-Origin", "*")
            # resp.headers.add('Access-Control-Allow-Headers', "*")
            # resp.headers.add('Access-Control-Allow-Methods', "*")
            # return resp, 200

            # return jsonify(loginbody), 200
            return corsify_actual_response(jsonify(loginbody)),200


# USER LOGIN API
class StaffLoginPageAPI(MethodView):

    def options(self):
        if request.method == 'OPTIONS':
            return build_preflight_response()



    # USER LOGIN ENDPOINT /

    #GET REACT HTML
    def get(self):
        return jsonify({"status":"post login"})

   
    def post(self):
        # a=[]
        # for items in StaffProfiles.objects.all():
        #     a.append(items.username)
        # return str(a)

        #Check if new account is Chief


        username = request.json['username']
        password = request.json['password'].encode("utf-8")
        #pubkey=request.json['pubkey']
      
        #get public key params
        #pubkey=request.headers["public_key"]

        

        usernamelist=StaffProfiles.objects.all().values_list('username')
        #print(usernamelist)
    

        # Check if user exists
        for items in usernamelist:
        # StaffProfiles.objects.filter(username=username):
            if not usernamelist:
                error = {
                "code": "USER_DOES_NOT_EXIST"
                }
                return jsonify({"error": error}), 200


        
        hashed_password=hash_text(password)
        # print (digest.hexdigest())
        # print (ResearcherTablerow.passwordhash)
        if StaffProfiles.objects.filter(username=username):
            for items in StaffProfiles.objects.filter(username=username):
                tblpasswordhash=items.passwordhash



                if  hashed_password != tblpasswordhash:
                    error = {
                        "code": "INCORRECT USERNAME OR PASSWORD"
                    }
                    return jsonify({"error": error}), 200 
                    #redirect (url_for("auth_app.loginpage_api", message="INCORRECT USERNAME OR PASSWORD"))

                elif items.verification_status == True and items.acceptance_status == False:
                    return jsonify({"status":"Contact Administration for further directions"}), 200

                elif items.verification_status == False:
                    return jsonify({"status":"Contact Administration for account verification"}), 200

                elif items.verification_status == True and items.acceptance_status == True:
                    # session['username']=username
                    #print(StaffProfilesrow.specialty)

                    newtoken=gentoken(username, password)
                    # category=categoryfind(newtoken) # if chief homepage dict
                    

                    #Call homepage variables
                    # #Call pubkey from daily cert table
                    # for items in DailyKeyPairs.objects.order_by("-timeOfRegistration").first():
                    #     pubkey=items.pubkey
                 
                    loginbody={"token":newtoken}
                    return  jsonify(loginbody), 200
        else:
            error = {
                "code": "USER_DOES_NOT_EXIST"
                }
            return jsonify({"error": error}), 200
            # return "fail"
            # # return redirect(url_for('auth_app.homepage_api', category=category))










# STAFF FORGOT PASSWORD

class StaffEmailForgotPasswordAPI(MethodView):

    def options(self):
        if request.method == 'OPTIONS':
            return build_preflight_response()

    def get (self):
        ##REACT HTML
        ...

    def post(self):
        email=request.json['email']
        emails=[]
        for names in StaffProfiles.objects.filter(email=email):
            emails.append(names.email)
        # email="marknjoroge.m@gmail.com"
        # if email != "today":
        if email in emails:
            # url="https://hgh-obs.com/forgotpassword/"
            recoverparams=hash_text(email+time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(float(time.time()+10800)))) + str(r(0,1000000000000000000000000)))
            RecoverPassword(recoverparams=recoverparams,email=email,timeOfRegistration=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(float(time.time()+10800))))).save()
            msgtype ="Confirmation email"
            recipientlist=emails
            subject="institution: "+msgtype
            body=recoverparams
            #resp=mymailer(recipientlist, msgtype, subject, body)

            # #send_email(email, recoveryparams)
            # recoverparams="today"
            # recepientdict={email:recoverparams}
            # try:
            # mailer(recepientdict)
            #, "response":resp}
            return jsonify({"success":recoverparams, "email": email}), 200
            # except Exception as e:
            #     return str(e)
        else:
            return jsonify ({"success":"if email in records recovery link shall be sent"}),200




class NewPasswordAPI(MethodView):

    def options(self):
        if request.method == 'OPTIONS':
            return build_preflight_response()


    def get(self):
        ...

    def post(self):
        #if reset params in reset password db, if not in db (invalid link), if status off in db, link expired
        recoverparams=request.headers['recoverparams']

        for names in RecoverPassword.objects.filter(recoverparams=recoverparams):
            if names.recoverparams==recoverparams:
                if names.recoverparamsstatus==False:
                    password=request.json['password']
                    names.update(recoverparamsstatus=True)
                    for identity in StaffProfiles.objects.filter(email=names.email):
                        passwordhash=hash_text(password)
                        identity.update(passwordhash=passwordhash, verification_status=False)
                        #to change passwordhash to list of tuples with timestamp and password as values. Append new tuple to list
                        #send email
                    message,code={"success":"password changed, reverify account with admin" },200
                    return jsonify(message),code
                    
                else:
                    message, code={"fail":"expired link"},200
                    return jsonify(message),code
            else:
                 message,code={"fail":"check recovery url"},200
                 return jsonify(message),code
        

# LOGOUT PAGE
class LogoutPageAPI(MethodView):

    decorators = [auth_required]


    def options(self):
        if request.method == 'OPTIONS':
            return build_preflight_response()
    
    # ADMIN ENDPOINT /logout/
    def get(self):
        ...
        # session.pop('username')
        # return redirect(url_for('auth_app.loginpage_api'))

    def post(self):
        #if token in params
        if request.headers["token"]:
            token=request.headers["token"]
        else:
            return jsonify({"error":"wrong device"}), 200
        for items in Tokens.objects.filter(token=token):
            items.update(status=False)
        return jsonify({"success":"logged out"}), 200
        #check token and change status and pop username
        ...



#######################################################################################################################################################

class StaffHomePageAPI(MethodView): 

    #get token from params
    #decrypt body and get message
    #verify signed text with body
    
    decorators = [auth_required]


    def options(self):
        if request.method == 'OPTIONS':
            return build_preflight_response()

    


    # HOMEPAGE USER
    def get(self):
        if not Tokens.objects.filter(token=request.headers["token"]):
            return "today"
        else:
            for user in Tokens.objects.filter(token=request.headers["token"]):
                username = user.username
            return username


    def post(self):
        #homepage params
        pass



# HOME PAGE ADMIN
class ChiefHomePageAPI(MethodView):

    def options(self):
        if request.method == 'OPTIONS':
            return build_preflight_response()


    # HOMEPAGE ENDPOINT /auth/signup/
    def get(self):

        return "success"


    def post(self):
        #profile, module access, params
        pass























