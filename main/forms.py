from django import forms
from django.forms import BooleanField

from main.models import Mailing, Client, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['owner', ]


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['owner', ]


class MailingManagerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['is_active', ]


class SuperUserMailingForm(StyleFormMixin, forms.ModelForm):
    clients = forms.ModelMultipleChoiceField(label="Клиенты",
                                             queryset=Client.objects.all(),
                                             widget=forms.CheckboxSelectMultiple(
                                                 attrs={'class': 'form-check-input'}
                                             ))

    class Meta:
        model = Mailing
        fields = ['name',
                  'message',
                  'date_time',
                  'period',
                  'status',
                  'clients',
                  'start',
                  'finish',
                  'is_active',
                  'next_sending_time']
