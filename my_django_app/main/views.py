from django.shortcuts import render,redirect
from .decorators import allowed_users,admin_only
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from news.models import Articles
from news.forms import ContactForm
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.contrib import messages


@login_required(login_url='login')
@admin_only
def index(request):
    data={
        'title':'Главная страница',
        'values':['Some','GN','01012022'],
        'obj':{
            'car':'Mercedes',
            'age':'19',
            'hobby':'Reading'          
        }
    }
    return render(request,'main/index.html',data)

@login_required(login_url='login')   
def about(request):
    return render(request,'main/index1.html')
  
def test(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], '200103023@stu.sdu.edu.kz', ['ashykbaev03@gmail.com'], fail_silently=True)
            if mail:
                messages.success(request, 'Email is send!')
                return redirect('about')
            else:
                messages.error(request,'Sending error!')
        else:
            messages.error(request, 'Register error!')
    else:
        form=ContactForm()
    return render(request, 'main/index1.html', {'form':form})  
  