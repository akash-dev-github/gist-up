from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^api/accounts/', include('login.urls')),
    url(r'^api_v1/', include('v1_apis.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^api/docs/', include('rest_framework_swagger.urls')),
]
