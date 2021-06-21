from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, DocForm
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from .models import Docs
from django.db.models import Q

def index(request):
    return render(request, 'file/index.html', {})

def registerUser(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'file/register.html', {'form':form})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('homepage')
            else:
                messages.error(request, 'Username or Password is Incorrect')
        else:
            messages.error(request, 'Fill out all the fields')

    return render(request, 'file/login.html', {})


def homepage(request):
	return render(request, 'file/homepage.html', {})

def logoutUser(request):
    logout(request)
    return redirect('login')

def example(request):
    return render(request, 'file/example.html', {})

def contact(request):
    return render(request, 'file/contact.html', {} )

def fileload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'file/fileload.html', context)

def viewfile(request):
    dok = Docs.objects.all()
    return render(request, 'file/viewfile.html', {
        'dok': dok
        })

def upload_file(request):
    if request.method == 'POST':
        form = DocForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewfile')
    else:
        form = DocForm()
    return render(request, 'file/upload_file.html', {
        'form': form
        })

def delete_doc(request, id):
    if request.method == 'POST':
        doks = Docs.objects.get(id=id)
        doks.delete()
    return redirect('viewfile')

def search_file(request):
    search_post = request.GET.get('search')
    if search_post:
        dok = Docs.objects.filter(title__icontains=search_post)
    else:
        dok = Docs.objects.all()
    return render(request, 'file/viewfile.html', {
        'dok': dok
        })
