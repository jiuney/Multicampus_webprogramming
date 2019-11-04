from django.db import models

def articles_image_path(instance, filename):
    # return f'articles/{instance.pk}번글/images/{filename}'
    # /media/articles/2번글/images/baby.jpg
    return 'articles/%Y/%m/%d/'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.FileField(blank=True, upload_to='articles/%Y/%m/%d') # ImageField는 pillow 필수