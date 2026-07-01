import os

SECRET_KEY = os.urandom(24)
SQLALCHEMY_DATABASE_URI = 'sqlite:///iam.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'replace-with-a-secure-random-key'

