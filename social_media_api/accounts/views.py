from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):

    try:
        user_to_follow = User.objects.get(id=user_id)

        request.user.following.add(user_to_follow)

        return Response({"message": "User followed successfully"})

    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):

    try:
        user_to_unfollow = User.objects.get(id=user_id)

        request.user.following.remove(user_to_unfollow)

        return Response({"message": "User unfollowed successfully"})

    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
    
    
class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        token = Token.objects.get(user=user)

        return Response({
            "user": serializer.data,
            "token": token.key
        })


from rest_framework.views import APIView
from rest_framework import status


class LoginView(APIView):

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "token": token.key
            })

        return Response(
            {"error": "Invalid credentials"},
            status=status.HTTP_400_BAD_REQUEST
        )