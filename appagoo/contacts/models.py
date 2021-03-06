from django import forms
from django.forms.widgets import *
from django.core.mail import send_mail, BadHeaderError

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    topic = forms.CharField()
    message = forms.CharField(widget=Textarea())