from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, get_user_model
from .serializers import UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated

CustomUser = get_user_model()


# REGISTER VIEW
class RegisterView(generics.GenericAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            token = Token.objects.get(user=user)

            return Response({
                "user": serializer.data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# LOGIN VIEW
class LoginView(generics.GenericAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]

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


# FOLLOW USER
class FollowUserView(generics.GenericAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):

        try:

            user_to_follow = CustomUser.objects.get(id=user_id)

            request.user.following.add(user_to_follow)

            return Response({"message": "User followed successfully"})

        except CustomUser.DoesNotExist:

            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )


# UNFOLLOW USER
class UnfollowUserView(generics.GenericAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):

        try:

            user_to_unfollow = CustomUser.objects.get(id=user_id)

            request.user.following.remove(user_to_unfollow)

            return Response({"message": "User unfollowed successfully"})

        except CustomUser.DoesNotExist:

            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )