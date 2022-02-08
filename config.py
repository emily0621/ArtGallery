class Config:

    SECRET_KEY = 'SECRET_KEY'

    SQLALCHEMY_DATABASE_URI = 'mysql://root:1234@localhost:3306/testdb'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False