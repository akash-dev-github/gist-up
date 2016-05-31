from django.conf.urls import url
import views

urlpatterns = [
    url(r'^api/sign_in$', views.sign_in, name='sign_in'),
    url(r'^api/sign_up$', views.sign_up, name='sign_up'),
    url(r'^logout$', views.logout_view, name='logout'),
]
