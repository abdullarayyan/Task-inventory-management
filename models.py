from app import db

class User(db.Model):
 __tablename__='stusents'
 #colums
 id=db.Column(db.Integer,primary_key=True,autoincrement=True)
 name=db.Column('username',db.String(50),unique=True,nullable=False)
