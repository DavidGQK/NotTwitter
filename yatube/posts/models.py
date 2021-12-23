from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название группы",
                             null=False)
    slug = models.SlugField(verbose_name="Ссылка", unique=True)
    description = models.TextField(verbose_name="Описание группы",
                                   max_length=300)

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name="Текст поста")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Автор поста",
                               related_name="post_author")
    # '''
    # Возможность в посте ссылаться на группу.
    # Чтобы пост не пропал при удалении группы задаем SET_NULL.
    # '''
    group = models.ForeignKey(Group, on_delete=models.CASCADE,
                              verbose_name="Тег группы",
                              related_name='group_posts', blank=True, null=True)

    image = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
       return self.text



