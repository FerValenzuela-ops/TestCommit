from django.contrib.auth.models import User
from django.db.models.base import Model
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer) :
    
    class Meta : 
        Model = User
        fields = ['url', 'username', 'email']
