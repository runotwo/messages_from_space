from django.conf.urls import url
from .views import get_messages, mark_read

urlpatterns = [
    url(r'^get_messages', get_messages, name='get_messages'),
    url(r'^mark_read', mark_read, name='mark_read')
]
