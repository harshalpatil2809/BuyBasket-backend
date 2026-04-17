from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken # Ye zaroori hai

class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Agar valid nahi hai, toh 400 error aayega na ki 500
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLogin(TokenObtainPairView):
    # SimpleJWT khud hi handle kar lega email login 
    # agar models.py mein USERNAME_FIELD = 'email' hai.
    pass

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # request.user mein logged-in user ka data hota hai
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class UserLogout(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            # Frontend se refresh token bhejna padega logout ke waqt
            refresh_token = request.data.get("refresh")
            token = RefreshToken(refresh_token)
            token.blacklist() # Token ko invalidate kar deta hai (Security!)
            return Response({"message": "Successfully logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Invalid token or already logged out"}, status=status.HTTP_400_BAD_REQUEST)