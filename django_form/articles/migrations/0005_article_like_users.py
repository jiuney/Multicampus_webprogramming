# Generated by Django 2.2.7 on 2019-11-12 06:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0004_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
