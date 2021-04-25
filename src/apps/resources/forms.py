from django import forms

from . import models


class RedirectForm(forms.ModelForm):

    class Meta:
        model = models.Redirect
        fields = ['key', 'url', 'active']