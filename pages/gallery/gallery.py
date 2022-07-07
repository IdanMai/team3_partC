import mysql.connector
from flask import Blueprint, render_template, request, redirect, jsonify

gallery = Blueprint('gallery', __name__,
                     static_folder='static',
                     static_url_path='/gallery/static',
                     template_folder='templates')


@gallery.route('/gallery')
def main():
    return render_template('gallery.html')
