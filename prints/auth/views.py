from flask import Blueprint
from .api import  *


auth_app = Blueprint("auth_app", __name__)




##################################################################################################################


# NEW USER LOGIN ENDPOINT URL
stafflogin_view = StaffLoginPageAPI.as_view('staffloginpage_api')

auth_app.add_url_rule('/staff/login',
	view_func=stafflogin_view, 
	methods=['POST'])


# NEW USER REGISTER ENDPOINT URL
staffregister_view = StaffRegisterAPI.as_view('staffregisterpage_api')

auth_app.add_url_rule('/staff/register', 
	view_func=staffregister_view, 
	methods=['POST', 'GET'])




# NEW LOGOUT ENDPOINT URL
logout_view = LogoutPageAPI.as_view('logout_api')

auth_app.add_url_rule('/staff/logout', 
	view_func=logout_view, 
	methods=['POST'])

#####################################################################################################################################################

# NEW HOMEPAGE ENDPOINT URL
staffhomepage_view = StaffHomePageAPI.as_view('staffhomepage_api')

auth_app.add_url_rule('/staff/home', 
	view_func=staffhomepage_view, 
	methods=['POST', 'GET' ])



# ADMIN HOMEPAGE ENDPOINT URL
chiefhomepage_view = ChiefHomePageAPI.as_view('chiefhomepage_api')

auth_app.add_url_rule('/chief/home', 
	view_func=chiefhomepage_view, 
	methods=['POST', 'GET' ])






##############################################################################################################

# STAFF SEND PASSWORD TO GET RECOVERY

staffEmailForgotPasswordAPI_view=StaffEmailForgotPasswordAPI.as_view('staffEmailForgotPassword_api')

auth_app.add_url_rule('/staff/forgotpassword', 
	view_func=staffEmailForgotPasswordAPI_view ,
	methods=['POST'])




#NEW PASSWORD SET

newPasswordAPI_view=NewPasswordAPI.as_view('newPassword_api')

auth_app.add_url_rule('/staff/newpassword', 
	view_func=newPasswordAPI_view,
	methods=['POST' ])


###############################################################################################################

# # VIEW STATS 
# viewstats_view = ViewStatsAPI.as_view('viewstats_api')

# auth_app.add_url_rule('/viewstats', 
# 	view_func=viewstats_view, 
# 	methods=['POST', 'GET' ])


# # VIEW STATS            
# viewstatsv2_view  = ViewStatsv2API.as_view('viewstatsv2_view')

# auth_app.add_url_rule('/api/v2/viewstats',
#         view_func=viewstatsv2_view,
#         methods=['POST', 'GET' ])


