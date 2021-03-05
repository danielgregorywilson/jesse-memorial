from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model

from people.models import Audio, Image, Story, Video
from people.serializers import (
    AudioSerializer, ImageSerializer, StorySerializer, UserSerializer,
    VideoSerializer
)


class RegisterView(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer


class UploadImageView(CreateAPIView):
    model = Image
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ImageSerializer


class UploadStoryView(CreateAPIView):
    model = Story
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StorySerializer


class UploadVideoView(CreateAPIView):
    model = Video
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VideoSerializer


class UploadAudioView(CreateAPIView):
    model = Audio
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AudioSerializer