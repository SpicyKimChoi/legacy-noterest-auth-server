class BaseRespond(object):
    status=200
    msg=""
    
    @classmethod
    def get_doc(cls):
        return {cls.status: cls.msg}

    @classmethod
    def get_respond(cls):
        return {"message":cls.msg}, cls.status


class SuccessAuthRespond(BaseRespond):    
    def __init__(self, userId, email, nickname, img_url):
        self.userId = userId
        self.email = email
        self.nickname = nickname
        self.img_url = img_url

        import jwt
        user_info = {
            "userId": userId,
            "email": email,
            "nickname": nickname,
            "img_url": img_url
        }
        self.jwt_token = jwt.encode(user_info, "secret", algorithm="HS256")

    def get_respond(self):
        return {"Authorization":self.jwt_token}, __class__.status


class SigninSuccessful(SuccessAuthRespond):
    status = 200
    msg = "로그인에 성공하였습니다."
        
    
class SignupSuccessful(SuccessAuthRespond):
    status = 201
    msg = "회원가입에 성공하였습니다."


class AlreadyExistEmail(BaseRespond):
    status = 409
    msg = "이미 존재하는 이메일입니다."


class AlreadyExistNick(BaseRespond):
    status = 400
    msg = "이미 존재하는 닉네임입니다."


class UserNotFound(BaseRespond):
    status = 404
    msg = "유저를 찾을 수 없습니다."


class ServerError(BaseRespond):
    status = 500
    msg = "서버에서 에러가 발생하였습니다."
    def __init__(self, error):
        self.error = error

    def get_respond(self):
        return {"message":self.msg, "error": self.error}, self.status