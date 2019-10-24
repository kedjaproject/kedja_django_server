from django import forms

from walls import models


class MembershipForm(forms.ModelForm):

    class Meta:
        model = models.WallMembership
        widgets = {
            'roles': forms.CheckboxSelectMultiple()
        }
        exclude = []
