from dataclasses import fields
from pyexpat import model
from urllib import request
from django import forms

import agents
from .models import Agent, Lead
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

User = get_user_model()

class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'age',
            'organization',
            'agent',
        )

class LeadForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField(min_value=0)
    
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

class AssignAgentForm(forms.Form):
    # agent = forms.ChoiceField(choices=[(
    #     ('Agent1', "Agent 1"),
    #     ('Agent2', "Agent 2")
    # )])
    agent = forms.ModelChoiceField(
        queryset=Agent.objects.none()
    )

    def __init__(self, *args, **kwargs) -> None:
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organization=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents

class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )