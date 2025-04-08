#!/usr/bin/env python3

#import the os module to access the environmental variables
import os

#import the load_dotenv function to load variables from a .env file
from dotenv import load_dotenv

#Load environmental variable froma .env file into the environment
load_dotenv()

#Define a configuration class to store application settings
class Config:
    #Get the database username from the environment variables
    DB_USERNAME  os.environ.get("DB_USERNAME")

    #Get the database password from the environment variables
    DB_PASSWORD  os.environ.get("DB_PASSWORD")

    #Get the database host
    DB_HOST  os.environ.get("DB_HOST")

    #Get the port number used by the database
    DB_PORT  os.environ.get("DB_PORT")

    #Get the database name
    DB_NAME  os.environ.get("DB_NAME")

    #Get the secret key used for the JWT or session managemnt
    SECRET_KEY = os.environ.get("SECRET_KEY")

    #Construct the full database URI that SQLAlchemy will use to connect to the MySQL
    SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}:@{DB_HOST}:{DB_PORT}:{DB_NAME}"

    #Disable SQLAlchemy event system to save memory
    SQLALCHEMY_TRACK_MODIFICATION = False
