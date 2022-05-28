import jwt
from functools import wraps
from flask import Blueprint, request, make_response, current_app
from datetime import datetime, timedelta


bp = Blueprint('security', __name__)

def check(username, password):
    if username == "hi" and password == "bruh":
        return True
@bp.route('/login',methods=(['POST']))
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    error = None


    if not check(username, password):
        error = 'Incorrect user or password'

    if error is None:
        payload = {
            'iat': datetime.utcnow(),                          # Current time
            'exp': datetime.utcnow() + timedelta(minutes=10),  # Expiration time
            'sub': "test",
            'rol': "user"
        }
        resp = make_response("", 200)
        resp.set_cookie('access_token', value = jwt.encode(payload, current_app.config['SECRET_KEY'],
                                                   algorithm='HS256'), httponly = True, secure=True)
        return resp

    return make_response(error, 401)


def token_required(rol):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.cookies.get('access_token')
            

            if not token:
                return make_response('Invalid credentials', 401)
            
            try:
                data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms='HS256')
                print(data)
            except Exception as e:
                return make_response(e, 'Invalid credentials', 401)
            
            if rol != data['rol']:
                return make_response('Invalid role', 403)

            return f(*args, **kwargs)
        return decorated

    return decorator