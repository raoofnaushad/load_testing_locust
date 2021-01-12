from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/posting', methods=['POST'])
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
    
    
    
    