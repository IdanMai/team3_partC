import mysql.connector
from flask import Blueprint, render_template, request, redirect, jsonify

orders = Blueprint('orders', __name__,
                       static_folder='static',
                       static_url_path='/orders',
                       template_folder='templates')


@orders.route('/Order_qestions')
def main():
    return render_template('Order_qestions.html')

@orders.route('/order')
def order():
    return render_template('order.html')

@orders.route('/OrderConfirmation')
def OrderConfirmation():
    return render_template('OrderConfirmation.html')
