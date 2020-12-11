from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
User = get_user_model()
class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ('username',)

class ResumeSerializer(serializers.ModelSerializer):
    task = TaskSerializer(required=False)
    user = UserSerializer(required=False)
    class Meta:
        model = Resume
        fields = ('name','motivation','user','task')

class ResumeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeImage
        fields = ['image']