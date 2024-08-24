from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView


def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PostForm()
    
    return render(request, 'index.html', {'form': form})


def success(request):
    return render(request, 'success.html')



def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list')
            else:
                messages.error(request, "Login yoki parol noto'g'ri.")
        else:
            messages.error(request, "Login yoki parol noto'g'ri.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = "list.html"



class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = "detail.html"



def user_logout(request):
    logout(request)
    return redirect('login')