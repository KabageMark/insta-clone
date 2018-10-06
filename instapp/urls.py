from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    url('^$',views.Posts,name = 'index'),
    url(r'^new/post$', views.NewPost, name='new-post'),
    url(r'^new/update$', views.Update, name='new-update')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)