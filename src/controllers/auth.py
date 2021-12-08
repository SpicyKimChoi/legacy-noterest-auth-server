from flask_restx import Resource
from flask import request

from src.services.user_service import UserService
from src.utils.user_dto import UserDTO
from src.utils.user_respond import SigninSuccessful, SignupSuccessful, AlreadyExistEmail, AlreadyExistNick, UserNotFound, ServerError

api = UserDTO.auth

@api.route('/signup')
class Signup(Resource):
    @api.expect(UserDTO.user_register_field)
    @api.doc(responses=SignupSuccessful.get_doc())
    @api.doc(responses=AlreadyExistEmail.get_doc())
    @api.doc(responses=AlreadyExistNick.get_doc())
    @api.doc(responses=ServerError.get_doc())
    def post(self):
        email = request.json['email']
        nickname = request.json['nickname']
        password = request.json['password']

        us = UserService()
        signup = us.signup(email,nickname,password)

        return signup.get_respond()
        

@api.route('/login')
class Signin(Resource):
    @api.expect(UserDTO.user_login_field)
    @api.doc(responses=SigninSuccessful.get_doc())
    @api.doc(responses=UserNotFound.get_doc())
    @api.doc(responses=ServerError.get_doc())
    def post(self):
        email = request.json['email']
        password = request.json['password']

        us = UserService()
        signin = us.signin(email,password)

        return signin.get_respond()


