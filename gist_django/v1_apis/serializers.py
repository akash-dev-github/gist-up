from rest_framework import serializers
from v1_apis.models import Article, Reader, Reaction


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article


class ReaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reader


class ReactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reaction


