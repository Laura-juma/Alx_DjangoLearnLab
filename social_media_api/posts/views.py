from rest_framework import viewsets, permissions, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# POST VIEWSET
class PostViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all().order_by('-created_at')

    serializer_class = PostSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):

        serializer.save(author=self.request.user)


# COMMENT VIEWSET
class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all().order_by('-created_at')

    serializer_class = CommentSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):

        serializer.save(author=self.request.user)


# FEED VIEW 
@permission_classes([permissions.IsAuthenticated])
def feed(request):

    following_users = request.user.following.all()

   
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)