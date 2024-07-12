from Crypto import *



from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA


from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

from Crypto.Cipher import AES, PKCS1_OAEP









# encryption, decryption and key generation methods
# to be used while generating encrypted strings to be parsed in routes for email confirmation and referral link identification
def myEncrypter(data):
	encdata = data.encode("utf-8")
	title=data+".bin"
	file_out = open(title, "wb")

	recipient_key = RSA.import_key(open("./mainModules/myCryptofunction/publickey.pem").read())
	session_key = get_random_bytes(16)

	# Encrypt the session key with the public RSA key
	cipher_rsa = PKCS1_OAEP.new(recipient_key)
	enc_session_key = cipher_rsa.encrypt(session_key)

	# Encrypt the data with the AES session key
	cipher_aes = AES.new(session_key, AES.MODE_EAX)
	ciphertext, tag = cipher_aes.encrypt_and_digest(encdata)
	[ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]




def myDecrypter(data):
        #enc_session_key, nonce, tag, ciphertext):
	title=data+".bin"
	file_in = open(title, "rb")

	private_key = RSA.import_key(open("./privatekey.pem").read())

	enc_session_key, nonce, tag, ciphertext = \
	[ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

	# Decrypt the session key with the private RSA key
	cipher_rsa = PKCS1_OAEP.new(private_key)
	session_key = cipher_rsa.decrypt(enc_session_key)

	# Decrypt the data with the AES session key
	cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
	newdata = cipher_aes.decrypt_and_verify(ciphertext, tag)
	print(newdata.decode("utf-8"))


def myKeyGenerator():
	key=RSA.generate(2048)
	private_key=key.export_key()
	file_out=open("private.pem", "wb")
	file_out.write(private_key)

	
	public_key=key.publickey().export_key()
	file_out=open("public.pem", "wb")
	file_out.write(public_key)



# required


# operation:save to db collection(mysafe)

# file.bin={
# 	enc_session_key:,
# 	cipher_aes.nonce:,
# 	tag:,
# 	ciphertext:}

# mysafe.collection schema
# username= userid
# transaction_id= <transactiontype-referral link/transactionnumber>
# [.bin filename path]= <random string gen, save to variable, save to db alongside username&transactionid>

# ciphertext.collection schema
# username
# ciphertext



# data objects:

# email verification
# link/<ciphertext>
# check ciphertext table
# if not present:
# 	return error message
# else:
# 	pass
# where username=username, fetch filepath/file.bin
# open filepath/file.bin
# read attributes
# decrypt
# if not success:
# 	return error message
# else:
# 	fetch data from dictionary
# update db username status
# redirect to login page, message=successfully verified



# page redirect referral link
# link/<ciphertext>
# check ciphertext table
# if not present:
# 	return error message
# else:
# 	pass
# where username=username, fetch filepath/file.bin
# open filepath/file.bin
# read attributes
# decrypt
# if not success:
# 	return error message
# else:
# 	fetch data from dictionary
# update db username status
# redirect to referenced page, message=welcome to this page





