from django.shortcuts import render
from home.views import sessionchek
from django.core.files.storage import FileSystemStorage
from accounts.models import user_detials
from upload.models import imguploads

# Create your views here.


def profile(request):
    flag=sessionchek(request)
    if flag ==1 :
        return detials(request)
    else:
        return render(request,'login.html')

def index(request):

    flag = sessionchek(request)
    if flag == 1:
        return render(request, 'home.html')
    else:
        return render(request, 'login.html')

#detials


def detials(request):
    context={}
    id=request.session['id']
    name=request.session['username']
    user=user_detials.objects.get(username=name,id=id)
    img=imguploads.objects.filter(cusid=id).order_by('-id')
    context['img']=img
    context['username']=user.username
    context['email']=user.email
    context['mob']=user.phonenumber
    context['dp']=user.propic
    context['name']=user.name
    context['followers']=user.followers
    context['followings']=user.followings
    context['post']=user.post
    context['verified']=user.verified

    return render(request,'profile.html',context)

def editprofile(request):
    context = {}
    flag=sessionchek(request)
    if flag==1:
        id = request.session['id']
        name = request.session['username']
        if request.method=='POST':
            return editupload(request)
        else:
            userz = user_detials.objects.get(username=name, id=id)
            context['user'] = userz
            return render(request, 'editprofile.html', context)
    else:
        return render(request,'login.html')


def editupload(request):
    context={}
    flag=0
    id = request.session['id']
    name = request.session['username']
    names = request.POST.get('name')
    username = request.POST.get('username')
    number = request.POST.get('number')

    email = request.POST.get('email')
    password = request.POST.get('password')
    password1 = request.POST.get('password1')
    usertable = user_detials.objects.get(username=name,id=id)

    table = user_detials.objects.all()
    user_id=0
    # varables
    f1=0
    f2=0
    f3=0
    f4=0
    f5=0
    f6=0

    # name update
    if names == usertable.name or names == "":
        f1=0
    else:
        user_detials.objects.filter(id=id).update(name=names)
        f1=1

    # username upload

    if username == usertable.username or username == "" :
       f2=0
    else:
        for i in table:
            if i.username == username:
                user_id=i.id
                flag=1
                break
            else:
                flag=0
        if flag==1:
            if user_id == id:
                user_detials.objects.filter(id=id).update(username=username)
                request.session['username']=username
                context['msg'] = 'username saved'
            else:
                context['msg'] = 'username alredy exist'
        else:
            user_detials.objects.filter(id=id).update(username=username)
            request.session['username'] = username
            context['msg'] = 'username saved'
    # number
    if number == usertable.phonenumber or number == "":
        context['msg']='phonenumber not updated '
    else:
        user_detials.objects.filter(id=id).update(phonenumber=number)
        context['msg'] = 'number  updated'

    # email
    if email == usertable.email or email == "" :
        context['msg']='email not updated'
    else:
        for i in table:
            if i.email == email:
                user_id=i.id
                flag=1
                break
            else:
                flag=0
        if flag==1:
            if user_id == id:
                user_detials.objects.filter(id=id).update(email=email)
                context['msg'] = 'email saved'
            else:
                context['msg'] = 'email alredy exist'
        else:
            user_detials.objects.filter(id=id).update(email=email)
            context['msg'] = 'email saved'

    # password
    if  names == "":
        context['msg']='password not updated '
    else:
        if password == password1:
            user_detials.objects.filter(id=id).update(name=names)
            context['msg'] = 'password is saved'
        else:
            context['msg'] = 'password match error'
#photo upload

    if 'image'in request.FILES:
        image = request.FILES['image']
        fs = FileSystemStorage()
        namez = fs.save(image.name, image)
        url = fs.url(namez)
        user_detials.objects.filter(id=id).update(propic=url)
    else:
        context['msg'] = 'image error'
    context['msg'] = 'updated successfully'
    a=request.session['username']
    usertable = user_detials.objects.get(username=a,id=id)
    context['user'] = usertable
    return render(request, 'editprofile.html', context)