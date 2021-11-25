from django import forms
from .models import StateChoices
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(label=_('Username'))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    # Required fields
    username = forms.CharField(label=_('Username'))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput())
    password_check = forms.CharField(label=_('Repeat your password'), widget=forms.PasswordInput())
    email = forms.EmailField(label=_('E-mail'))

    # Optional fields
    first_name = forms.CharField(label=_('First name'), required=False)
    last_name = forms.CharField(label=_('Last name'), required=False)


class NewEventForm(forms.Form):
    title = forms.CharField(label=_('Title'), widget=forms.TextInput(attrs={'class': 'input-group-text mb-3'}))
    description = forms.CharField(label=_('Description'), widget=forms.TextInput(attrs={'class': 'comment-area'}))
    date = forms.DateField(
        label=_('Date'),
        widget=forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),
    )
    state = forms.ChoiceField(label=_('Event state'), choices=StateChoices.states())


class SubscriptionForm(forms.Form):
    comment = forms.CharField(label=_('Write your comment'), widget=forms.Textarea(attrs={'style': 'resize: none;'}))
