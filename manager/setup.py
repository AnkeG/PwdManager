try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'discription': 'A password manager',
	'author': 'Anke Ge',
	'url':'URL',
	'download_url':'download_url',
	'author_email':'geanke12@gmail.com',
	'version':'0.1',
	'install_requires':['sqlite3', 'cryptography', 'pyperclip',],
	'packages':[],
	'scripts':[],
	'name': 'PwdManager'
	}

setup(**config)

