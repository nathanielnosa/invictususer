from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Profile

# user serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email']

# profile serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSerializer()
        fields = ['fullname','username','email','phone','gender','profile_pix','bio']

# registration serializer
class RegistrationSerializer(serializers.ModelSerializer):
    username= serializers.CharField(write_only=True)
    password1=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    
    class Meta:
        model = Profile
        fields = ['fullname',"username","password1","password2",'email','phone','gender','profile_pix','bio']

    # validate
    def validate(self,data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Password fields didn't match.")
        return data
    # validate email
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value
    # create user and profile together
    def create(self,validated_data):
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        password = validated_data.pop('password1')

        user = User.objects.create_user(username=username,email=email,password=password)
        profile = Profile.objects.create(
            user=user,
            fullname=validated_data['fullname'],
            phone=validated_data['phone'],
            gender=validated_data['gender'],
            profile_pix=validated_data['profile_pix'],
            bio=validated_data['bio']
            )
        # function to send email
        return profile