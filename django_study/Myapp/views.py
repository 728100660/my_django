from django.shortcuts import render
from .models import Animals
from django.http import HttpResponse,JsonResponse
# Create your views here.
def test(request):
    # s = Animals.objects.all()
    # return HttpResponse(s)
    return render(request,'form_study.html')

def base(request):
    context = {
        'title':'title'
    }
    return render(request,"extend.html",context=context)