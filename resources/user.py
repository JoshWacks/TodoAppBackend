from flask_restful import Resource
from models import db

class User(Resource):

    def __init__(self, id, api_key,username, first_name, last_name, password, email_address):
        self.id =id,
        self.api_key = api_key
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email_address = email_address

    def serialize(self):
        return {
            'id' : self.id,
            'api_key' : self.api_key,
            'username' : self.username,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'email_address' : self.email_address,
            'password' : self.password,

        }


    def get(self):
        return {"message":"Hello World!"}
