import os

from flask import Flask, jsonify, request, send_from_directory, abort

from utils import *

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# @app.route('/predict', methods=['POST'])
# def predict():
#     return jsonify({'class_id': 'IMAGE_NET_XXX', 'class_name': 'Cat'})


UPLOAD_FOLDER = './uploads'
MIA_IMAGE_FOLDER='./mia_image'
# 初始化时创建上传目录
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
# 初始化时创建反转图像保存目录,存在则清空（先不清空看看效果）
if not os.path.exists(MIA_IMAGE_FOLDER):
    os.makedirs(MIA_IMAGE_FOLDER)
# else:
#     clear_folder(MIA_IMAGE_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MIA_IMAGE_FOLDER'] = MIA_IMAGE_FOLDER

# 上传文件
@app.route('/api/upload', methods=['POST'])
def upload_file():
    # 检查请求中是否包含文件
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    file = request.files['file']
    # 如果用户没有选择文件
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400
    # 检查文件是否合法
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify({"message": f"File {filename} uploaded successfully"}), 200
    else:
        return jsonify({"error": "Invalid file type"}), 400

#返回生成的图像
@app.route('/result/<filename>', methods=['GET'])
def get_file(filename):
    try:
        return send_from_directory(app.config['MIA_IMAGE_FOLDER'], filename)
    except FileNotFoundError:
        abort(404, description="File not found")



if __name__ == '__main__':
    app.run()
