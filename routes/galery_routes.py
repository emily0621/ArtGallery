from app import app
from flask import jsonify
from schemas import FullPostSchema

import models


@app.route('/gallery', methods=['GET'])
def getAllPosts():
    posts = models.Post.getAllPosts()
    return jsonify(FullPostSchema(many=True).dump(posts))

