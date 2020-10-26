from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/erpmax_task'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost:3306/{DB_NAME}'


#db.session.commit()
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/location')
def location():
    return render_template('location.html')

if __name__ == "__main__":
    app.run(debug=True)
