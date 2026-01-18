#!/usr/bin/env python3

from app import app
from models import db, Customer, Item, Review

with app.app_context():
    print("Deleting existing data...")
    Review.query.delete()
    Customer.query.delete()
    Item.query.delete()

    print("Creating customers...")
    customer1 = Customer(name="Tal Yuri")
    customer2 = Customer(name="Raha Rossi")
    customer3 = Customer(name="Levi Schwartz")

    db.session.add_all([customer1, customer2, customer3])
    db.session.commit()

    print("Creating items...")
    item1 = Item(name="Laptop Backpack", price=49.99)
    item2 = Item(name="Insulated Coffee Mug", price=9.99)
    item3 = Item(name="Wireless Mouse", price=24.99)
    item4 = Item(name="USB-C Cable", price=12.99)

    db.session.add_all([item1, item2, item3, item4])
    db.session.commit()

    print("Creating reviews...")
    review1 = Review(comment="Great backpack! Fits my laptop perfectly.", customer_id=customer1.id, item_id=item1.id)
    review2 = Review(comment="Keeps my coffee hot for hours.", customer_id=customer1.id, item_id=item2.id)
    review3 = Review(comment="Very comfortable mouse, highly recommend.", customer_id=customer2.id, item_id=item3.id)
    review4 = Review(comment="Good quality cable, charges fast.", customer_id=customer2.id, item_id=item4.id)
    review5 = Review(comment="Nice backpack but a bit pricey.", customer_id=customer3.id, item_id=item1.id)
    review6 = Review(comment="The mouse is okay, nothing special.", customer_id=customer3.id, item_id=item3.id)

    db.session.add_all([review1, review2, review3, review4, review5, review6])
    db.session.commit()

    print("Seeding complete!")