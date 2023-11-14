from django.db import models

# Create your models here.

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
    img_id = models.ImageField(upload_to='images/') #models.TextField(blank=True, null=True)

    def __str__(self):
        return f'ID: {self.id} | Заголовок: {self.title}| Юрл: {self.url} | Дата публикации: {self.published_at} |'

    class Meta:
        managed = False
        db_table = 'news'