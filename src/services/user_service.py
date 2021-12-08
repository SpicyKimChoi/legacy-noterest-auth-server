from app import db
from src.utils.user_respond import SigninSuccessful, SignupSuccessful, AlreadyExistEmail, AlreadyExistNick, UserNotFound, ServerError
from src.models.user_model import User

import bcrypt

class UserService(object):
    def __init__(self):
        self.conn = db.session

    def email_exist(self,email):
        email_exists = self.conn.query(User).\
            filter_by(email=email).all()
        
        return bool(email_exists)

    def nickname_exist(self,nickname):
        nickname_exists = self.conn.query(User).\
            filter_by(nickname=nickname).all()
        
        return bool(nickname_exists)

    def signup(self, email, nickname, password):
        if self.email_exist(email):
            return AlreadyExistEmail()
        elif self.nickname_exist(nickname):
            return AlreadyExistNick()
        else:
            encode_pwd = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode('utf-8')
            current_user = User(email=email, nickname=nickname,password=encode_pwd, img_url='')
            self.conn.add(current_user)
            self.conn.commit()

            get_user = self.conn.query(User).\
                filter_by(email=email).first()

            return SignupSuccessful(get_user.id,get_user.email,get_user.nickname,get_user.img_url)

    def signin(self, email, password):
        user = self.conn.query(User).\
            filter_by(email=email).first()

        if not user:
            return UserNotFound()
        elif bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return SigninSuccessful(user.id, user.email, user.nickname,user.img_url)
        else:
            return UserNotFound()
