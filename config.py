class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:password@devlog-postgresql/noterest'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = ''
