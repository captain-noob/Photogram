from django.shortcuts import render
from .models import user_detials
from django.utils import timezone
from django.http import HttpResponseRedirect


def login(request):
    flag=0
    if request.method=='POST':
        user=request.POST.get('username')
        passw=request.POST.get('pass')
        usertable = user_detials.objects.all()
        user_all = usertable.all()
        for userz in user_all:
            if userz.email==user and userz.password==passw:
                flag = 1
                request.session['username']=userz.username
                request.session['id']=userz.id
                break
            else:
                flag=0
    else:
        return logout(request)
    #check
    if flag == 1:
        return home(request)

    else:
        return render(request, 'login.html')
from home.views import home

def chk_session(request):
    if 'username' in request.session and 'id' in request.session:
        # return render(request, 'userlists.html')
        return HttpResponseRedirect('/photogram/')
    else:
        return render(request, 'login.html')

def logout(request):
    if 'logout' in request.GET:
        request.session.flush()
    else:
        return chk_session(request)





# signup
def signup(request):
    context = {}
    flag=0
    if request.method=='POST':
        user=request.POST.get('user')
        namez=request.POST.get('name')
        phone=request.POST.get('phone')
        emails=request.POST.get('email')
        passw=request.POST.get('password')
        passw1=request.POST.get('password1')
        time = timezone.now().today()
        # user_detials(username='1', name='1', phonenumber='1', propic='/media/user--default.png', email='1',password='1', date=time, followers=0, followings=0).save()

        usertable=user_detials.objects.all()
        user_all=usertable.all()
        for userz in user_all:
            if userz.username != user:
                flag = 1
            else:
                flag = 0
        #signup request
        if flag==1:
            for usern in user_all:
                if usern.email != emails:
                    if passw1 == passw:
                        user_detials(username=user, name=namez, phonenumber=phone, propic='/media/user--default.png',
                                     email=emails, password=passw1, date=time, followers=0, followings=0).save()
                        context['msg'] = 'Signup success... Continue with Login'
                    else:
                        context['msg'] = 'Password dosenot match'
                else:
                    context['msg'] = 'Email alredy exists'
        else:
            context['msg'] = 'Username alredy exist'
        #return
        return render(request, 'signup.html', context)
    else:
        return render(request, 'signup.html')