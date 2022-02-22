from app import app
from flask import jsonify, request
from schemas import FullPostSchema, WithoutIdPostSchema
from models.post import Post


@app.route('/gallery', methods=['POST'])
def addPost():
    data = request.get_json(force=True)
    post = Post(
        title=data.get('title'),
        text=data.get('text'),
        category=data.get('category'),
        url=data.get('url'),
        author=data.get('author')
    )
    post.addPost()
    return "Success"


@app.route('/gallery', methods=['GET'])
def getAllPosts():
    posts = Post.getAllPosts()
    return jsonify(WithoutIdPostSchema(many=True).dump(posts))


@app.route('/gallery/<username>', methods=['GET'])
def getAllPostsByAuthor(username):
    posts = Post.getAllPostsByAuthor(username)
    return jsonify(WithoutIdPostSchema(many=True).dump(posts))
