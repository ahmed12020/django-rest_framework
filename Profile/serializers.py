from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    urls = serializers.HyperlinkedIdentityField(view_name='accounts:profiledetail')
    class Meta:
        model = Profile
        fields =['urls', 'name', 'title' , 'content' , 'email', 'datetime', 'url', 'slug' ]



class ProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =['name', 'title' , 'content' , 'email', 'datetime', 'url', 'slug' ]



class ProfileSerializerAPIViw(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields =['name', 'title' , 'content' , 'email', 'datetime', 'url', 'slug' ]