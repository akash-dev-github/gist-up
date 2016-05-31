from django.conf.urls import url
from login.views import sign_in, sign_up, logout_view

urlpatterns = [
    url(r'^sign_in$', sign_in, name='sign_in'),
    url(r'^sign_up$', sign_up, name='sign_up'),
    url(r'^logout$', logout_view, name='logout'),
]
