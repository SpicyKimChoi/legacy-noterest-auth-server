"""유저 인증 컨트롤러"""
from flask_restx import Resource
from flask import request

from src.services.user_service import UserService
from src.utils.user_dto import UserDTO
from src.utils.user_respond import SigninSuccessful, \
    SignupSuccessful, AlreadyExistEmail, AlreadyExistNick, UserNotFound, ServerError

api = UserDTO.auth

@api.route('/signup')
class Signup(Resource):
    """회원가입 controller"""
    @staticmethod
    @api.expect(UserDTO.user_register_field)
    @api.doc(responses=SignupSuccessful.get_doc())
    @api.doc(responses=AlreadyExistEmail.get_doc())
    @api.doc(responses=AlreadyExistNick.get_doc())
    @api.doc(responses=ServerError.get_doc())
    def post():
        """post 요청, 회원가입"""
        email = request.json['email']
        nickname = request.json['nickname']
        password = request.json['password']

        user_service = UserService()
        signup = user_service.signup(email,nickname,password)

        return signup.get_respond()


@api.route('/signin')
class Signin(Resource):
    """로그인 controller"""
    @staticmethod
    @api.expect(UserDTO.user_login_field)
    @api.doc(responses=SigninSuccessful.get_doc())
    @api.doc(responses=UserNotFound.get_doc())
    @api.doc(responses=ServerError.get_doc())
    def post():
        """post 요청, 로그인"""
        email = request.json['email']
        password = request.json['password']

        user_service = UserService()
        signin = user_service.signin(email,password)

        return signin.get_respond()
