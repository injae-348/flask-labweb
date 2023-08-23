# 서버 환경
from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

# 시크릿 키
# python -c "import os; print(os.urandom(16))" -> 으로 발급 받음
SECRET_KEY = b'\xad|F6*ib%Y\xbf\xa4\x10s=\x85\x08'