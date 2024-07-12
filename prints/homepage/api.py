from flask.views import MethodView
from flask import request, abort, jsonify, render_template, redirect, url_for, session,send_from_directory, make_response

from .models import *
import uuid, json, importlib
import json, time
import requests

# response = requests.get(...)
# dictionary = json.loads(response.text)


# # Serializing json  
# json_object = json.dumps(dictionary)


#Time GMT +3
nowtime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(float(time.time()+10800))))



class HomePageAPI(MethodView):

	def get (self):
		return render_template('homepage/index.html')




class ContactUsAPI(MethodView):

	def get (self):
		return render_template('homepage/ContactUs.html')

	def post (self):
		formdata = dict(request.form)
		name, phone, email, message = formdata ['name'], formdata['phone'], formdata['email'], formdata['message']

		formdata["timeOfRegistration"] =time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(float(time.time()))))
		ContactUsTable(**formdata).save()
		return ContactUsTable.objects.all().to_json()
		#return str([name, phone, email, message])




class AboutUsAPI(MethodView):

	def get (self):
		return render_template('homepage/AboutUs.html')

