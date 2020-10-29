
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/erpmax_task'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost:3306/{DB_NAME}'

db = SQLAlchemy(app)




@app.route('/')
def index():

    from models import Balance
    all_data = Balance.query.all()

    return render_template("index.html",balance=all_data)

@app.route('/move')
def move():
    from models import Movement

    all_data = Movement.query.all()
    return render_template("move.html",Movement=all_data)


@app.route('/product')
def product():
    from models import Product

    all_data = Product.query.all()
    return render_template("product.html", Product = all_data)


@app.route('/location')
def location():
    from models import Location

    all_data = Location.query.all()
    return render_template("location.html", location = all_data)


@app.route('/insertproduct', methods = ['POST'])
def insertpro():
    if request.method == 'POST':

        product_name = request.form['product_name']
        product_qty = request.form['quantity']
        from models import Product

        my_data = Product(product_name, product_qty)
        db.session.add(my_data)
        db.session.commit()
        flash("Add Product Successfully")

        return redirect(url_for('product'))

@app.route('/insertlocation', methods = ['POST'])
def insertloc():
    if request.method == 'POST':

        location_name = request.form['location_name']
        from models import Location

        my_data = Location(location_name)
        db.session.add(my_data)
        db.session.commit()
        flash("Add Location Successfully")

        return redirect(url_for('location'))

@app.route('/update/', methods = ['GET', 'POST'])
def update():

    if request.method == 'POST':
        from models import Product

        my_data = Product.query.get(request.form.get('id'))
        my_data.product_name = request.form['product_name']
        my_data.product_qty = request.form['quantity']
        try:
            db.session.commit()
            flash("Product Updated Successfully")
        except:
            flash("Nothivg ")


        return redirect(url_for('product'))

@app.route('/delete/<product_id>/', methods = ['GET', 'POST'])
def delete(product_id):
    from models import Product

    my_data = Product.query.get(product_id)

    try:
        db.session.delete(my_data)
        db.session.commit()
        flash("ddd Deleted Successfully")
    except:
        flash("nooo Updated Successfully")

    return redirect(url_for('product'))


@app.route('/updateloc/', methods = ['GET', 'POST'])
def updateloc():

    if request.method == 'POST':
        from models import Location

        my_data = Location.query.get(request.form.get('id'))

        my_data.location_name = request.form['location_name']
        try:
            db.session.commit()
            flash("nn Updated Successfully")
        except:
            flash("nooo Updated Successfully")


        return redirect(url_for('location'))


@app.route('/delete/<location_id>/', methods = ['GET', 'POST'])
def deleteloc(location_id):
    from models import Location

    my_data = Location.query.get(location_id)

    try:
        db.session.delete(my_data)
        db.session.commit()
        flash("Location Deleted Successfully")
    except:
        flash("Location Deleted Unsuccessfully")

    return redirect(url_for('location'))



