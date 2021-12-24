from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post, Group, Follow
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model


User = get_user_model()


@login_required
def add_comment(request, username, post_id):
    post = get_object_or_404(Post, author__username=username, id=post_id)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post', username, post_id)
    return render(request, 'profile.html', {'form': form, 'post': post})


@login_required
def follow_index(request):
    post_list = Post.objects.filter(author__following__user=request.user)
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'follow.html', {'page': page, 'paginator': paginator})


@login_required
def profile_follow(request, username):
    author = get_object_or_404(User, username=username)
    if request.user != author:
        Follow.objects.get_or_create(user=request.user, author=author)
    return redirect('profile', username)


@login_required
def profile_unfollow(request, username):
    author = get_object_or_404(User, username=username)
    follow_to_delete = Follow.objects.filter(user=request.user, author=author)
    follow_to_delete.delete()
    return redirect('profile', username)


def page_not_found(request, exception):
    return render(request, "misc/404.html", {"path": request.path}, status=404)


def server_error(request):
    return render(request, "misc/500.html", status=500)


@login_required
def profile(request, username):
    # author = get_object_or_404(User, username=username)
    # post_list = Post.objects.filter(author = author).order_by('-pub_date').all()
    author = get_object_or_404(User, username=username)
    post_list = author.posts.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    subscribe = request.user.is_authenticated and Follow.objects.filter(
        user=request.user,
        author=author
    ).exists()
    return render(request, 'profile.html', {'page': page, 'paginator': paginator, 'author': author, 'subscribe': subscribe})


# @login_required
# def post_view(request, username, post_id):
#     profile = get_object_or_404(User, username=username)
#     post = get_object_or_404(Post, pk=post_id)
#     post_list = Post.objects.filter(author = profile).order_by('-pub_date').all()
#     posts_count = post_list.count()
#     context = {'profile': profile, 'post': post, 'posts_count': posts_count}
#     form = PostForm(request.POST or None, files=request.FILES or None, instance=post)
#     return render(request, "post.html", context)

@login_required
def post(request, username, post_id):
    post = get_object_or_404(Post, author__username=username, id=post_id)
    form = CommentForm()
    return render(request, 'profile.html', {'post': post, 'author': post.author, 'form': form})


@login_required
def post_edit(request, username, post_id):
    title = "Редактировать запись"
    btn_caption = "Сохранить"
    post = get_object_or_404(Post, author__username=username, id=post_id)
    if request.user != post.author:
        return redirect('post', username, post_id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post', username, post_id)
    return render(request, 'new_post.html', {'post': post, 'form': form, 'title': title, 'btn_caption': btn_caption})


@login_required
def new_post(request):
    title = "Добавить запись"
    btn_caption = "Добавить"
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('index')
    return render(request, 'new_post.html', {'form': form, 'title': title, 'btn_caption': btn_caption})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    post_list = group.posts.all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'group.html', {'page': page, 'paginator': paginator, 'group': group})


def index(request):
    post_list = Post.objects.select_related('author', 'group').all()
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html', {'page': page, 'paginator': paginator})
        
        
        
        
