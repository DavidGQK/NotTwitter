
from django.db import models
from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['group', 'text', 'image']
        labels = {
            'group': ('Группа'),
            'text': ('Текст'),
            'image': ('Изображение')
        }

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)