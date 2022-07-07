import mysql.connector
from flask import Blueprint, render_template, request, redirect, jsonify

sign_up = Blueprint('sign_up', __name__,
                    static_folder='static',
                    static_url_path='/sign_up',
                    template_folder='templates')


@sign_up.route('/sign_up')
def main():
    return render_template('sign_up.html')


@sign_up.route('/log_in')
def log_in():
    return render_template('log_in.html')
