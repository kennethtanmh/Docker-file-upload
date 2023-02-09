from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename
import os
import subprocess

app = Flask(__name__)
api = Api(app)

# uploads_dir = "/home/coga/Desktop/pass/backend/uploads"
uploads_dir = "/app/data"

class FileUpload(Resource):
    def post(self):
        files1 = request.files.getlist("files1")
        files2 = request.files.getlist("files2")
        filenames = []
        for file in files1:
            file1_name = secure_filename(file.filename)
            file.save(os.path.join(uploads_dir, file1_name))
            filenames.append(file.filename)
        for file in files2:
            file2_name = secure_filename(file.filename)
            file.save(os.path.join(uploads_dir, file2_name))  
            filenames.append(file.filename)
        # file1 = files1[0].filename
        # file2 = files2[0].filename
        
        result1 = subprocess.run(["cksum", os.path.join(uploads_dir, file1_name)], capture_output=True).stdout.decode().split()[0]
        result2 = subprocess.run(["cksum", os.path.join(uploads_dir, file2_name)], capture_output=True).stdout.decode().split()[0]
         
        response = {'file1_name': file1_name, 'file2_name': file2_name, 'file1_result': result1, 'file2_result': result2}
        return jsonify(response)

api.add_resource(FileUpload, '/api/upload')


if __name__ == '__main__':
    app.run(debug=True, port=5000)


