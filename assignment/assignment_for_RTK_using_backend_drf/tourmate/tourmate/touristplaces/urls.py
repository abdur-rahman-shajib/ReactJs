from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from touristplaces import views

urlpatterns = [
    url('touristplaces/', views.TouristPlaceList.as_view()),
    url('projects/', views.ProjectList.as_view()),
    url('techstack/', views.TechStackList.as_view()),
    url(r'touristplace_detail/(?P<pk>\d+)/', views.TouristPlaceDetail.as_view()),
    url('users/', views.UserList.as_view()),
    url(r'user_detail/(?P<pk>\d+)/', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)