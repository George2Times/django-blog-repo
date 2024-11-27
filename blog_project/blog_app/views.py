from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog_app/post_list.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'blog_app/register.html', {'form': form})

@login_required
def post_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content, author=request.user)
        messages.success(request, 'Post created successfully!')
        return redirect('post-list')  # użyj poprawnej nazwy widoku zamiast 'blog-home'
    return render(request, 'blog_app/post_form.html')

@login_required
def post_update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user != post.author:
        return redirect('post-list')
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        messages.success(request, 'Post updated successfully!')
        return redirect('post-list')
    return render(request, 'blog_app/post_form.html', {'post': post})
