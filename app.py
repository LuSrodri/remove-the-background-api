import os
import uuid
from flask import Flask, flash, jsonify, make_response, request, redirect, url_for, send_file
from flask_cors import cross_origin
from werkzeug.utils import secure_filename
from Services.RemoveService import remove_background

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
@app.route("/ping", methods=['GET'])
@cross_origin()
def ping():
    return '<h1>pong</h1>'

@app.route("/removeback", methods=['POST'])
@cross_origin()
def upload_file():
    if 'file' not in request.files:
        response = make_response(jsonify({'error': 'No file part'}), 400)
        return response
    
    file = request.files['file']
    if file.filename == '':
        response = make_response(jsonify({'error': 'No selected file'}), 400)
        return response
    
    if file and allowed_file(file.filename):
        filename = secure_filename(str(uuid.uuid4()) + '.png')
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        image_without_background_path = remove_background(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return send_file(image_without_background_path)
    
    else:
        response = make_response(jsonify({'error': 'File not allowed'}), 400)
        return response
        
        
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))