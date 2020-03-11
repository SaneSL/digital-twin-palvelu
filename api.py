from flask import Flask, jsonify
from app import app

@app.route('/', methods=['GET'])
def get():
    return jsonify({'msg': 'Moro'})