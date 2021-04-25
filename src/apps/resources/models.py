import tempfile
from datetime import datetime

from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_save


from django.db import models


class Redirect(models.Model):
    key = models.CharField(unique=True, max_length=250)
    url = models.URLField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.key}: {self.url}"

    def get_redirect(self):
        return self.url

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        super(Redirect, self).save(*args, **kwargs)


@receiver(post_save, sender=Redirect)
def set_key(sender, created, instance, **kwargs):
    if instance.active and not created:
        cache.set(instance.key, instance.url, 10000)
