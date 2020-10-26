
from App import db
class Product(db.Model):
 __tablename__='Product'
 #colums
 product_id = db.Column(db.Integer,primary_key=True)
 product_name = db.Column(db.String(20), nullable = False)
 #product_name = db.Column(db.String(20),uniaqe=True,nullable=False)
 product_qty = db.Column(db.Integer,nullable=False)

 def __init__(self,product_name,product_qty):
     self.product_name=product_name
     self.product_qty=product_qty




#Product (product_id)
#Location (location_id)
#
#
# class Product(db.Model):
#     prod_id = db.Column(db.Integer, primary_key= True)
#     prod_name = db.Column(db.String(20), nullable = False)
#     prod_name = db.Column(db.String(20),unique = True ,nullable = False)
#     prod_qty = db.Column(db.Integer, nullable = False)
#     def __repr__(self):
#         return f"Product('{self.prod_id}','{self.prod_name}','{self.prod_qty}')"#
#ProductMovement (movement_id, timestamp, from_location, to_location, product_id, qty)