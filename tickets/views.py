from django.shortcuts import render,redirect, HttpResponseRedirect, HttpResponse    
from django.views import View
from .models import newticket
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
import random

class Login(View):
    def get(self,request):
        # return redirect('/detail')
        return render(request,'login.html')
    def post(self,request):
        username = request.POST['username']
        passwd  = request.POST['pass']
        user = auth.authenticate(username=username,password=passwd)
        if user is not None:
            auth.login(request,user)
            return render(request,'detail.html')
        else:
            messages.info(request,'Invelid credentials')
            return redirect('/')

class Register(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        name = request.POST['Name']
        username = request.POST['username']
        passwd = request.POST['pass']
        email = request.POST['email']
        uniq_id = random.randint()
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Already Taken')
            print('username')
            return HttpResponseRedirect('/register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email Already taken')
            print('email')
            return HttpResponseRedirect('/register')
        else:
            user = User.objects.create_user(username=username,password=passwd,first_name=name,email=email,id=uniq_id)
            user.save()
            return render(request,'newTickets.html')

class Logout(View):
    def get(self,request):
        auth.logout(request)
        return redirect('/')


class NewTickets(View):
    def get(self,request):
        return render(request,'newTickets.html')
    def post(self,request):
        department =request.POST['department']
        category = request.POST['category']
        url = request.POST['url']
        contact =request.POST['contact'] 
        description =request.POST['description']
        subject =request.POST['subject']
        email = request.POST['email']
        phone =request.POST['Phone']
        priority =request.POST['Priority']
        file =request.POST['file']
        obj1 = newticket(Department=department,category=category,url=url,Contact_name=contact,Description=description,subject=subject,email=email,phone=phone,priority=priority,file=file)
        obj1.save()
        # print(department,category,url)
        return render(request,'detail.html')
class Detail(View):
    def get(self,request):
        uid = User.objects.filter(username=User.first_name)
        for i in uid:
            # id = i.id
            print(i.id)
            data1= newticket.objects.all()
    #    for i in data1:
            if id == i.id:
              return render(request,'detail.html',{'data':data1})
            else:
                return redirect("/detal")
        return redirect("/detail")