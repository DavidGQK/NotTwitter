from django.contrib import admin
from .models import Post, Group


class GroupAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ("pk", "title", "description", "slug",)
    search_fields = ("title", "description",)
    list_filter = ("title",)
    empty_value_display = "-пусто-"

admin.site.register(Group, GroupAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk','text', 'pub_date', 'author')
    search_fields = ('text',)
    list_filter = ('pub_date',)
    # empty_value_display = "-пусто-"

admin.site.register(Post, PostAdmin)
