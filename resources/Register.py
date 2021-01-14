from flask_restful import Resource
from flask import request
from models import db, User 
import random
import string

class Register(Resource):
    def get(self):
        users = User.query.all()
        userList =[]
        for i in range(0,len(users)):
            userList.append(users[i].serialize())
        return { "status " : str(userList)}, 200

    def post(self):
        json_data = request.get_json(force=True)

        if not json_data:
            return {'message': 'No input data provided'}, 400

        user = User.query.filter_by(username=json_data['username']).first()
        if user:
            return {'message': 'Username not available'}, 400

        email = User.query.filter_by(username=json_data['email_address']).first()
        if email:
            return {'message': 'Email address already in use '}, 400

        api_key =self.generate_key()

        api_test = User.query.filter_by(api_key=api_key).first()
        if api_test:
            return {'message': 'API key already exists'}, 400

        user = User(
            api_key = api_key,
            username = json_data['username'],
            first_name = json_data['first_name'],
            last_name = json_data['last_name'],
            password = json_data['password'],
            email_address = json_data['email_address'],
            
        )

        db.session.add(user)
        db.session.commit()

        result = User.serialize(user)

        return {"statuc" : "success ", 'data':result}, 201

    def generate_key(self):
        return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(50))
     