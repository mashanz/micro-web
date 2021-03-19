from flask import Flask, jsonify
from flask.globals import request, session
app = Flask(__name__)

# base response format
def base_response(status = 200, message = "OK", method = "GET", response=None):
    return jsonify({
        "method": method,
        "status": status,
        "message": message,
        "data": response
    })

# 404 Custom Handler
@app.errorhandler(404)
def page_not_found(error):
    return(base_response(status = 404, method = str(request.method), message=str(error)))

# 405 Custom Handler
@app.errorhandler(405)
def method_not_allowed(error):
    return(base_response(status = 405, method = str(request.method), message=str(error)))

# 500 Custom Handler
@app.errorhandler(500)
def page_not_found(error):
    return(base_response(status = 500, method = str(request.method), message=str(error)))

# Index API
@app.route('/')
def api_index():
    return(base_response(method = str(request.method)))

# Users API
@app.route('/user/', methods = ["GET", "POST"])
@app.route('/user/<int:id>', methods = ["GET", "POST", "PUT", "DELETE"])
def api_user(id = None):
    response = {
            "id": id
    }
    return(base_response(method = str(request.method), response = response))