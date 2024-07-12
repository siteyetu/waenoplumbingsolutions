from Crypto.Hash import SHA256

def hash_text(texts):
	try:
		texts=texts.encode("utf-8")
	except:
		pass
	digest = SHA256.new()
	digest.update(texts)
	newtext=digest.hexdigest()
	return newtext