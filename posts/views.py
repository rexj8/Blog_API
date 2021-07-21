# VIEW - To render data into frontend, and handle requests from user, we need to create a view.

from rest_framework import generics
from rest_framework.filters import SearchFilter

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    ## -- For sorting
    # filter_backends = [OrderingFilter]
    # ordering_fields = ['created_at','id']

    ## -- For searching
    ##      ^ Starts with search(default)
    ##      @ Full text search
    ##      $ Regex search
    filter_backends = [SearchFilter]
    search_fields = ['id', 'title']
    # search_fields = ['id','=title']  ## title has to be match exactly

    print(queryset)
    print(serializer_class)


# class PostDetail(generics.RetrieveAPIView):
# if you go to http://localhost:8000/api/1/
# only operations allowed -> GET, HEAD, OPTIONS

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # but in this class if you go to http://localhost:8000/api/1/
    # operations allowed -> GET, PUT, PATCH, DELETE, HEAD, OPTIONS
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    print(queryset)
    print(serializer_class)


# A QuerySet is, in essence, a list of objects of a given Model. 
# QuerySets allow you to read the data from the database, filter it and order it.
# 

class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAdminUser]