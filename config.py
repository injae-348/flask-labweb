import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
# Secret key로 dev와 같이 유추하기 쉬운 문자열을 사용하면 안된다
# 개발환경이므로 이렇게 사용
SECRET_KEY="dev"