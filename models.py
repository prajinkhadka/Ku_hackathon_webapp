from myproject import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
import hashlib

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    __tablename__ ='users'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(64), unique = True, index = True)
    username = db.Column(db.String(64), unique = True, index = True)
    refer_by=db.Column(db.String(64),unique=True)
    password_hash = db.Column(db.String(128))
    #resulting_hash = hashlib.md5(username.encode())

    def __init__(self,username,email,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash,password)
    
