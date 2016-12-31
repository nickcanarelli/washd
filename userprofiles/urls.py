from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^my-laundry/', views.logged_in, name='client-laundry'),
    url(r'^profile/', views.profile, name='client-profile'),
    url(r'^editprofile/', views.update_profile, name='client-profile-edit'),
]
