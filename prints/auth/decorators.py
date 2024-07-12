# On this Decorator, we check if the token passed is valid
from functools import wraps
import time
from random import randint as r

from flask import redirect, url_for,session, request, jsonify


from prints.auth.models import StaffProfiles, Tokens, DailyKeyPairs
from mainModules.crypto.myHasher import hash_text
from mainModules.crypto.mySigner import verify
from mainModules.crypto.myEncrypter import myDecrypter

# from flask_cors import cross_origin




# def cross_origin(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         cross_origin(origin='*',headers=['Content-Type','Authorization'])

#         return f(*args, **kwargs)
#     return decorated_function




def auth_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):

        try:
            #add token table verification, token status check and user name fetch

            #if token in params
            if request.headers["token"]:
                token=request.headers["token"]
                
            else:
                return jsonify({"error":"wrong device"}), 401

            #if token in table    
            # if not Tokens.objects.filter(token=token):
            #     return jsonify({"error":"wrong devices"})

            try:
                for items in Tokens.objects.filter(token=token):
                    username=items.username

                    if items.status==False:
                        return jsonify({"error":"kindly login again"}), 401
                    else:
                        pass
            
                    for name in StaffProfiles.objects.filter(username=username):
                        #rejected
                        if name.verification_status==True and name.acceptance_status==False:
                            #return redirect(url_for('admin_app.applicationrejected_api'))
                            return jsonify({"error":"account rejected"}), 401
                        
                        #unverified
                        elif name.verification_status==False:
                            return jsonify({"error":"kindly contact admin for account verification"}), 401
                            
                        
                        elif name.verification_status==True and name.acceptance_status==True:
                            ...
            except:
                return jsonify({"error":"wrong devices"}) ,406


                    

                        #return redirect(url_for('admin_app.waitforadminverif_api'))
                        #try:
                        #     pubkey=items.pubkey
                        #     message=request.form['message']
                        #     #message=decryptedmessage
                        #     signed=request.form['signed']
                        #     if verify(message, signed, pubkey) == "success":
                        #         ...
                        #     else:
                        #         return jsonify({"error":"sender not verified"})
                        # #decryption and signature verification

            # except:
            #     return jsonify({"error":"wrong devices"})
            #     return jsonify({"error":"kindly log in"})
        except AttributeError as err:
            return jsonify({"error":str(err)})
        except KeyError:
            return jsonify({"error":"kindly log in KeyError"}), 403

        return f(*args, **kwargs)
    return decorated_function




        
def username_fetch(token):
    #add token table username fetch
    for names in Tokens.objects.filter(token=token):
        username=names.username
    return username

        
def username_fetch(token):
    #add token table username fetch
    for names in Tokens.objects.filter(token=token):
        username=names.username
    return username



# ip whitelist method
def ip_check():
    #get ip check lib
    #confirm if ip in list else redirect
    #if check pass
    clientip=request.remote_addr
    clientip=request.environ['REMOTE_ADDR']

    #to comprise of hospital local desktop static IPs
    iplist=[]
    
    if clientip not in iplist:
        abort(403)
        return ("Unknown user")
    ...




# time to leave method
def timeoutcheck(clienttimestamp):
    endtime=clienttimestamp+30
    nowtime=time.time()
    if nowtime>endtime:
        abort(400, "timeoutcheck")



# category check for page provision
def categoryfind(token):
    username=username_fetch(token) 
    for names in StaffProfiles.objects.filter(username=username):
        category=names.specialty
    return category



def gentoken(username, password):
        #Token generation
        now=time.time()
        expiry_time=now+3600

        pretoken=username+str(password)+str(now)+str(expiry_time) + str(r(0,1000000000000000000000000))

        newtoken=hash_text(pretoken)

        #Call pubkey from daily cert table
        # for items in DailyKeyPairs.objects.order_by("-timeOfRegistration").first():
        #     pubkey=items.pubkey
        pubkey=None

        #Token Table Update
        newToken=Tokens(username=username, token=newtoken, timeOfRegistration=now, timeofexpiry=expiry_time, pubkey=pubkey, status=True)
        newToken.save()
        return newtoken
