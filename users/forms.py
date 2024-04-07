
from django import forms

from allauth.utils import (
    set_form_field_order,
)
from allauth.account.forms import  SignupForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.utils.translation import gettext_lazy as _

from users.models import Profile


class ExtendedSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(ExtendedSignupForm, self).__init__(*args, **kwargs)
        self.fields["first_name"] = forms.CharField(
            label=_("Fist Name"),
            max_length=255,
            widget=forms.TextInput(
                attrs={"placeholder": _("Fist Name"), "autocomplete": "Fist Name"}
            ),
        )

        self.fields["last_name"] = forms.CharField(
            label=_("Last Name"),
            max_length=255,
            widget=forms.TextInput(
                attrs={"placeholder": _("Last Name"), "autocomplete": "Fist Name"}
            ),
        )
        self.fields["resume"] = forms.FileField(
            label=_("Resume"), required=False
        )
        self.fields["newsletter"] = forms.BooleanField(
            label=_("Newsletter"), required=False
        )


        if hasattr(self, "field_order"):
            set_form_field_order(self, self.field_order)

    field_order = [
        "email",
        'first_name',
        'last_name',
        "password",
        "resume",
        "newsletter",
    ]




class StepOneForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['experience_sector', 'year_sector', 'country_experience', 'highest_degree']

class StepTwoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['language', 'gender', 'citizenship']
