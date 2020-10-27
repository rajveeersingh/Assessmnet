from django.shortcuts import render,redirect, HttpResponseRedirect
from django.views import View
from .models import newticket
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
import random

class login(View):
    def get(self,request):
        return redirect('/detail')
        # return render(request,'login.html')
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

class register(View):
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

class logout(View):
    def get(self,request):
        auth.logout(request)
        return redirect('/')


class newTickets(View):
    def get(self,request):
        return render(request,'newTickets.html')
    def post(self,request):
        # department =newtickets.objects.create(Department=request.POST['department'])
        # category = newtickets.objects.create(category=request.POST['category'])
        # url = newtickets.objects.create(url=request.POST['url'])
        # contact = newtickets.objects.create(Contact_name=request.POST['contact'])
        # description = newtickets.objects.create(Description=request.POST['description'])
        # subject = newtickets.objects.create(subject=request.POST['subject'])
        # email = newtickets.objects.create(email=request.POST['email'])
        # phone = newtickets.objects.create(phone=request.POST['Phone'])
        # priority = newtickets.objects.create(priority=request.POST['Priority'])
        # file = newtickets.objects.create(file=request.POST['file'])
        # print(department,category)        
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
class detail(View):
    def get(self,request):
       uid = User.id
       data= newticket.objects.filter(id=uid)
       print(data.url)
       return render(request,'detail.html',{'data':data})