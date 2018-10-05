from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'index'),
    url(r'^new/post$', views.NewPost, name='new-post')
]