from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('touristplaces.urls')),
    url('auth', include('tourmateauth.urls')),
    url('api-auth/', include('rest_framework.urls')),
]

