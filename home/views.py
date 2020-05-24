from django.shortcuts import render
from rating.models import comments
# Create your views here.

def home(request):
    flag = sessionchek(request)
    if flag == 1:
        return homedisp(request)
    else:
        return render(request, 'login.html')


def sessionchek(request):
    flag=0
    if 'username' in request.session and 'id' in request.session:
        id=request.session['id']
        cap = user_detials.objects.get(id=id)
        if request.session['username'] == cap.username:
            flag=1
            return flag
        else:
            flag = 0
            return flag
    else:
        flag = 0
        return flag
from accounts.models import user_detials
from upload.models import imguploads

def homedisp(request):
    commentxz=comments.objects.all()
    img=imguploads.objects.all().order_by('-id')
    cap=user_detials.objects.all()
    context={'img':img}
    context['uid']=cap
    context['comment']=commentxz
    return render(request, 'home.html',context)
