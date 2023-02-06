from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import os
import subprocess

app = Flask(__name__)
api = Api(app)

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
        
        resultI = subprocess.run(["cksum", "/home/coga/Desktop/pass/backend/uploads/" + file1], capture_output=True)
        resultII = subprocess.run(["cksum", "/home/coga/Desktop/pass/backend/uploads/" + file2], capture_output=True)
        
        result1 = resultI.stdout.decode().split()[0]
        result2 = resultII.stdout.decode().split()[0]

        print(result1)
        print(result2)
        
        if result1 == result2:
            print('The files are identical.')
        else:
            print('The files are different.')

        response = {'file1_name': file1, 'file2_name': file2, 'file1_result': result1, 'file2_result': result2}
        return jsonify(response)


api.add_resource(FileUpload, '/api/upload')


if __name__ == '__main__':
    app.run(debug=True, port=5000)


