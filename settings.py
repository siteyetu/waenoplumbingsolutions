import os


SECRET_KEY = 'going productions-copy-blueprints-chef'
DEBUG=True

MONGODB_SETTINGS = {
	'DB' : 'bluePrintsDB',
	'HOST' : '127.0.0.1',
	'PORT' : 27017
	}
	
# MONGODB_SETTINGS = {
# 	'DB' : 'separateDatabaseForAudit',
# 	'HOST' : '127.0.0.1',
# 	'PORT' : 27017
# 	}

TEXT_UPLOAD_FOLDER = './docs/uploads/text'
AUDIO_UPLOAD_FOLDER = './docs/uploads/audio'
IMAGE_UPLOAD_FOLDER = './docs/uploads/images'
OTHERS_UPLOAD_FOLDER = './docs/uploads/others'

KYC_UPLOAD_FOLDER = './docs/uploads/kyc'
EXCEL_DOWNLOAD_FOLDER = './docs/downloads/excel'


STATIC_IMAGE_URL = 'images'
STATIC_KYC_URL = 'kyc'
STATIC_PDFS_URL = 'pdfs'
STATIC_EXCEL_URL = 'excel'

IMAGE_ALLOWED_EXTENSIONS = set(['bmp', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'svgj'])
KYC_ALLOWED_EXTENSIONS = set(['txt', 'pdf'])

CORS_HEADERS = 'Content-Type'


mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'a@gmail.com',
    "MAIL_PASSWORD": 'a'
}
