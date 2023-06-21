
from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm
from users.models import User

class LoginView(BaseLoginView):
    template_name = 'users/login.html'

class LogoutView(BaseLogoutView):
    pass

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("user:login")

    def form_valid(self, form):
        self.object = form.save()
        send_mail(
            subject="Поздравляем с регистрацией",
            message="Вы зарегистрировались на нашей платформе, добро пожаловать!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)

class UserUpdateView(UpdateView):
    model = User
    fields = ("email", "phone", "telegram", "avatar")
    success_url = reverse_lazy("catalog:index")

class UserPasswordView(UpdateView):
    model = User
    fields = ()
    template_name = 'users/user_password.html'
    success_url = reverse_lazy("user:login")

    def form_valid(self, form):
        self.object = form.save()
        new_password = User.objects.make_random_password()
        self.object.set_password(new_password)
        self.object.save(update_fields=['password'])
        send_mail(
            subject="Обновление пароля",
            message=f"Ваш новый пароль: {new_password}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)