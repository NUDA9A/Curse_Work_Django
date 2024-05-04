import random
from main.services import get_cached_mailing_ammount, get_cached_mailing_active, get_cached_clients_ammount, \
    get_cached_blog_list

from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from main.forms import ClientForm, MessageForm, SuperUserMailingForm, MailingManagerForm, StyleFormMixin
from main.models import Mailing, Client, Message, Try


# Create your views here.

class HomePageView(ListView):
    model = Mailing
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['mailings_ammount'] = get_cached_mailing_ammount()
        context_data['active_mailings_ammount'] = get_cached_mailing_active()
        context_data['clients_ammount'] = get_cached_clients_ammount()
        blog_list = get_cached_blog_list()
        random.shuffle(blog_list)
        context_data['blog_list'] = blog_list[:3]
        return context_data


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing


def get_default_mailing_form(user):
    class MailingForm(StyleFormMixin, forms.ModelForm):
        clients = forms.ModelMultipleChoiceField(label="Клиенты",
                                                 queryset=Client.objects.filter(owner=user),
                                                 widget=forms.CheckboxSelectMultiple(
                                                     attrs={'class': 'form-check-input'}
                                                 ))

        class Meta:
            model = Mailing
            fields = ('name', 'message', 'start', 'finish', 'period', 'clients')

    return MailingForm


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    success_url = reverse_lazy('main:mailings')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return get_default_mailing_form(user)
        if user.is_superuser:
            return SuperUserMailingForm
        if user.has_perm('main.set_active'):
            return MailingManagerForm
        raise PermissionError


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('main:mailings')


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    success_url = reverse_lazy('main:mailings')

    def get_form_class(self):
        return get_default_mailing_form(self.request.user)

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        context = self.get_context_data()

        return super().form_valid(form)


class MessageListView(LoginRequiredMixin, ListView):
    model = Message


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('main:messages')


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('main:messages')


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('main:messages')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        context = self.get_context_data()

        return super().form_valid(form)


class ClientListView(LoginRequiredMixin, ListView):
    model = Client


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:clients')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('main:clients')


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('main:clients')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        context = self.get_context_data()

        return super().form_valid(form)


class TryListView(LoginRequiredMixin, ListView):
    model = Try
