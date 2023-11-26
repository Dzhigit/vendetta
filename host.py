from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from src.data.config import smtp_user, smtp_password

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import random
import sqlite3
import logging

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser(bundle_errors=True)
sqlite_con = sqlite3.connect(
    database='vendetta.db',
    check_same_thread=False
)
sqlite_cur = sqlite_con.cursor()
yandex_smtp = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
yandex_smtp.login(smtp_user, smtp_password)
logging.basicConfig(
    level=logging.DEBUG
)
logger = logging.getLogger('server')


def send_code(_from, to, subject, attach):
    msg = MIMEMultipart()
    msg['From'] = _from
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(attach, 'plain'))

    try:
        logger.debug(f'Send code wia email {to}')
        yandex_smtp.sendmail(_from, to, msg.as_string())
        logger.debug(f'Code already send on email {to}')
        return 1
    except Exception as exc:
        logger.error(f'Error to send code on email {to} \n {exc}')
        return 0


class VerificationHandler(Resource):
    def get(self, email):
        code = ''.join([str(random.randint(0, 9)) for i in range(6)])

        if send_code(
            smtp_user,
            email,
            'Verification code on VTQ',
            f'Your verification code: {code}'
        ):
            logger.debug(f'Create {email} and {code} temp data')
            sqlite_cur.execute(f"""INSERT INTO verification (email, code) VALUES ('{email}', {code});""")
            sqlite_con.commit()

            return {'DONE': 'Code already send'}
        else:
            return {'EMAIL_ERROR': 'Please enter real email'}


class RegistrationHandler(Resource):
    def get(self):
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        re_password = request.form['re_password']
        code = request.form['code']

        if password == re_password:
            result = sqlite_cur.execute(f"""SELECT * FROM verification WHERE email={email};""")
            verify_code = result.fetchone()[1]

            if code == verify_code:
                logger.debug(f'Delete {email} and {code} in temp verification')
                sqlite_cur.execute(f"""DELETE FROM verification WHERE email={email};""")
                sqlite_con.commit()

                logger.debug(f'Add new user in db')
                sqlite_cur.execute(
                    f"""INSERT INTO users (username, email, password) VALUES ({username}, {email}, {password});"""
                )
                sqlite_con.commit()

                return {'DONE': 'Registration successful'}

            else:
                logger.debug(f'User {username} code not required')
                return {'CODE_ERROR': 'Pleas retry your code'}
        else:
            logger.debug(f'Incorrect password user {username}')
            sqlite_cur.execute(f"""DELETE FROM verification WHERE email={email};""")
            sqlite_con.commit()

            return {'PASSWORD_ERROR': 'Please check your password'}


api.add_resource(VerificationHandler, '/verification/<string:email>')
api.add_resource(RegistrationHandler, '/registration')

if __name__ == '__main__':
    app.run(debug=True)
