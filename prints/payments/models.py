from application import db



class AuthTable (db.Document):
	first_name = db.StringField(db_field="first_name", required=True, max_length=50)
	tokens  = db.StringField(db_field="tokens")
	expiryDatee  = db.StringField(db_field="expiryDatee")
	error = db.BooleanField(db_field="error")
	status  = db.StringField(db_field="status")
	nowtime = db.StringField(db_field="nowtime")
	message = db.StringField(db_field="message")




class IPNTable (db.Document):
	url = db.StringField(db_field="url")
	created_date = db.StringField(db_field="created_date")
	ipn_id = db.StringField(db_field="ipn_id")
	error = db.BooleanField(db_field="error")
	status  = db.StringField(db_field="status")
	nowtime = db.StringField(db_field="nowtime")



class PaymentInfoTable (db.Document):
	payid = db.StringField(db_field="payid-3344ZZ")
	currency = db.StringField(db_field="currency")
	amount = db.FloatField(db_field="amount")
	description = db.StringField(db_field="description")
	callback_url = db.StringField(db_field="callback_urle")
	notification_id = db.StringField(db_field="notification_id")
	billing_address = db.DictField(db_field="billing_address")

    # email_address = db.StringField(db_field="")
    # phone_number = db.StringField(db_field="")
    # country_code = db.StringField(db_field="")
    # first_name = db.StringField(db_field="")
    # middle_name = db.StringField(db_field="")
    # last_name = db.StringField(db_field="")
    # line_1 = db.StringField(db_field="")
    # line_2 = db.StringField(db_field="")
    # city = db.StringField(db_field="")
    # state = db.StringField(db_field="")
    # postal_code = db.StringField(db_field="")
    # zip_code = db.StringField(db_field="")
	






class TransactionStatusTable(db.Document):
	payment_method = db.StringField(db_field="payment_method")
	amount = db.FloatField(db_field="amount")
	created_date = db.StringField(db_field="created_date")
	confirmation_code = db.StringField(db_field="confirmation_code")
	payment_status_description = db.StringField(db_field="payment_status_description")
	description = db.StringField(db_field="description")
	message = db.StringField(db_field="message")
	payment_account = db.StringField(db_field="476173**payment_account")
	call_back_url = db.StringField(db_field="call_back_url")
	status_code = db.StringField(db_field="status_code")
	merchant_reference = db.StringField(db_field="merchant_reference")
	payment_status_code = db.StringField(db_field="payment_status_code")
	currency = db.StringField(db_field="currency")
	error = db.StringField(db_field="error")
	status  = db.StringField(db_field="status")
	nowtime = db.StringField(db_field="nowtime")


    # ": {
    # error_type = db.BooleanField(db_field="error")
    # code = db.BooleanField(db_field="error")
    # message = db.BooleanField(db_field="error")
    # call_back_url": null
	# },


class PaymentresponseTable (db.Document):
	order_tracking_id = db.StringField(db_field="order_tracking_id")
	merchant_reference = db.StringField(db_field="merchant_reference")
	redirect_url = db.StringField(db_field="redirect_url")
	error = db.BooleanField(db_field="error")
	status  = db.StringField(db_field="status")
	nowtime = db.StringField(db_field="nowtime")



class IPListTable (db.Document):
	url = db.StringField(db_field="url")
	created_date = db.StringField(db_field="created_date")
	ipn_id = db.StringField(db_field="ipn_id")
	error = db.BooleanField(db_field="error")
	status  = db.StringField(db_field="status")
	nowtime = db.StringField(db_field="nowtime")



class IPNStatusTable (db.Document):
	OrderTrackingId= db.StringField(db_field="OrderTrackingId")
	OrderNotificationType = db.StringField(db_field="OrderNotificationType")
	OrderMerchantReference = db.StringField(db_field="OrderMerchantReference")
	nowtime = db.StringField(db_field="nowtime")



class OrderResponseTable (db.Document):
	OrderTrackingId= db.StringField(db_field="OrderTrackingId")
	OrderNotificationType = db.StringField(db_field="OrderNotificationType")
	OrderMerchantReference = db.StringField(db_field="OrderMerchantReference")
	nowtime = db.StringField(db_field="nowtime")