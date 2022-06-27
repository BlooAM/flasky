from datetime import datetime
from threading import Thread

from flask import render_template, session, redirect, url_for
from flask_mail import Message

from app.main import main
from app.main.forms.forms import NameForm
from app import db, mail
from app.models import User, Role


def send_async_email(app, msg):
    with app.app_context():
        mail.send()

def send_email(to, subject, template, **kwargs):
    msg = Message(
        main.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, 
        sender=main.config['FLASKY_MAIL_SENDER'], 
        recipients=[to]
        )
    msg.body = render_template(template, + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[main, msg])
    thr.start()
    return thr


@main.route('/', methods=['POST', 'GET'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    return render_template('index.html', form=form, name=session.get('name'), known=session.get('known', False))

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
