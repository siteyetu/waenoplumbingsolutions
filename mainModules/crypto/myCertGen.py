from Crypto.PublicKey import RSA 
from prints.auth.models import DailyKeyPairs
from time import time as now
import os

certdir="./docs/documentation/certs"

def genKeys(privatename, publicname, passphrase):
	keypair=RSA.generate(4096)
	public_key=keypair.publickey()
	if passphrase:
		passphrase=passphrase
	else:
		passphrase=None

	privlocation=os.path.join(certdir,privatename)
	publocation=os.path.join(certdir,publicname)

	with open (privlocation+".ppk", "wb") as files:
		private_key=keypair.exportKey("PEM",passphrase)
		files.write(private_key)
		files.close()

	with open (publocation, "wb") as files:
		public_key=public_key.exportKey("PEM",passphrase)
		files.write(public_key)
		files.close()

	pairdb=DailyKeyPairs(privkey=private_key, pubkey=public_key, timeOfRegistration=now())
	pairdb.save()