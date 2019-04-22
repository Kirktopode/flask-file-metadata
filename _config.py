import os

basedir = os.path.abspath(os.path.dirname(__file__))

# DATABASE = 'exercise_logs.db'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'just something random'
UPLOADS = 'uploads'

UPLOAD_PATH = os.path.join(basedir, UPLOADS)
# DATABASE_PATH = os.path.join(basedir, DATABASE)