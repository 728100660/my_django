from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def upload_file(request):
    if request.method == 'GET':
        return render(request,'upload_file.html')
    elif request.method == 'POST':
        rec_file = request.FILES.get('icon')
        print(rec_file)
        # with 在读取完毕后，自动关闭
        with open("D:/python_code/django_study/static/img/test.docx",'wb') as save_file:
            for part in rec_file.chunks():
                save_file.write(part)
                save_file.flush()
        return HttpResponse("文件上传成功")