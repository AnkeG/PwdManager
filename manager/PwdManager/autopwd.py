import string, secrets

def autopwd(length = 10, numofdigits = 3):
	alphabet = string.ascii_letters + string.digits +string.punctuation
	while True:
		password = ''.join(secrets.choice(alphabet) for i in range(length))
		if (any(c.islower() for c in password)
			and any(c.isupper() for c in password)
			and any(c.isalnum()==False for c in password)
			and sum(c.isdigit() for c in password)>=numofdigits):
			break
	return password