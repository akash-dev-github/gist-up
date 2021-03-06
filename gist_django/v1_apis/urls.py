from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import CreateArticle, ModifyArticle, CreateReader, ModifyReader, \
    CreateReaction, ModifyReaction

urlpatterns = [

    # article APIs
    url(r'^article$', csrf_exempt(CreateArticle.as_view())),
    url(r'^article/(?P<pk>\w+)$', ModifyArticle.as_view()),

    # reader APIs
    url(r'^reader$', CreateReader.as_view()),
    url(r'^reader/(?P<pk>\w+)$', ModifyReader.as_view()),

    # reaction APIs
    url(r'^reaction$', CreateReaction.as_view()),
    url(r'^reaction/(?P<pk>\w+)$', ModifyReaction.as_view()),
]
