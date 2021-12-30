from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=50,
        unique=True
    )
    description = models.TextField()

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(
        'Текст',
        help_text='Место для мыслей'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        help_text='Выберите группу',
        verbose_name='Группа'
    )
    image = models.ImageField(
        upload_to='posts/',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        author = self.author
        text = self.text[:10]
        return f'{author}: {text}'


class Comment(models.Model):
    post = models.ForeignKey(Post,
                            on_delete=models.CASCADE,
                            related_name='comments',
                            verbose_name='Запись')
    author = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name='comments',
                            verbose_name='Автор')                
    text = models.TextField('Текст',
                            help_text='Пиши тут!')
    created = models.DateTimeField(auto_now_add=True,
                            verbose_name='Дата публикации')
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Follow(models.Model):
    user = models.ForeignKey(User,
                            null=True,
                            on_delete=models.CASCADE,
                            related_name='follower',
                            verbose_name='Пользователь')
    author = models.ForeignKey(User,
                            null=True,
                            on_delete=models.CASCADE,
                            related_name='following',
                            verbose_name='Автор')
        
    class Meta:
        unique_together = ('user', 'author')
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'



