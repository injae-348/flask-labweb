import os
from werkzeug.utils import secure_filename

def save_image(file):
    if file:
        # 파일 저장 경로 설정
        # upload_dir = os.path.join(os.path.dirname(__file__), 'static/img/portfolio')
        upload_dir = 'pybo/static/img/portfolio'
        os.makedirs(upload_dir, exist_ok=True)
        filename = secure_filename(file.filename)
        file_path = os.path.join(upload_dir, filename)
        # 파일 저장
        file.save(file_path)
        file_path = file_path[5:]

        return file_path