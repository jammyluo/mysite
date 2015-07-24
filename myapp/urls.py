from django.conf.urls import *
from myapp.views import list_posts

 
urlpatterns = patterns('',
                      url(r'^list_posts',list_posts),
                      )