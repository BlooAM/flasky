from flask import render_template

from app.auth import auth
from app.auth.forms import LoginForm

@auth.route('/login')
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)
