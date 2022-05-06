from dataclasses import fields
from distutils.log import Log
import imp
from multiprocessing import context
from operator import length_hint
from tarfile import LENGTH_NAME
from unicodedata import name
from django.shortcuts import render,redirect,get_object_or_404
from .models import Articles, Post, Qundylyq, Quram,Logs
from .forms import ArticlesForm,CreateUserForm, Logreg,ContactForm
from django.views.generic import DetailView,UpdateView,DeleteView
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from main.decorators import unauthenticated_user,allowed_users,admin_only
from django.template.loader import render_to_string

from django.core.mail import EmailMessage
from django.core.mail import send_mail

@unauthenticated_user
def registerPage(request):
    

    form=CreateUserForm()
    
    if request.method =='POST':
        form=CreateUserForm(request.POST)
        form2=Logreg(request.POST)
        email = request.POST['email']
        email_subject = 'Registration notification'
        email_body = render_to_string('news/activate.html')
        emaill=EmailMessage(subject=email_subject, body=email_body, from_email='200103023@stu.sdu.edu.kz', to=[email])
        if form.is_valid():
            form2.save()
            user=form.save()
            username=form.cleaned_data.get('username')
            emaill.send()

            group=Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request,'Account was created successfully for '+username)

            return redirect('login')

    context={'form':form}
    return render(request,'news/register.html',context)

@unauthenticated_user
def loginPage(request):
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'username or password is incorrect')
        
        context={}
        return render(request,'news/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def news_home(request):
    news = Articles.objects.extra(select={'length':'Length(title)'}).order_by('-length') 
    return render(request,'news/news_home.html',{'news':news})

class NewDetailView(DetailView):
    model=Articles
    template_name='news/details_view.html'
    context_object_name='article'


class NewUpdateView(UpdateView):
    model=Articles
    template_name='news/create.html'
    
    form_class=ArticlesForm

class NewDeleteView(DeleteView):
    model=Articles
    success_url='/news/'
    template_name='news/news-delete.html'

class QuramView(DetailView):
    model=Quram
    template_name='news/quram.html'
    context_object_name='quram'

class QundylyqView(DetailView):
    model=Qundylyq
    template_name='main/qundylyq.html'
    context_object_name='qundylyq'


def userPage(request):
    news = Articles.objects.extra(select={'length':'Length(title)'}).order_by('-length') 
    context={'news':news}
    return render(request,'news/user.html',context)

@login_required(login_url='login')
@admin_only
def show_post(request,post_slug):
    post=get_object_or_404(Post,slug=post_slug)
    context={'post':post}
    return render(request,'news/post.html',context=context)

@login_required(login_url='login')
@admin_only
def index(request):
    return render(request,'news/index.html')    

@login_required(login_url='login')
@admin_only
def create(request):
    error=''
    if request.method =='POST':
        form = ArticlesForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполена неверно!'    

    form=ArticlesForm()

    data={
        'form':form,
        'error':error
    }

    return render(request,'news/create.html',data)

def clientPage(request):
    return render(request, 'news/client.html')  

def send_message(request):

    email = EmailMessage(
        'PictureSend',
        'Picture sent successfully and here',
        '200103023@stu.sdu.edu.kz',
        ['200103023@stu.sdu.edu.kz'],
        headers={'Message-ID':'foo'},
    )
    email.attach_file('E:/photo/back.png')
    email.send(fail_silently=False)
    return render(request, 'news/successfull.html')
  