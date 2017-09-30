from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^userlist/(?P<room_name>[a-zA-Z_]+)/', views.userlist, name='userlist'),
    url(r'^room/(?P<room_name>[a-zA-Z_]+)/', views.room, name='room'),
]
