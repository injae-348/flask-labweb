import os
from werkzeug.utils import secure_filename
from flask import current_app
def save_image(file,folder):
    if file:
        # 파일 저장 경로 설정
        # upload_dir = os.path.join(os.path.dirname(__file__), 'static/img/portfolio')
        # upload_dir = 'pybo/static/img/portfolio'
        upload_dir = os.path.join(current_app.root_path,'static/uploads',folder)
        os.makedirs(upload_dir, exist_ok=True)
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_dir, filename)
        # 파일 저장
        file.save(file_path)
        # file_path = filename

        return filename
    

def delete_image(folder, image_path):
    # 이미지 파일의 전체 경로
    if folder and image_path:
        file_path = os.path.join(current_app.root_path, 'static/uploads', folder, image_path)
    else:
        file_path=""
    if os.path.exists(file_path):
        os.remove(file_path)
