from flask import Flask, request
from flask_restful import Resource, Api
import os
import hashlib

app = Flask(__name__)
api = Api(app)

def hashfile(file):
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

class FileUpload(Resource):
    def post(self):
        files1 = request.files.getlist("files1")
        files2 = request.files.getlist("files2")
        filenames = []
        for file in files1:
            file.save(os.path.join("/home/coga/Desktop/pass/backend/uploads", file.filename))
            filenames.append(file.filename)
        for file in files2:
            file.save(os.path.join("/home/coga/Desktop/pass/backend/uploads", file.filename))   
            filenames.append(file.filename)
        file1 = files1[0].filename
        file2 = files2[0].filename

        f1_hash = hashfile(os.path.join("/home/coga/Desktop/pass/backend/uploads", file1))
        f2_hash = hashfile(os.path.join("/home/coga/Desktop/pass/backend/uploads", file2))

        if f1_hash == f2_hash:
            print('The files are identical.')
        else:
            print('The files are different.')

        return 

api.add_resource(FileUpload, '/api/upload')


if __name__ == '__main__':
    app.run(debug=True, port=5000)
