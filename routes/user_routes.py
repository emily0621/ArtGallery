from app import app
from flask import jsonify


@app.route('/test_route', methods=['GET'])
def testMethod():
    return jsonify("test_route")