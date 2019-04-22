#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from flask import Flask, request, render_template, \
    jsonify, redirect, url_for
from werkzeug.utils import secure_filename

# Support for gomix's 'front-end' and 'back-end' UI.
app = Flask(__name__, static_folder='public', template_folder='views')
app.config.from_object('_config')

# Set the app secret key from the secret environment variables.
app.secret = os.environ.get('SECRET')

# def connect_db():
#     return sqlite3.connect(app.config['DATABASE_PATH'])

@app.route('/')
def homepage():
    """Displays thot hormeparger."""
    return render_template('index.html')
    
@app.route('/api/fileanyse', methods=['POST'])
def fileanyse():
    """Simple API my hoes anddreas.
    """
    if "file" in request.files:
        file = request.files["file"]
    # print(file.filename)
    # print(file.content_type)
    # print(os.fstat(file.stream.fileno()).st_size)
        return jsonify({
            "name":	file.filename,
            "type":	file.content_type,
            "size":	os.fstat(file.stream.fileno()).st_size
        })  
    return jsonify({
        "error": "no file included"
    })
  
if __name__ == '__main__':
    app.run()