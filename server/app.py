#!/usr/bin/env python3

from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Customer, Item, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/')
def index():
    return '<h1>Customer Review API</h1>'


@app.route('/customers')
def customers():
    customers = Customer.query.all()
    return jsonify([customer.to_dict() for customer in customers])


@app.route('/customers/<int:id>')
def customer_by_id(id):
    customer = Customer.query.filter_by(id=id).first()
    if customer:
        return jsonify(customer.to_dict())
    return jsonify({'error': 'Customer not found'}), 404


@app.route('/items')
def items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])


@app.route('/items/<int:id>')
def item_by_id(id):
    item = Item.query.filter_by(id=id).first()
    if item:
        return jsonify(item.to_dict())
    return jsonify({'error': 'Item not found'}), 404


@app.route('/reviews')
def reviews():
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews])


@app.route('/reviews/<int:id>')
def review_by_id(id):
    review = Review.query.filter_by(id=id).first()
    if review:
        return jsonify(review.to_dict())
    return jsonify({'error': 'Review not found'}), 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)