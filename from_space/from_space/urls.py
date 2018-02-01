from django.conf.urls import include, url
from django.contrib import admin
from .views import index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^api/', include('api_messages.urls')),
    url(r'^admin/', admin.site.urls),
]
