"""
API 응답 클래스
"""
import jwt

class BaseRespond:
    """
    기본이되는 응답 클래스
    """
    status=200
    msg=""

    @classmethod
    def get_doc(cls):
        """
        응답에 대한 status와 메시지를 dic형태로 반환
        """
        return {cls.status: cls.msg}

    @classmethod
    def get_respond(cls):
        """
        응답 반환
        """
        return {"message":cls.msg}, cls.status


class SuccessAuthRespond(BaseRespond):
    """
    인증 성공시 응답
    """
    def __init__(self, user_id, email, nickname, img_url):
        self.user_id = user_id
        self.email = email
        self.nickname = nickname
        self.img_url = img_url

        user_info = {
            "user_id": user_id,
            "email": email,
            "nickname": nickname,
            "img_url": img_url
        }
        self.jwt_token = jwt.encode(user_info, "secret", algorithm="HS256")

    def get_respond(self):
        return {"Authorization":self.jwt_token}, __class__.status


class SigninSuccessful(SuccessAuthRespond):
    """로그인 성공에 대한 응답"""
    status = 200
    msg = "로그인에 성공하였습니다."


class SignupSuccessful(SuccessAuthRespond):
    """회원가입 성공에 대한 응답"""
    status = 201
    msg = "회원가입에 성공하였습니다."


class AlreadyExistEmail(BaseRespond):
    """이미 존재하는 이메일에 대한 응답"""
    status = 409
    msg = "이미 존재하는 이메일입니다."


class AlreadyExistNick(BaseRespond):
    """이미 존재하는 닉네임에 대한 응답"""
    status = 400
    msg = "이미 존재하는 닉네임입니다."


class UserNotFound(BaseRespond):
    """존재하지 않는 유저 로그인에 대한 응답"""
    status = 404
    msg = "유저를 찾을 수 없습니다."


class ServerError(BaseRespond):
    """서버에서 에러가 발생한 경우"""
    status = 500
    msg = "서버에서 에러가 발생하였습니다."
    def __init__(self, error):
        self.error = error

    def get_respond(self):
        return {"message":self.msg, "error": self.error}, self.status
