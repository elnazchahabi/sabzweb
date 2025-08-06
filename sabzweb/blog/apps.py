from django.apps import AppConfig
from django.db import connection

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name='وبلاگ'

