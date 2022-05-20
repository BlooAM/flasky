import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    app.config['SECRET_KEY'] = 'HardToGuessSecretKey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') #TODO: set mail user in MAIL_USER environ var
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD') #TODO: set mail password in MAIL_PASWORD environ var
    app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
    app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <flasky@example.com>'
    app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN') #TODO: set flasky admin name in FLASKY_ADMIN environ var