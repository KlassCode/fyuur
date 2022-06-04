import os
from pickle import TRUE
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:nbaklass0597@localhost:5432/flyuur'
SQLALCHEMY_TRACK_MODIFICATIONS=True