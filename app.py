from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from S3_Utils.bucket import FileObj
import os


os.putenv('LANG','en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app=Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/upload",methods=['POST','GET'])
def upload():
    file=request.files['file']
    fileName=secure_filename(file.filename)    
    file.save(fileName)
    print(fileName)
    user_id='Swapnadeep'
    fileUploader=FileObj(user_id=user_id,filename=fileName)
    file_url=fileUploader.upload()
    JSON_Obj=jsonify({'user_id':user_id,
                      'file_key':str(user_id)+'/'+fileName,
                      'file_url':file_url})
    os.remove('./'+fileName)

    return JSON_Obj



if __name__=="__main__":
    app.run()

