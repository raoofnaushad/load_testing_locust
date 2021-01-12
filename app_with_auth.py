from flask import Flask, request
import jwt
from datetime import datetime, timedelta
from functools import wraps




app = Flask(__name__)

SECRET_KEY = "this_is_a_secret_key"
user_id = "raoof_123"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        response = {
            "success" : False,
            "authentication_status" : False 
        }
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            print("No token")
            return response, 401
        try:
            data = jwt.decode(token, SECRET_KEY)
            if data["user_id"] != user_id:
                print("User not identified")
                return response, 401
        except Exception as ex:
            print(str(ex))
            return response, 401
        return f(*args, **kwargs)
    return decorated

@app.route('/login', methods=['POST'])
def login():
    response = {
        "success" : False,
        "message" : "Invalid parameters",
        "token" : ""
    }
    auth = request.form
    if auth.get('email') == "raoof@trajectus.com" and auth.get("password") == "iamraoof":
        expiry = datetime.utcnow() + timedelta(minutes=50) 
        token = jwt.encode({
            'user_id': user_id,
            'exp': expiry
        }, SECRET_KEY)
        
        response["message"] = "token generated"
        response["token"] = token.decode('UTF-8')
        response["success"] = True
        return response, 200
    return response, 401


@app.route('/')
@token_required
def hello_world():
    return 'Hello, World!'

@app.route('/posting', methods=['POST'])
@token_required
def posting():
    response = {
        "message" : "ERROR",
        "success" : False
    }
    request_body = request.json
    if request_body["content"] == "2":
        response["message"] = "DHOOM!"
    else:
        response["message"] = "BHOOM!"
    response["success"] = True
    return response, 200



if __name__ == "__main__":
    app.run('0.0.0.0',port=5000)