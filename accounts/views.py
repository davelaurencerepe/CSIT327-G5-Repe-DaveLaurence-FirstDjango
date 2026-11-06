from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    success_message = "Account created! You can now log in."


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    fields = ["first_name", "last_name", "email", "course"]
    template_name = "registration/profile.html"
    success_url = reverse_lazy("dashboard")
    success_message = "Profile updated."

    def get_object(self, queryset=None):
        return self.request.user