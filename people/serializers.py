import datetime

from django.contrib.auth.models import Group, User

from rest_framework import serializers

from .models import Image, Story


class UserSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source='get_full_name')
    
    class Meta:
        model = User
        fields = ['pk', 'url', 'username', 'email', 'name', 'groups', 'is_staff']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Group
        fields = ['pk', 'url']


class ImageSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Image
        fields = ['pk', 'image']

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
