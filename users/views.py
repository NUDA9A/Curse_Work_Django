import random

from django.contrib.auth.views import LoginView as BaseLoginView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


# Create your views here.


class UsersListView(ListView):
    model = User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        verify_code = ''.join([str(random.randint(0, 9)) for i in range(6)])
        user.verification_code = verify_code
        user.save()
        link = f"http://{self.request.get_host()}/users/register/confirm/{verify_code}/"
        message = f"Для подтверждения регистрации перейдите по ссылке: {link}"
        send_mail(
            "Регистрация",
            message,
            EMAIL_HOST_USER,
            [user.email],
            False
        )

        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('main:index')

    def get_object(self, queryset=None):
        return self.request.user


def verify_user(request, verify_code):
    for user in User.objects.all():
        if user.verification_code == verify_code:
            user.is_active = True
            user.save()
    return redirect(reverse_lazy('users:login'))


class LoginView(BaseLoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('main:index')


class UserManagerView(UpdateView):
    model = User
    fields = ['is_active', ]
    success_url = reverse_lazy('users:users_list')
