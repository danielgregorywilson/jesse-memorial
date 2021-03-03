import datetime

from django.db import models
from django.utils.translation import gettext as _


class Upload(models.Model):
    class Meta:
        abstract = True

    uploaded_by = models.ForeignKey("auth.User", verbose_name=_("user"), on_delete=models.CASCADE)


class Story(Upload):
    class Meta:
        verbose_name = _("Story")
        verbose_name_plural = _("Stories")

    story = models.TextField(blank=True, null=True)


class Image(Upload):
    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    image = models.ImageField(upload_to="uploads/images")




# class PerformanceReview(models.Model):
#     signed_position_description = models.FileField(_("signed position description"), upload_to="uploads/signed-position-descriptions", blank=True, null=True)