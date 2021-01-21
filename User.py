from flask import Flask, session
from passlib.hash import pbkdf2_sha256
import json
import uuid
import jsonify
import datetime

class User:

    def start_session(self, user):
        session['logged_in'] = True
        session['User'] = user
        return json.dumps(session)



    def signup(self, email, password):

        user = {
            "_id" : uuid.uuid4().hex,
            "email" : email,
            "password" : password,
            "datetime" : datetime.datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)"),
            "accesstoken" : "access-sandbox-405cd7bb-d2be-4fbc-88b8-065c589ce509"


        }

        user["password"] = pbkdf2_sha256.encrypt(user["password"])

        return user
