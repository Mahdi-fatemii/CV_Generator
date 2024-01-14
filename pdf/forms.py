from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ("first_name", "last_name", "email", "phone",
                  "summary", "degree", "school", "university",
                  "previous_work", "skills")

