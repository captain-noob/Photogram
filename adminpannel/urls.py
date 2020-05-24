from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.adminlogin,name="adminlogin"),
    path('pannel/',views.index,name="adminhome"),
    path('logout/',views.adminlogout,name="logout"),
    path('reported/',views.reportedpro,name="reported"),
    path('imager/',views.reportedimages,name='images'),
    path('verify/',views.verification,name='veri'),
    path('prifile/',views.displaypro,name='pro'),
    path('fn/',views.function,name='fn'),
    path('verp/',views.ver,name='pr'),
    path('f1/',views.f1,name='f1'),
]