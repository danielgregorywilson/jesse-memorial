import datetime

from django.db import models
from django.utils.translation import gettext as _


class Memory(models.Model):
    class Meta:
        abstract = True

    uploaded_by = models.ForeignKey("auth.User", verbose_name=_("uploaded by"), on_delete=models.CASCADE)
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
    approved = models.BooleanField(default=False)


class Story(Memory):
    class Meta:
        verbose_name = _("Story")
        verbose_name_plural = _("Stories")

    story = models.TextField(blank=True, null=True)


class Image(Memory):
    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    image = models.ImageField(upload_to="uploads/images")


class Video(Memory):
    class Meta:
        verbose_name = _("Video")
        verbose_name_plural = _("Videos")

    video = models.FileField(upload_to="uploads/videos")


class Audio(Memory):
    class Meta:
        verbose_name = _("Audio")
        verbose_name_plural = _("Audios")

    audio = models.FileField(upload_to="uploads/audio")


# class PerformanceReview(models.Model):
#     signed_position_description = models.FileField(_("signed position description"), upload_to="uploads/signed-position-descriptions", blank=True, null=True)