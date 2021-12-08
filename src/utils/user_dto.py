from flask_restx import Namespace, fields

class UserDTO(object):
    auth = Namespace(
        name="Auth",
        description="유저 인증을 진행하는 API"
    )

    user_register_field = auth.model('user_register_field', {  
        'email': fields.String(description='유저의 Email', required=True, example="example@service.com"),
        'nickname': fields.String(description='유저의 nickname', required=True, example="examplenick"),
        'password': fields.String(description='유저의 Password', required=True, example="password123")
    })

    user_login_field = auth.model('user_login_field', {  
        'email': fields.String(description='유저의 Email', required=True, example="example@service.com"),
        'password': fields.String(description='유저의 Password', required=True, example="password123")
    })

    user_field = auth.model('user_field', {  
        'id': fields.String(description='유저의 고유 id', required=True, example="12"),
        'email': fields.String(description='유저의 Email', required=True, example="example@service.com"),
        'nickname': fields.String(description='유저의 nickname', required=True, example="examplenick"),
        'password': fields.String(description='유저의 Password', required=True, example="password123"),
        'img_url': fields.String(description='유저의 프로필 사진 링크', required=True, example="https:s3123.com")
    })