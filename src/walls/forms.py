from django import forms

from walls import models


class RoleForm(forms.ModelForm):

    class Meta:
        model = models.WallRole
        widgets = {
            'roles': forms.CheckboxSelectMultiple()
        }
        exclude = []
