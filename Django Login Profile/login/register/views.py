from django.shortcuts import render
from register.models import *
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth import authenticate
import json,requests
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
# Create your views here.
def logindata(request):
	print('hello')
	return render(request,'basic.html')

def registerdata(request):
	print('hello')
	return render(request,'register.html')

def register(request):
    if request.method == "POST":
        permission_classes = (IsAuthenticated,)
        data = json.loads(request.body)
        fname=data['fname']
        lname=data['lname']
        email=data['email']
        password=data['password']
        passwordnew =  make_password(password)

        phone=data['phone']
        address=data['address']
        form = CreateUser(fname=fname,lname=lname,email=email,password=passwordnew,phone=phone,address=address)
        form.save()
        post_data = {'username': 'Anurodh','password':'123456789'}
        url = request.build_absolute_uri('/api/token/')
        response = requests.post(url, data=post_data)
        content = response.content
        access = json.loads(content)['access']
        refresh = json.loads(content)['refresh']
        return JsonResponse({'result':'success','access':access,'refresh':refresh})

def profile(request):
    #import pdb;pdb.set_trace()
    if request.user.is_authenticated:
        alldata =CreateUser.objects.all()
        return render(request, 'profile.html', {"client":alldata})
@csrf_exempt
def auth(request):
  if request.method == "POST":
    if request.user.is_authenticated:
        return HttpResponse('success')
    else:
        if request.user.is_authenticated==False:
            data = json.loads(request.body)
            print(data['refresh'])
            refresh = {'refresh':data['refresh']}
            url = request.build_absolute_uri('/api/token/refresh/')
            response = requests.post(url, data=refresh)
            content = response.content
            access = json.loads(content)['access']
            print(access)
            return JsonResponse({'res':'refresh token','access':access})
        return HttpResponse('fail')