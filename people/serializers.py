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
        fields = ['pk', 'story', 'title', 'description', 'date']

    def create(self, validated_data):
        story = Story.objects.create(
            story=validated_data['story'],
            uploaded_by=self.context['request'].user,
            title=validated_data.get('title', ''),
            description=validated_data.get('description', ''),
        )
        if 'date' in validated_data:
            story.date = validated_data['date']
            story.save()
        return story


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    date = serializers.DateField(required=False)

    class Meta:
        model = Image
        fields = ['pk', 'image', 'title', 'description', 'date']
    
    def create(self, validated_data):
        image = Image.objects.create(
            image=validated_data['image'],
            uploaded_by=self.context['request'].user,
            title=validated_data.get('title', ''),
            description=validated_data.get('description', ''),
        )
        if 'date' in validated_data:
            image.date = validated_data['date']
            image.save()
        return image


class VideoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Video
        fields = ['pk', 'video', 'title', 'description', 'date']
    
    def create(self, validated_data):
        video = Video.objects.create(
            video=validated_data['video'],
            uploaded_by=self.context['request'].user,
            title=validated_data.get('title', ''),
            description=validated_data.get('description', ''),
        )
        if 'date' in validated_data:
            video.date = validated_data['date']
            video.save()
        return video


class AudioSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Audio
        fields = ['pk', 'audio', 'title', 'description', 'date']

    def create(self, validated_data):
        audio = Audio.objects.create(
            audio=validated_data['audio'],
            uploaded_by=self.context['request'].user,
            title=validated_data.get('title', ''),
            description=validated_data.get('description', ''),
        )
        if 'date' in validated_data:
            audio.date = validated_data['date']
            audio.save()
        return audio


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
