# curs
База практически недоступна, потому что конвертировать из Postgresql в SQLite очень нетривиальная задача, \
а разрабатывать я начал сразу в Postgresql. Потому, что разрабатываю на удаленном сервере. \
Короче все что можно посмотреть, это статику. Ну и сами новости в fixtures лежат выгруженные. \
Через fixtures перекачать данные тоже с ходу не получилось. \
Надо сериализатор дорабатывать. \
ОС: RedOS 7.3 \
Python: 3.8.2 \
requirements.txt - есть 

404 страницы нет - не ищите :)

З.Ы. Себе для примера закачал рельные новости cnbc news (янки https://www.cnbc.com/world/?region=world) 
Модель: 
```
class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    published_at = models.DateField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    header_image = models.TextField(blank=True, null=True)
    raw_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    scraped_at = models.DateField(blank=True, null=True)
    img_id = models.ImageField(upload_to='images/')
```
Строка подключения к Postgresql:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'curs',
        'USER': 'curs',
        'PASSWORD': 'curs',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```
### Settings.py
ALLOWED_HOSTS = ['*']\
STATICFILES_DIRS = [BASE_DIR / 'static',]\
LANGUAGE_CODE = "ru-ru"\
TIME_ZONE = "Europe/Moscow"

### Commands
python manage.py news\
python manage.py migrate\
python manage.py createsuperuser


### SQLite - убогая дичь :)
pip install sqlite-web\
sqlite_web --host 0.0.0.0 backend/db.sqlite3