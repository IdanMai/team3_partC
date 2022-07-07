import mysql.connector
from flask import Blueprint, render_template, request, redirect, jsonify
from datetime import datetime


my_account = Blueprint('my_account', __name__,
                       static_folder='static',
                       static_url_path='/my_account',
                       template_folder='templates')


@my_account.route('/my_account')
def main():
    datetimeObject = datetime(1993,6,26)
    today = datetime.now()
    delta1 = datetime(today.year, datetimeObject.month, datetimeObject.day)
    delta2 = datetime(today.year+1, datetimeObject.month, datetimeObject.day)
    days = ((delta1 if delta1 > today else delta2) - today).days
    email = "needToTakeFromPage"

    return render_template('my_account.html',days=days)
