from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import students
import time
# 导入加密模块
import hashlib
# Create your views here.


def test(request):
    return HttpResponse(111)


def login(request):
    print('hello')
    return render(request,'login.html')


def do_login(request):
    username = request.POST.get('username')

    response = HttpResponseRedirect(reverse('Cookie_session:mine'))

    response.set_cookie('username',username)

    return response

def mine(request):
    username = request.COOKIES.get('username')
    if username:
        return HttpResponse(username)
    else:
        return redirect(reverse('Cookie_session:login'))

def t_mine(request):
    token = request.COOKIES.get('token')
    print('token',token)
    try:
        student = students.objects.get(token=token)
    except:
        print(2)
        return redirect(reverse('Cookie_session:t_login'))
    return render(request,'t_mine.html',context={'username':student.username})

def t_login(request):
    #高内聚
    #通过浏览器url访问的时候请求方法是get，此时返回t_login页面
    #post既是点击了登录按钮
    if request.method == 'GET':
        return render(request,'t_login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # student的形式<QuerySet [{'id': 1, 'username': 'Jeck', 'password': '1234', 'token': '0'}]>
        student = students.objects.filter(username=username,password=password)
        if student:
            ip = request.META.get('REMOTE_ADDR')
            print(ip)
            token = generate_token(ip)
            print(token)
            # 必须加此行，否则student是queryset类型
            student = student.first()
            # 现在的student是students的对象 students object (1)
            print(type(student))
            print(student)
            student.token = token
            student.save()
            response = redirect(reverse('Cookie_session:t_mine'))
            response.set_cookie('token',token)
            return response
        else:
            print('账号或者密码输入错误')
            return redirect(reverse('Cookie_session:t_login'))
    

def generate_token(ip):
    t = time.ctime()
    return hashlib.new("md5",(ip+t).encode("utf-8")).hexdigest()
