from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    path('profile/', include('profiles.urls')),
    path('upload/', include('upload.urls')),
    path('user/',include('userlist.urls')),
    path('friends/',include('friends.urls')),
    path('rating/',include('rating.urls')),
]