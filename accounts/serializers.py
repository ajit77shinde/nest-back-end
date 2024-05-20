from rest_framework import serializers
from accounts.models import User
#from accounts.backend import authenticate
from django.contrib.auth import authenticate

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
    
    