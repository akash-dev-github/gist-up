from django.contrib import admin
from v1_apis.models import Article, Reaction, Reader

admin.site.register(Article)
admin.site.register(Reaction)
admin.site.register(Reader)