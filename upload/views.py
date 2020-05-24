from django.shortcuts import render
from  home.views import sessionchek

from accounts.models import user_detials
from .models import imguploads
from django.core.files.storage import FileSystemStorage


# Create your views here.
def uploads(request):
    flag = sessionchek(request)
    if flag==1:
        return fileupload(request)
    else:
        return render(request,'login.html')

def fileupload(request):
    if request.method=='POST':
        photo=request.FILES['photo']
        text=request.POST.get('text')
        id=request.session['id']
        fs=FileSystemStorage()
        acc=user_detials.objects.get(id=id)
        name=fs.save(photo.name,photo)
        url=fs.url(name)
        imguploads(image=url,caption=text,cusid=acc,command=0,likes=0  ).save()
        s='upload successfully'
        context={'msg':s}
        imcount=imguploads.objects.filter(cusid=id).count()

        user_detials.objects.filter(id=id).update(post=imcount)

        return render(request, 'photouploads.html',context)
    else:
        return render(request, 'photouploads.html')