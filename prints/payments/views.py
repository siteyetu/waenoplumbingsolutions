from flask import Blueprint
from .api import  *


payments_app = Blueprint("payments_app", __name__)


newpayments_view = NewPaymentsAPI.as_view('newpayments_api')

payments_app.add_url_rule('/payments/new', 
	view_func=newpayments_view, 
	methods=['POST'])


ipnlist_view = IPNListAPI.as_view('ipnlist_api')

payments_app.add_url_rule('/payments/ipnlist', 
	view_func=ipnlist_view, 
	methods=['GET'])




ipnstatus_view = IPNStatusAPI.as_view('ipnstatus_api')

payments_app.add_url_rule('/payments/ipnstatus',
	view_func=ipnstatus_view, 
	methods=['GET'])


submitorderrequest_view = SubmitOrderRequestAPI.as_view('submitorderrequest_api')

payments_app.add_url_rule('/payments/submitorderrequest', 
	view_func=submitorderrequest_view, 
	methods=['GET'])
