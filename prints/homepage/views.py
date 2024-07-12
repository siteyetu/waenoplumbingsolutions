from flask import Blueprint
from .api import  *


homepage_app = Blueprint("homepage_app", __name__)


homepage_view = HomePageAPI.as_view('homepage_api')

homepage_app.add_url_rule('/', 
	view_func=homepage_view, 
	methods=['GET'])



contactus_view = ContactUsAPI.as_view('contactus_api')

homepage_app.add_url_rule('/contactus', 
	view_func=contactus_view, 
	methods=['GET', 'POST'])


aboutus_view = AboutUsAPI.as_view('aboutus_api')

homepage_app.add_url_rule('/aboutus', 
	view_func=aboutus_view, 
	methods=['GET'])