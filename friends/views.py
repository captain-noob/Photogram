from django.shortcuts import render
from django.http import HttpResponseRedirect
from accounts.models import user_detials
from home.views import sessionchek ,homedisp
from .models import followings,followers
from upload.models import imguploads
from userlist.views import userlist

# Create your views here.
def friend(request):
    flag=sessionchek(request)
    if flag == 1:
        context={}
        if 'username' in request.GET:
            username = request.GET['username']
            myids = request.session['id']
            myusrname = request.session['username']

            follow=followings.objects.filter(myuid_id=myids,follw_uname=username).count()
            user = user_detials.objects.get(username=username)
            userz = user_detials.objects.get(username=myusrname)

            folr=followers.objects.filter(myid=userz,foll_uid=user).count()

            fid = user.id
            fname = user.username




            if follow ==0 and folr == 0:
                followings(myuid_id=myids,follw_uid_id=fid,follw_uname=fname,myusname=myusrname).save()
                followers(myid=userz,myuname=myusrname,foll_uname=fname,foll_uid=user).save()

                folcount=followers.objects.filter(foll_uid=fid).count()
                count=followings.objects.filter(myuid_id=myids).count()

                user_detials.objects.filter(id=myids).update(followings=count)
                user_detials.objects.filter(id=fid).update(followers=folcount)

            return userlist(request)
        else:
            return HttpResponseRedirect('/photogram/user')
    else:
        return render(request,'login.html')



def unfriend(request):
    flag = sessionchek(request)
    if flag == 1:
        context = {}
        if 'username' in request.GET:
            username = request.GET['username']
            myids = request.session['id']
            myusrname = request.session['username']

            follow = followings.objects.filter(myuid_id=myids, follw_uname=username).count()
            user = user_detials.objects.get(username=username)
            userz = user_detials.objects.get(username=myusrname)

            folr=followers.objects.filter(myid=userz,foll_uid=user).count()


            fid = user.id
            fname = user.username

            if follow == 1 and folr == 1:
                followings.objects.get(myuid_id=myids, follw_uid_id=fid, follw_uname=fname, myusname=myusrname).delete()
                followers.objects.get(myid=userz, myuname=myusrname, foll_uname=fname, foll_uid=user).delete()

                folcount = followers.objects.filter(foll_uid=fid).count()
                count = followings.objects.filter(myuid_id=myids).count()
                #
                user_detials.objects.filter(id=myids).update(followings=count)
                user_detials.objects.filter(id=fid).update(followers=folcount)

            return userlist(request)
        else:
            return HttpResponseRedirect('/photogram/user')
    else:
        return render(request, 'login.html')

def reportprofile(request):
    flag = sessionchek(request)
    if flag == 1:
        context = {}
        if 'username' in request.GET:
            username = request.GET['username']
            user=user_detials.objects.get(username=username)

            report=user.report+1

            user_detials.objects.filter(username=username).update(report=report)
            request.session['report']="reported Successfully"
            return userlist(request)
        else:
            return HttpResponseRedirect('/photogram/user')

    else:
        return render(request, 'login.html')

def reportphoto(request):
    flag = sessionchek(request)
    if flag == 1:
        if 'id' in request.GET:
            id = request.GET['id']
            user = imguploads.objects.get(id=id)

            report = user.report + 1

            imguploads.objects.filter(id=id).update(report=report)
            request.session['report'] = "reported Successfully"
            return homedisp(request)
    else:
        return render(request, 'login.html')