from django.urls import path ,include
from . import views


urlpatterns = [
    path('',views.friend,name='followzzzz'),
    path('unfollow/',views.unfriend,name='unfollow'),
    path('report/',views.reportprofile,name='report'),
    path('reportphoto/',views.reportphoto,name='photoreport'),
]