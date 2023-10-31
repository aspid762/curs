# curs

### Settings.py
ALLOWED_HOSTS = ['*']\
STATICFILES_DIRS = [BASE_DIR / 'static',]\
LANGUAGE_CODE = "ru-ru"\
TIME_ZONE = "Europe/Moscow"

### Commands
python manage.py news\
python manage.py migrate\
python manage.py createsuperuser


### SQLite
pip install sqlite-web\
sqlite_web --host 0.0.0.0 backend/db.sqlite3