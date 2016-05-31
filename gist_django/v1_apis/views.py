from rest_framework import generics

from v1_apis.models import Article, Reaction, Reader

from v1_apis.serializers import ArticleSerializer, ReactionSerializer, ReaderSerializer


# ############### Article APIs ############################


class CreateArticle(generics.ListCreateAPIView):
    """
        Create a new Article row.
    """
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)


class ModifyArticle(generics.RetrieveUpdateDestroyAPIView):
    """
        RUD Article
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = (permissions.IsAuthenticated,)


# ############### Reaction APIs ############################


class CreateReaction(generics.ListCreateAPIView):
    """
        Create a new Reaction row.
    """
    serializer_class = ReactionSerializer
    queryset = Reaction.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)


class ModifyReaction(generics.RetrieveUpdateDestroyAPIView):
    """
        RUD Reaction
    """
    queryset = Reaction.objects.all()
    serializer_class = ReactionSerializer
    # permission_classes = (permissions.IsAuthenticated,)


# ############### Reader APIs ############################


class CreateReader(generics.ListCreateAPIView):
    """
        Create a new Reader row.
    """
    serializer_class = ReaderSerializer
    queryset = Reader.objects.all()
    # permission_classes = (permissions.IsAuthenticated,)


class ModifyReader(generics.RetrieveUpdateDestroyAPIView):
    """
        RUD Reader
    """
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializer
    # permission_classes = (permissions.IsAuthenticated,)
