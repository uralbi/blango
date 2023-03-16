from rest_framework import generics
from blog.api.permissions import AuthorModifyOrReadOnly, IsAdminUserForObject

from blog.api.srzs import PostSerializer
from blog.models import Post


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
    serializer_class = PostSerializer
