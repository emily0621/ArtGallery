from app import app

import models
from flask import jsonify, request
from schemas import FullPostSchema, WithoutIdPostSchema


@app.route('/gallery', methods=['POST'])
def addPost():
    data = request.get_json(force=True)
    post = models.Post.addPost(data.get('title'),
                               data.get('text'),
                               data.get('category'),
                               data.get('url'),
                               data.get('author'))
    if type(post) == str:
        return jsonify(post)
    return jsonify(FullPostSchema().dump(post))


@app.route('/gallery/<id_post>', methods=['PUT'])
def editPost(id_post):
    post = models.Post.getPostById(id_post)
    if not post:
        return 'Invalid link'
    data = request.get_json(force=True)
    if data.get('title'):
        if not post.setTitle(data.get('title')):
            return 'Long title'
    if data.get('text'):
        if not post.setText(data.get('text')):
            return 'Long text'
    if data.get('category'):
        if not post.setCategory(data.get('category')):
            return 'Category doesn`t exists'
    models.Post.commit()
    return jsonify(FullPostSchema().dump(post))


@app.route('/gallery/<id_post>', methods=['DELETE'])
def deletePostById(id_post):
    ans = models.Post.deletePostById(id_post)
    if not ans:
        return jsonify("Invalid link")
    return jsonify("Post was deleted")


@app.route('/gallery', methods=['GET'])
def getAllPosts():
    posts = models.Post.getAllPosts()
    return jsonify(WithoutIdPostSchema(many=True).dump(posts))


@app.route('/gallery/<username>', methods=['GET'])
def getAllPostsByAuthor(username):
    if not models.Author.getAuthorByUsername(username):
        return jsonify('Author doesn`t exists')
    posts = models.Post.getAllPostsByAuthor(username)
    return jsonify(WithoutIdPostSchema(many=True).dump(posts))


@app.route('/gallery/post/<id_post>', methods=['GET'])
def getPostById(id_post):
    post = models.Post.getPostById(id_post)
    if not post:
        return jsonify('Invalid link')
    return jsonify(WithoutIdPostSchema().dump(post))
