from django.shortcuts import render
from home.views import sessionchek
from .models import likes,comments
from accounts.models import user_detials
from upload.models import imguploads
from django.http import HttpResponseRedirect
from home.views import home


# Create your views here.
def like(request):
    flag=sessionchek(request)
    if flag==1:
        if 'id' in request.GET:
            id=request.session['id']
            im_id=request.GET['id']
            xxx = likes.objects.filter(photo_id=im_id,cus_id=id).count()
            if xxx==0:
                user = user_detials.objects.get(id=id)
                img = imguploads.objects.get(id=im_id)

                likes(cus_id=user, photo_id=img).save()
                ass = imguploads.objects.get(id=im_id)
                cnt = ass.likes + 1
                imguploads.objects.filter(id=im_id).update(likes=cnt)
                return home(request)

            return  home(request)
    else:
        return render(request,'login.html')

def commentz(request):
    flag = sessionchek(request)
    if flag == 1:
        if request.method=='POST':
            id=request.session['id']
            img_id=request.POST.get('img_id')
            comment=request.POST.get('comment')
            user = user_detials.objects.get(id=id)
            img = imguploads.objects.get(id=img_id)

            comments(cus_id=user,photo_id=img,comments=comment).save()

            cnt=comments.objects.filter(photo_id=img_id).count()
            imguploads.objects.filter(id=img_id).update(command=cnt)



            return  home(request)
        else:
            return  home(request)

    else:
        return render(request,'login.html')

def verification(request):
    flag = sessionchek(request)
    if flag == 1:
        if 'username' in request.GET:
            user=request.GET['username']
            user_detials.objects.filter(username=user).update(verified=2)
            return HttpResponseRedirect('/photogram/profile/')
    else:
        return render(request, 'login.html')