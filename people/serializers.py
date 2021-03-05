import datetime

from django.contrib.auth.models import Group, User

from rest_framework import serializers

from .models import Audio, Image, Story, Video


class UserSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='get_full_name', required=False)
    username = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True, required=False)
    
    class Meta:
        model = User
        fields = ['pk', 'url', 'username', 'email', 'password', 'first_name', 'last_name', 'name', 'groups', 'is_staff']
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Group
        fields = ['pk', 'url']


class StorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Story
        fields = ['pk', 'story']


class ImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Image
        fields = ['pk', 'image']


class VideoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Video
        fields = ['pk', 'video']


class AudioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Audio
        fields = ['pk', 'audio']


# class PerformanceReviewFileUploadSerializer(serializers.HyperlinkedModelSerializer):
#     signed_position_description = serializers.FileField()

#     class Meta:
#         model = PerformanceReview
#         fields = [
#             'url', 'signed_position_description'
#         ]


# class FileUploadSerializer(serializers.Serializer):
#     file_upload = serializers.FileField()

#     class Meta:
#         fields = ['file_upload']
