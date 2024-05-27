
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = User.objects.create_user(**serializer.validated_data)
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        try:  
            user=authenticate(request,username=username,password=password)
            if user is not None:
                return Response({'message':'Login successfull!!'},status=status.HTTP_200_OK)
            else:
                return Response({'message':'Invalid credentials'},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
 
    