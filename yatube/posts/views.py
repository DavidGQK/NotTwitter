from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Group
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model


User = get_user_model()


def profile(request, username):
    profile = get_object_or_404(User, username=username)
    post_list = Post.objects.filter(author = profile).order_by('-pub_date').all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    posts_count = post_list.count()
    page = paginator.get_page(page_number)
    context = {'profile': profile, 'page': page, 'paginator': paginator, 'posts_count': posts_count}
    return render(request, "profile.html", context)
 
 
def post_view(request, username, post_id):
    profile = get_object_or_404(User, username=username)
    post = get_object_or_404(Post, pk=post_id)
    post_list = Post.objects.filter(author = profile).order_by('-pub_date').all()
    posts_count = post_list.count()
    context = {'profile': profile, 'post': post, 'posts_count': posts_count}
    return render(request, "post.html", context)


def post_edit(request, username, post_id):
    if request.user.username != username:
        return redirect(f'/{username}/{post_id}')

    title = "Редактировать запись"
    btn_caption = "Сохранить"
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            n_post = form.save(commit=False)
            n_post.author = request.user
            n_post.save()
            return redirect(f'/{username}/{post_id}')      
    form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form, 'title': title, 'btn_caption': btn_caption, 'post': post})

@login_required
def new_post(request):
    title = "Добавить запись"
    btn_caption = "Добавить"
    form = PostForm(request.POST or None, files=request.FILES or None)
    if request.method == "POST" and form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect("index")
    form = PostForm()
    return render(request, "post_new.html", {"form": form, "title": title, "btn_caption": btn_caption})

# view-функция для страницы сообщества
def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    # Метод .filter позволяет ограничить поиск по критериям. Это аналог добавления
    # условия WHERE group_id = {group_id}
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(request, "group.html", {"group": group, "posts": posts})


def index(request):
        post_list = Post.objects.order_by('-pub_date').all()
        paginator = Paginator(post_list, 10)  # показывать по 10 записей на странице.

        page_number = request.GET.get('page')  # переменная в URL с номером запрошенной страницы
        page = paginator.get_page(page_number)  # получить записи с нужным смещением
        return render(
            request,
            'index.html',
            {'page': page, 'paginator': paginator}
       )


