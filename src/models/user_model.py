from app import db

class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(50))
    nickname = db.Column(db.String(20))
    password = db.Column(db.String(255))
    img_url = db.Column(db.String(255))
    
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())