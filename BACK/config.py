import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkey'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:1234@localhost:3306/universe'
    SQLALCHEMY_TRACK_MODIFICATIONS = False