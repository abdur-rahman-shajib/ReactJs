from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from tourmateauth import views


urlpatterns = [
    url('createuser/', views.CreateUser.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)