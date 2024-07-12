from flask import Flask
from flask_mail import Message
from settings import mail_settings
from application import mail

#from flask_mail import Mail
#app = Flask(__name__)
#mail = Mail(app)

def mailer(recepientdict)   :
    recepientlist=[]
    

    for key in recepientdict:
        recepientlist.append(recepientdict)

        msg = Message(subject="HARGEISA OBSTETRICS AND GYNAECOLOGY : Account Verification",
                      sender=mail_settings["MAIL_USERNAME"],
                      recipients=recepientlist, # replace with your email for testing
                      body="https://hgh-obs.com/staff/forgotpassword?recoverparams="+recepientdict[key])
        mail.send(msg)
    return "success"




def mymailer(recipientlist, msgtype, subject, body):
   msg = Message(
                subject,
                sender ='hargeisaobstetrics@hghobs.com',
                recipients = recipientlist
               )
   msg.body = body
   mail.send(msg)
   resp=msgtype+" sent to "+str(recipientlist)
   return resp
# from flask import Flask
  

# app = Flask(__name__)

# @app.route('/url')
# def hello_world():
#     mail = Mail(app)

#     for key in recepientdict:
#         recepientlist.append(recepientdict)

#         msg = Message(subject="HARGEISA OBSTETRICS AND GYNAECOLOGY : Account Verification",
#                       sender=mail_settings["MAIL_USERNAME"],
#                       recipients=recepientlist, # replace with your email for testing
#                       body="https://hgh-obs.com/staff/forgotpassword?recoverparams="+recepientdict[key])
#         mail.send(msg)
#         return 'Hello World'
        
  
# # main driver function
# if __name__ == '__main__':
  
#     # run() method of Flask class runs the application 
#     # on the local development server.
#     app.run()







# from flask import Flask
# from flask_mail import Mail, Message
# import os

# app = Flask(__name__)

# mail_settings = {
#     "MAIL_SERVER": 'smtp.gmail.com',
#     "MAIL_PORT": 587,
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": 'mbatiacisco@gmail.com',
#     "MAIL_PASSWORD": 'iajfpcyuvzgefgyr'
# }

# app.config.update(mail_settings)
# mail = Mail(app)

# # if __name__ == '__main__':
# #     with app.app_context():
#         msg = Message(subject="Hello",
#                       sender='mbatiacisco@gmail.com',
#                       recipients=["marknjoroge.m@gmail.com"], # replace with your email for testing
#                       body="This is a test email I sent with Gmail and Python!")
#         mail.send(msg)




# The port for SSL is 465 and not 587, however when I used SSL the mail arrived to the junk mail.

# For me the thing that worked was to use TLS over regular SMTP instead of SMTP_SSL.

# Note that this is a secure method as TLS is also a cryptographic protocol (not unlike SSL).

# import smtplib, ssl

# port = 587  # For starttls
# smtp_server = "smtp.gmail.com"
# sender_email = "mbatiacisco@gmail.com"
# receiver_email = "marknjoroge.m@gmail.com"
# password = 'iajfpcyuvzgefgyr'
# message = """\
# Subject: Hi there

# This message is sent from Mamtaa."""

# context = ssl.create_default_context()
# with smtplib.SMTP(smtp_server, port) as server:
#     server.ehlo()  # Can be omitted
#     server.starttls(context=context)
#     server.ehlo()  # Can be omitted
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)





# import smtplib
# import os
# def mail():
#     try:
#         mailuser = 'mbatiacisco@gmail.com'

#         mailpasswd = 'iajfpcyuvzgefgyr'

#         fromaddr = 'mbatiacisco@gmail.com'

#         toaddrs = 'marknjoroge.m@gmail.com'

#         msg ="hello"



#         server = smtplib.SMTP_SSL('smtp.google.com')

#         server = smtplib.SMTP_SSL_PORT=587

#         server.user(mailuser)

#         server.pass_(mailpasswd)

#         server.set_debuglevel(1)

#         server.sendmail(fromaddr, toaddrs, msg)

#         server.quit()
#     except Exception as e:
#         return str(e)
#     os.system('echo "success1"')
#     print ("success2")
#     return "success3"

# mail()
