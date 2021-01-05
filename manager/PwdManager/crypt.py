from cryptography.fernet import Fernet

def new_key():
	return Fernet.generate_key()

def read_key(key):
	return Fernet(key)

def encrypt_pwd(cipher, s):
	return cipher.encrypt(str.encode(s))

def decrypt_pwd(cipher, text):
	return cipher.decrypt(text).decode()