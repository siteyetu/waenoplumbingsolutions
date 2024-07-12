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


defurl = "http://127.0.0.1:5000/payments"

#################################################################################################################





class NewPaymentsAPI (MethodView):


	# decorators = [auth_required]

	def options(self):
	    if request.method == 'OPTIONS':
	        return build_preflight_response()



	def post(self):

		paymentinfo = request.json

		paymentinfolist = ["id","currency","amount", "description"]
		addresslist = ["email_address", "phone_number", "country_code", "first_name","middle_name","last_name","line_1",
		 "city","state","postal_code","zip_code"]


		for item in paymentinfolist:
			if item not in paymentinfo:
				return ("incomplete payment address, "+ item + " is misssing")
			if item == "billing_address":
				for obj in addresslist:
					if obj not in paymentinfo["billing_address"]:
						return ("incomplete billing address, "+ obj + " is misssing")


		paymentinfo["payid"]=paymentinfo["id"]
		del paymentinfo["id"]

		print(paymentinfo)
		#PaymentInfoTable(**paymentinfo).save()


		jsonh="application/json"

		headers = {
		"Accept":jsonh,
		"Content-Type":jsonh
		}

		body = {
		"consumer_key":"",
		"consumer_secret":""
		}


		url = "https://pay.pesapal.com/v3/api/Auth/RequestToken"

		response = requests.post(url, headers = headers, json = body)

		authresponse = json.loads(response.text)

		authresponse["nowtime"] = nowtime

		print (authresponse)

		#AuthTable(**authresponse).save()

		token=authresponse["token"]


		#register ipn url
		headers["Authorization"] = token

		body= {
		"id": defurl+"/ipnstatus",
		"ipn_notification_type": "GET"
		}


		url = " https://pay.pesapal.com/v3/api/URLSetup/RegisterIPN"

		response = requests.post(url, headers = headers, json = body)

		ipnresponse = json.loads(response.text)

		ipnresponse["nowtime"] = nowtime

		print ("ipnresponse")

		#IPNTable(**ipnresponse).save()

		ipn_id = ipnresponse["ipn_id"]


		#pay process 
		paymentinfo["notification_id"] = ipn_id
		paymentinfo["callback_url"] = defurl + "/submitorderrequest"


		body = paymentinfo

		url = " https://pay.pesapal.com/v3/api/Transactions/SubmitOrderRequest"

		response = requests.post(url, headers = headers, json = body)


		paymentresponse = json.loads(response.text)

		paymentresponse["nowtime"] = nowtime

		print(paymentresponse)

		#PaymentresponseTable(**paymentresponse).save()

		orderdetails = {}
		orderdetails["order_tracking_id"] = paymentresponse["order_tracking_id"]
		orderdetails["merchant_reference"] = paymentresponse["merchant_reference"]

		redirect_url = paymentresponse["redirect_url"]


		# user redirected to pesapal and makes payment then redirected to response page
		if status == "redirect":
			return redirect(redirect_url)
		elif status == "direct":
			return jsonify (orderdetails),paymentresponse["status"]




    
		


		


class  IPNListAPI (MethodView):

		def options(self):
			if request.method == 'OPTIONS':
			    return build_preflight_response()




		def get (self):

			listofdicts = json.loads(response.text)

			for dicts in listofdicts:
				dicts["nowtime"] = nowtime
				IPListTable (**dicts).save()

			return jsonify (response.text), 200





class IPNStatusAPI (MethodView):


	def options(self):
	    if request.method == 'OPTIONS':
	        return build_preflight_response()


	def get(self):

		IPNStatusDict = request.params

		IPNStatusDict["nowtime"] = nowtime

		IPNStatusTable(**IPNStatusDict).save()

		return ("success"),200



class  SubmitOrderRequestAPI (MethodView):


	def options(self):
	    if request.method == 'OPTIONS':
	        return build_preflight_response()


	def get(self):

		SubmitOrderRequestTable(**request.params).save()

		url = " https://pay.pesapal.com/v3/api/Transactions/GetTransactionStatus"

		response = requests.get(url, params= request.params["OrderTrackingId"])

		transactionstatusresponse = json.loads(response.text)

		transactionstatusresponse["nowtime"] = nowtime

		TransactionstatusTable (**transactionstatusresponse).save()

		transactionstatus = {}
		itemlist = ["payment_method","amount","created_date","confirmation_code"]

		for item in list1:
			transactionstatus [item] =  transactionstatusresponse [item]


		#return redirect to post with transactionstatus as body


		return jsonify(transactionstatus),200






	