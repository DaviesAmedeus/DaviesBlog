import os
class Config:
    # A secret key protects against modifying cookies and cross site forgery requests.
    SECRET_KEY = "3b8f3841c7f869ab5081ec65504c9298"
    SQLALCHEMY_DATABASE_URI="sqlite:///site.db"
    # print(os.environ.get('SQLALCHEMY_DATABASE_URI'))

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
