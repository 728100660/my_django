from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
#导入重定向包
from django.shortcuts import redirect
# Create your views here.

def home(request):
    return render(request,'home.html')

def Post(request):
    name = request.POST.get('username')
    return HttpResponse(name)

def Get(request,sid): 
    print(sid)
    return HttpResponse(12121)
#test和test2是路由的反向解析，写在html里面
def test(request):
    return render(request,'test.html')

def test2(request):
    return HttpResponse('成功！')

def test3(request):
    return render(request,'table.html')

#在vews里面的路由反向解析
def test4(request):
    url = reversed('TestUrl:test4')
    return redirect(url)