"""
user-auth
"""

from flask import Flask
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    """
    flask 실행 구문, restx, migration 연결
    """
    flask_app = Flask(__name__)
    CORS(flask_app)

    if flask_app.config["ENV"] == 'production':
        flask_app.config.from_object('config.ProductionConfig')
    else:
        flask_app.config.from_object('config.DevelopmentConfig')

    if config is not None:
        flask_app.config.update(config)

    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    api = Api(
        app=flask_app,
        version='0.1',
        title="User Authentication Service",
        description="유저의 인증(로그인, 회원가입)을 진행하는 서버입니다.",
        terms_url="/",
        contact="wonjundero@gmail.com",
        license="MIT"
    )

    from src.controllers.auth import api as auth_ns
    api.add_namespace(auth_ns, '/auth')

    return flask_app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
