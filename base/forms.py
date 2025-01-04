from django.forms import ModelForm
from .models import Room,About
from django.contrib.auth.models import User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host','participants']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class AboutForm(ModelForm):
    class Meta:
        model = About
        fields = ['about']
