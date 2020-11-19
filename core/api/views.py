from . import api
from flask import request
from models import User
from core import bcrypt, db
from sqlalchemy.exc import IntegrityError


@api.route('/')
def index():
    return "<h1>Hello World!</h1>"


@api.route('/register', methods=['POST'])
def register():
    data = request.get_json(force=True)
    user = User()
    for i in data:
        if i == 'password':
            p = bcrypt.generate_password_hash(
                data[i]
            )
            p = str(p, 'utf-8')
            print(p)
            user.password = p
        setattr(user, i, data[i])
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return {
            "status": "Error",
            "message": "User with email already exists"
        }, 403
    resp, status_code = {
        "message": "Signup Complete",
        "status": "Success"
    }, 201
    return resp, status_code
