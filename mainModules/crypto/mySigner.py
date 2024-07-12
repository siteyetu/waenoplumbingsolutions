from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA


from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

from Crypto.Cipher import AES, PKCS1_OAEP




# signer and verifier to be called when signing strings to finserve and verifying signature from apps
def mySigner(concatenatedString):
	unsigned=concatenatedString.encode('utf-8')

		

	# with open("./docs/uploads/keys", "r") as myfile:
	#     private_key = RSA.importKey(myfile.read())
	#Daily Key Pairs private key retrieval
	for keys in DailyKeyPairs.objects.order_by('-timeOfRegistration').first():
	 	private_key=keys.privkey


	un_signed = SHA256.new(unsigned)
	signature = pkcs1_15.new(private_key).sign(un_signed)
	signer = PKCS1_v1_5.new(private_key)
	signBase64 = b64encode(sigBytes)

	#print (signBase64, digest)

	return signBase64, signature



#To recieve body and signed body from client, counter check with client public key 
def verify(signature, decryptedbody, key):

	# with open(u"./mainModules/myCryptofunction/publickey.pem", "r") as myfile:
	#     public_key = RSA.importKey(myfile.read())
	#Token table public key retrieval
	 # for keys in DailyKeyPairs.objects.order_by('-timeOfRegistration').first():
	 # 	public_key=keys.publickey

	#verifier = PKCS1_v1_5.new(public_key)
	
	body=SHA256.new(decryptedbody)


	try:
		pkcs1_15.new(key).verify(body, signature)
		print ("The signature is valid.")
		return "success"
	except (ValueError, TypeError):
		print ("The signature is not valid.")
		return "error"
	
	# assert, 'Signature verification failed'
	# print ("successful verification")




# digesterval=mySigner("twende")[0]
# sigBytes=mySigner("twende")[1]



# if myVerifier(digesterval, sigBytes)=='successful verification':
#         print('twende kass')
# elif myVerifier(digesterval, sigBytes)=='Verification failed':
#         print ('verification failed')
# else:
#         print ('unknown error')

