from App import db

from datetime import datetime



class Location(db.Model):

    location_id = db.Column(db.Integer, primary_key=True)
    location_name = db.Column(db.String(20), unique=True, nullable=False)

    def __init__(self, location_name):
        #self.location_id = location_id
        self.location_name = location_name

class Product(db.Model):

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(20), unique=True, nullable=False)
    product_qty = db.Column(db.Integer, nullable=False)

    def __init__(self, product_name, product_qty):
        #self.product_id=product_id
        self.product_name=product_name
        self.product_qty=product_qty

class Movement(db.Model):
    move_id = db.Column(db.Integer, primary_key= True)
    ts = db.Column(db.DateTime, default=datetime.utcnow)
    frm = db.Column(db.String(20), nullable = False)
    to = db.Column(db.String(20), nullable = False)
    p_name = db.Column(db.String(20), nullable = False)
    p_qty = db.Column(db.Integer, nullable = False)

    def __init__(self, move_id, ts, frm, to, p_name, p_qty):
        self.move_id = move_id
        self.ts = ts
        self.frm = frm
        self.to = to
        self.p_name = p_name
        self.p_qty = p_qty


class Balance(db.Model):
    bid = db.Column(db.Integer, primary_key= True,nullable = False)
    product = db.Column(db.String(20), nullable = False)
    location = db.Column(db.String(20),nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"Balance('{self.bid}','{self.product}','{self.location}','{self.quantity}')"
