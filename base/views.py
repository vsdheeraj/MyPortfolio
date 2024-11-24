from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader  import render_to_string

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .models import *
from .form import *
from .filters import *

import os              
from dotenv import load_dotenv
load_dotenv()               #for 'os.environ.get("MY_EMAIL")' in sendEmail view - so that mail is sent to themselves.

# Create your views here.
def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    return render(request, 'base/index.html', {'posts':posts})

def posts(request):
    posts = Post.objects.filter(active = True)  
    myFilter = PostFilter(request.GET, queryset=posts)
    posts = myFilter.qs
    
    page = request.GET.get('page')
    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'base/posts.html', {'posts':posts, 'myFilter':myFilter})

def post(request, slug):
	post = Post.objects.get(slug=slug)
	return render(request, 'base/post.html', {'post' : post})

def profile(request):
    return render(request, 'base/profile.html')


# CRUD VIEWS
@login_required(login_url='home')
def createPost(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('posts')

    return render(request, 'base/post_form.html', {'form':form})

@login_required(login_url='home')
def updatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES,instance=post)
        if form.is_valid:
            form.save()
            return redirect('post', slug=post.slug)

    return render(request, 'base/post_form.html', {'form':form})

@login_required(login_url='home')
def deletePost(request, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')

    return render(request, 'base/delete.html', {'item':post})


# Email Sending
def sendEmail(request):

	if request.method == 'POST':

		template = render_to_string('base/email_template.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})

		email = EmailMessage(
			request.POST['subject'],           # Subject from the form
			template,                          # Email body (rendered HTML template)
			settings.EMAIL_HOST_USER,          # Sender email from settings
			[os.environ.get("MY_EMAIL")]       # Recipient email(s)
			)

		email.fail_silently=False
		email.send()

	return render(request, 'base/email_sent.html')


# Login, Register & Logout
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')

	if request.method == 'POST':
		email = request.POST.get('email')
		password =request.POST.get('password')

		#Little Hack to work around re-building the usermodel
		try:
			user = User.objects.get(email=email)  # fetch the user by email
			user = authenticate(request, username=user.username, password=password) # authenticate
		except: 
			messages.error(request, 'User with this email does not exists')
			return redirect('login')
			
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Email OR password is incorrect')

	context = {}
	return render(request, 'base/login.html', context)

def registerPage(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')  # Get the email from the form
            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists! Please choose a different one.')
                return redirect('register')  # Redirect back to the registration page
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Account successfuly created!')
            
            user = authenticate(request, username=user.username, password=request.POST['password1']) #Attempts to log the user in after registration.

            if user is not None:
                login(request, user)          # If authentication is successful, the user is logged in immediately using Django's login() method.
                
            next_url = request.GET.get('next')  # Handles redirection - 'next'in (?next=/some/url) specifies where to go after login.
            if next_url == '' or next_url == None: 
                next_url = 'home'
            return redirect(next_url)
        else:
            messages.error(request, 'An error has occured with registration')
    context = {'form':form}
    return render(request, 'base/register.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')