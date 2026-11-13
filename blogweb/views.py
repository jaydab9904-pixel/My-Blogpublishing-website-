from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Post
from .forms import PostForm, RegisterForm
# Create your views here.


def home(request):
    
    query = request.GET.get('q', '').strip()
    
    posts = Post.objects.all().order_by('-created_at')

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__icontains=query) |
            Q(category__name__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'website_name': 'Homepage',
        'welcome_message': 'Welcome! Discover our Blogs.',
        'posts': page_obj,
        'query': query,
        'page_obj': page_obj,
    }

    return render(request, 'blogweb/home.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.author = request.user.username
            post.save()
            form.save_m2m()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'blogweb/create_post.html', {'form': form})



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'blogweb/post_detail.html', {'post': post})


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if post.owner != request.user:
        return render(
            request,
            'blogweb/not_authorized.html',
            status=403
        )

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(
        request,
        'blogweb/edit_post.html',
        {'form': form, 'post': post}
    )


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.owner != request.user:

        return render(
                request,
                'blogweb/not_authorized.html',
                status=403
            )

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'blogweb/confirm_delete.html', {'post': post})

@login_required
def delete_all_my_posts(request):
    if request.method == 'POST':
        request.user.posts.all().delete()
        return redirect('home')

    return render(request, 'blogweb/confirm_delete_all.html')



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'blogweb/register.html', {'form': form})

