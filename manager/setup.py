try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'discription': 'A password manager',
	'author': 'Anke Ge',
	'url':'URL',
	'download_url':'download_url',
	'author_email':'geanke20@gmail.com',
	'version':'0.1',
	'install_requires':['nose'],
	'packages':['NAME'],
	'scripts':[],
	'name': 'PwdManager'
	}

setup(**config)

