from rest_framework import serializers
from users.models import User
#from users.backend import authenticate
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_str, smart_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import send_normal_email

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length = 68, min_length=6, style={'input_type':'password'}, write_only = True)
    password2 = serializers.CharField(max_length = 68, min_length=6, style={'input_type':'password'},write_only = True)
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number','password','password2')
    
    def validate(self, attrs):
        password = attrs.get('password','')
        password2 = attrs.get('password','')
        if password != password2:
            raise serializers.ValidationError({"password":"Passwords must match"})
        return attrs
    
    def create(self,validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True,style={'input_type':'password'})
    full_name = serializers.CharField(max_length=255,read_only=True)
    access_token = serializers.CharField(max_length=255,read_only=True)
    refresh_token = serializers.CharField(max_length=255,read_only=True)
    
    class Meta:
        model = User
        fields = ['email', 'password', 'full_name', 'access_token', 'refresh_token']
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        print(f"Password is: {password}")
        request = self.context.get('request')
        print(f"Attempting to authenticate user with email: {email}")
        user = authenticate(request, email=email, password=password)
        #user = authenticate(request, username=email, password=password)
        print(f"User is: {user}")
        if not user:
            print("Authentication failed")
            raise serializers.ValidationError({'password': 'Invalid credentials'})
        if not user.is_active:
            print("User account is disabled")
            raise serializers.ValidationError({'error': 'Account disabled'})
        print("Authentication successful")
        user_token = user.tokens()
        return {
            'email': user.email,
            'full_name': user.full_name,
            'access_token': str(user_token.get('access')),
            'refresh_token': str(user_token.get('refresh'))
        }

class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, min_length=3)

    class Meta:
        model = User
        fields = ['email']
    def validate(self,attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb6 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            request = self.context.get('request')
            site_domain = get_current_site(request).domain
            relative_link = reverse('users:password_reset_confirm', kwargs={'uidb6': uidb6, 'token': token})
            abslink= 'http://'+site_domain+relative_link
            email_body = f"You are receiving this email because you requested a password reset for your account.\n {abslink}"
            data = {
                'email_body': email_body,
                'to_email': user.email,
            'subject': 'Reset your password'
            }
            send_normal_email(data)
    