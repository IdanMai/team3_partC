import mysql.connector
from flask import Blueprint, render_template, request, redirect, jsonify, flash, url_for
from utilities.db.user import User


sign_up = Blueprint('sign_up', __name__,
                    static_folder='static',
                    static_url_path='/sign_up',
                    template_folder='templates')


@sign_up.route('/sign_up')
def main():
    return render_template('sign_up.html')


@sign_up.route('/log_in/<message>/<message_type>')
def log_in(message, message_type):
    if message:
        flash(message, message_type)
    return render_template('log_in.html')


@sign_up.route('/create_user', methods=['post'])
def create_user():
    password = request.form['password']
    verify = request.form['verifyPassword']
    email = request.form['email']

    user = User(request.form['email'], request.form['username'], request.form['birthdate'], request.form['password'])

    if password != verify:
        flash("Passwords Do Not Match", "warning")

    else:
        searched_user = user.search_user(email)
        if searched_user:
            flash("User Email already exists", "danger")

        else:
            user_added = user.add_user()
            return redirect(url_for('sign_up.log_in', message="User Created Successfully!", message_type="success"))

    return redirect('/sign_up')


@sign_up.route('/login_user')
def login_user():
    found_user = user.search_user()
    if found_user:
        if user.password == request.form['password']:
            return render_template('home.html', username=user.username)
        else:
            return render_template('log_in.html', message="wrong password")

    else:
        return render_template('log_in.html', message="wrong email")




# Creates an instance for the User class for export.
#user = User()
