"""
DB 접근 계층, ORM 사용
"""
import bcrypt

from app import db
from src.utils.user_respond import SigninSuccessful, \
    SignupSuccessful, AlreadyExistEmail, AlreadyExistNick, UserNotFound
from src.models.user_model import User



class UserService:
    """user 인증과 관련된 클래스"""
    def __init__(self):
        self.conn = db.session

    def email_exist(self,email):
        """이메일이 존재하는지 확인"""
        email_exists = self.conn.query(User).\
            filter_by(email=email).all()

        return bool(email_exists)

    def nickname_exist(self,nickname):
        """닉네임이 존재하는지 확인"""
        nickname_exists = self.conn.query(User).\
            filter_by(nickname=nickname).all()

        return bool(nickname_exists)

    def signup(self, email, nickname, password):
        """회원가입 진행"""
        if self.email_exist(email):
            return AlreadyExistEmail()
        if self.nickname_exist(nickname):
            return AlreadyExistNick()

        encode_pwd = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode('utf-8')
        current_user = User(email=email, nickname=nickname,password=encode_pwd, img_url='')
        self.conn.add(current_user)
        self.conn.commit()

        get_user = self.conn.query(User).\
            filter_by(email=email).first()

        return SignupSuccessful(get_user.id,get_user.email,get_user.nickname,get_user.img_url)

    def signin(self, email, password):
        """로그인 진행"""
        user = self.conn.query(User).\
            filter_by(email=email).first()

        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return SigninSuccessful(user.id, user.email, user.nickname,user.img_url)

        return UserNotFound()
