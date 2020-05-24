from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.like,name='like' ),
    path('comments/',views.commentz,name='comment' ),
    path('verify/',views.verification,name='verify' ),
]