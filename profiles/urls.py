

from django.urls import path ,include
from . import views


urlpatterns = [
    path('',views.profile,name="profile"),
    path('edit/',views.editprofile,name="editpro"),
]