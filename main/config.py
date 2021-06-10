from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
	SECRET_KEY = environ.get('SECRET_KEY')
	MIRROR_API_URL_PREFIX = environ.get('MIRROR_API_URL_PREFIX') or ''

	DEBUG = int(environ.get('DEBUG')) if environ.get('DEBUG') else 1
	TESTING = int(environ.get('TESTING')) if environ.get('TESTING') else 1

	POSTGRES_DB_URI = {
		'user': environ.get('POSTGRES_DB_USERNAME'),
		'pw': environ.get('POSTGRES_DB_PASSWORD'),
		'db': environ.get('POSTGRES_DB_DATABASE'),
		'host': environ.get('POSTGRES_DB_HOST'),
		'port': environ.get('POSTGRES_DB_PORT'),
	}
	SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES_DB_URI