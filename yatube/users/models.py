from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class User(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название группы",
                             null=False)
    slug = models.SlugField(verbose_name="Ссылка", unique=True)
    description = models.TextField(verbose_name="Описание группы",
                                   max_length=300)

    def __str__(self):
        return self.title
