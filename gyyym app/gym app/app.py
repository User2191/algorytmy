import register
from flask import Flask, render_template, jsonify, request, json, redirect, url_for
from flask_pymongo import PyMongo
from datetime import datetime, timedelta
from flask_bs4 import Bootstrap
from flask_wtf import FlaskForm
import secrets
import mysql.connector
from html_json_forms import parse_json_form
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired
import json
import bcrypt

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)

mydb = mysql.connector.connect(
    host="sql84.lh.pl",
    user="serwer158348_kmadzia",
    password="7C*qZ-1WAuduA_2*",
    database="serwer158348_kmadzia"
)

# formularze logowania i rejestracji
class LoginForm(FlaskForm):
    """
    formularz logowania uzytkowników
    """
    user_name = StringField('Nazwa użytkownika', validators=[DataRequired()])
    user_password = PasswordField('Hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj')


class RegistrationForm(FlaskForm):
    """
    formularz rejestracji
    """
    user_name = StringField('Nazwa użytkownika', validators=[DataRequired()])
    user_password = PasswordField('Hasło', validators=[DataRequired()])
    user_password_repeat = PasswordField('Powtórz hasło', validators=[DataRequired()])
    user_first_name = StringField('Imię', validators=[DataRequired()])
    user_last_name = StringField('Nazwisko', validators=[DataRequired()])
    user_email = EmailField('Email', validators=[DataRequired()])
    submit = SubmitField('Rejestruj')

# funkcje do logowania, wylogowania, rejestracji użytkowników
# strona główna
@app.route('/')
def login():
    login_form = LoginForm()
    return render_template('login.html', login_form=login_form)
    user_password = login.form['user_password']
    user_name = login.form['user_name']
    mycursor.callproc('sp_checkUser',(user_name,user_password))

"""
@app.route('/register')
def register():
    register_form = RegistrationForm()
    return render_template('register.html', title='Rejestracja', register_form=register_form)
    user_password = request.form['user_password']
    user_email = request.form['user_email']
    user_name = request.form['user_name']
    mycursor.callproc('sp_createUser',(user_name,user_email,user_password))
"""

@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegistrationForm()

    if request.method == 'POST':
        user_name = request.form['user_name']
        user_password = request.form['user_password']  # Remember to hash the password
        user_email = request.form['user_email']

        # Hash the password
        hashed_password = bcrypt.hashpw(user_password.encode('utf-8'), bcrypt.gensalt())

        # Connecting to the database
        with mydb.cursor() as mycursor:
            sql = "INSERT INTO users (user_name, user_password, user_email) VALUES (%s, %s, %s)"
            mycursor.execute(sql, (user_name, hashed_password, user_email))
            mydb.commit()
            return redirect(url_for('clock'))
    return render_template('register.html', title='Rejestracja', register_form=register_form)


@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Pobieranie danych z formularza
        data = [(i, int(request.form[f'number{i}'])) for i in range(1, 11)]

        # Zapis danych do bazy
        with mydb.cursor() as mycursor:
            mycursor.executemany('INSERT INTO prs (exercise, weight) VALUES (?, ?)', data)
            mydb.commit()
            mydb.close()

        return "saved"
    except Exception as e:
        return f"error: {e}"

# główna część aplikacji

@app.route('/clock')
def clock():
    return render_template('clock.html', title='Home')


@app.route('/progress')
def progress():
    return render_template('progress.html', title='progress')


@app.route('/exercises')
def exercises():
    return render_template('exercises.html', title='exercises')


@app.route('/calendar')
def calendar():
    return render_template('calendar.html', title='calendar')


@app.route('/person')
def person():
    return render_template('person.html', title='person')


if __name__ == '__main__':
    app.run(debug=True)
