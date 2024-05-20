from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from accounts.serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.response import Response 
from rest_framework import status
from accounts.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated

class RegisterUserView(GenericAPIView):
    serializer_class = UserRegisterSerializer
    def post(self,request):
        user_data = request.data 
        serializer = self.serializer_class(data=user_data)
        if serializer.is_valid(raise_exception=True):
            password = serializer.validated_data['password']
            if User.objects.filter(email = serializer.validated_data['email']).exists():
                return Response({'error': 'Email already exists'}, status = status.HTTP_400_BAD_REQUEST)
            #serializer.validated_data['password'] = make_password(password)
            serializer.save()
            user = serializer.data
            return Response({
                'data': user,
                'message': f'Hi, thank you for registering with us!'
            },status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class LoginUserView(GenericAPIView):
    serializer_class =  UserLoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    '''
class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            print("Valid data:", serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        print("Invalid data:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)'''
    
class TestAuthentication(GenericAPIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user_id = request.user.user_id
        return Response({'message': 'You are authenticated', 'user_id': user_id}, status=status.HTTP_200_OK)