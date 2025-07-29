# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Houses(models.Model):

    #__Houses_FIELDS__
    id = models.TextField(max_length=255, null=True, blank=True)
    number = models.TextField(max_length=255, null=True, blank=True)
    rooftype = models.ForeignKey(roofs, on_delete=models.CASCADE)

    #__Houses_FIELDS__END

    class Meta:
        verbose_name        = _("Houses")
        verbose_name_plural = _("Houses")


class Roofs(models.Model):

    #__Roofs_FIELDS__
    id = models.BooleanField()
    rooftype = models.ForeignKey(houses, on_delete=models.CASCADE)

    #__Roofs_FIELDS__END

    class Meta:
        verbose_name        = _("Roofs")
        verbose_name_plural = _("Roofs")



#__MODELS__END
