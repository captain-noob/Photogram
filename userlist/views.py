from django.shortcuts import render
from django.http import HttpResponseRedirect
from home.views import sessionchek
from accounts.models import user_detials
from upload.models import imguploads
from friends.models import followings
from rating.models import comments


# Create your views here.
def userlist(request):
    context = {}
    flag=sessionchek(request)
    if flag == 1:

        if request.method == 'POST':
            return search(request)
        else:
            if 'username' in request.GET:
                username = request.GET['username']
                user = request.session['username']
                ids = request.session['id']
                if username == user:
                    return HttpResponseRedirect('/photogram/profile')
                else:
                    user = user_detials.objects.get(username=username)
                    userid = user.id
                    img = imguploads.objects.filter(cusid=userid).order_by('-id')
                    following=followings.objects.filter(follw_uid_id=userid,myuid_id=ids).count()
                    if following==1:
                        context['following']=1
                    else:
                        context['following']=0

                    context['username'] = user.username
                    context['img'] = img
                    context['name'] = user.name
                    context['dp'] = user.propic
                    context['verified'] = user.verified
                    context['followers'] = user.followers
                    context['followings'] = user.followings
                    context['post'] = user.post
                    commentxz = comments.objects.all()
                    context['comment'] = commentxz
                    context['user'] = user
                    return render(request, 'userlists.html', context)
            else:
                return render(request, 'search.html')
    else:
        return render(request, 'login.html')

def search(request):
    context={}
    searchid = request.POST.get('search')
    use=user_detials.objects.all()
    flag=0
    for user in use:
        if user.username == searchid:
            uid=user.id
            flag=1
            break

    if flag==1:
        usr = user_detials.objects.get(id=uid)
        context['i'] = usr
        return render(request, 's1.html', context)
    else:
        uses = user_detials.objects.filter(name__contains=searchid)
        context['user']=uses
        return render(request, 's2.html',context)