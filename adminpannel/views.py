from django.shortcuts import render
from .models import admin
from django.contrib.sessions.models import Session
from django.contrib.sessions.base_session import AbstractBaseSession
from accounts.models import user_detials
from django.http import HttpResponseRedirect
from upload.models import imguploads
from rating.models import likes,comments

# Create your views here.
def adminlogin(request):

    flag=0
    context={}
    session=sessioncheck(request)
    if session== 1:
        return HttpResponseRedirect('pannel/')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('pass')

            result=admin.objects.all()
            for adminz in result:
                if adminz.username == username and adminz.password == password:
                    flag = 1
                    request.session['admin_uname'] = adminz.username
                    request.session['admin_id'] = adminz.id
                    break
                else:
                    flag = 0

            if flag==1:
                return HttpResponseRedirect('pannel/')
            else:
                msg="Password Incorrect"
                context['msg'] = msg

        return render(request,'adminlogin.html',context)


def sessioncheck(request):
    flag=0
    if 'admin_id' in request.session:
        flag=1
        return flag
    else:
        flag=0
        return flag


def index(request):
    flag=sessioncheck(request)
    if flag==1:
        context = {}
        online = Session.objects.all().count()
        usercount = user_detials.objects.all().count()
        images= imguploads.objects.all().count()
        context['users'] = usercount
        context['online'] = online -1
        context['imgc'] = images
        return render(request, 'pannel/index.html', context)
    else:
        return adminlogin(request)

def adminlogout(request):
    if 'admin_id' in request.session:
        request.session.flush()
        return adminlogin(request)

def reportedpro(request):
    flag=sessioncheck(request)
    context={}
    if flag==1:
        users=user_detials.objects.filter(report__gt=0)
        context['user']=users
        return render(request,'pannel/activity.html',context)
    else:
        return adminlogin(request)

def displaypro(request):
    flag = sessioncheck(request)
    context = {}
    if flag == 1:
        if 'user' in request.GET:
            name = request.GET['user']
            user = user_detials.objects.get(username=name)
            id = user.id
            img = imguploads.objects.filter(cusid=id).order_by('-id')
            context['img'] = img
            context['username'] = user.username
            context['email'] = user.email
            context['mob'] = user.phonenumber
            context['dp'] = user.propic
            context['name'] = user.name
            context['followers'] = user.followers
            context['followings'] = user.followings
            context['post'] = user.post
            context['verified'] = user.verified
            return render(request, 'profile/profile.html',context)
        else:
            return HttpResponseRedirect('/admin/')
    else:
        return adminlogin(request)


def reportedimages(request):
    flag = sessioncheck(request)
    context = {}
    if flag == 1:
        img=imguploads.objects.filter(report__gte=1)
        use=user_detials.objects.all()
        context['img']=img
        context['user']=use
        if 'id' in request.GET:
            id=request.GET['id']
            imguploads.objects.filter(id=id).update(report=0)
        if 'delid' in request.GET:
            id=request.GET['delid']
            likes.objects.filter(photo_id=id).delete()
            comments.objects.filter(photo_id=id).delete()
            imguploads.objects.filter(id=id).delete()
        return render(request,'pannel/message.html',context)
    else:
        return adminlogin(request)


def verification(request):
    flag = sessioncheck(request)
    context = {}
    if flag == 1:
        ver=user_detials.objects.filter(verified=2)
        context['img']=ver


        return render(request,'pannel/task.html',context)
    else:
        return adminlogin(request)
def f1(request):
    if 'user' in request.GET:
        users = request.GET['user']
        user_detials.objects.filter(username=users).update(verified=0)

    if 'userver' in request.GET:
        userz = request.GET['userver']
        user_detials.objects.filter(username=userz).update(verified=1)

    return HttpResponseRedirect('/admin/')

def ver(request):
    if 'user' in request.GET:
        context={}
        name = request.GET['user']
        user = user_detials.objects.get(username=name)
        id = user.id
        img = imguploads.objects.filter(cusid=id).order_by('-id')
        context['img'] = img
        context['username'] = user.username
        context['email'] = user.email
        context['mob'] = user.phonenumber
        context['dp'] = user.propic
        context['name'] = user.name
        context['followers'] = user.followers
        context['followings'] = user.followings
        context['post'] = user.post
        context['verified'] = user.verified
        return render(request, 'ver/profile.html', context)
    else:
        return HttpResponseRedirect('/admin/')


def function(request):
    if 'cancel' in request.GET:
        username=request.GET['cancel']
        user_detials.objects.filter(username=username).update(report=0)


    if 'delete' in request.GET:
        username = request.GET['delete']
        user=user_detials.objects.get(username=username)
        id=user.id
        im=imguploads.objects.filter(cusid=id)
        for image in im:
            imageid=image.id
            likes.objects.filter(photo_id=imageid).delete()
            comments.objects.filter(photo_id=imageid).delete()
        imguploads.objects.filter(cusid=id).delete()
        user_detials.objects.filter(id=id).delete()
    return HttpResponseRedirect('/admin/')