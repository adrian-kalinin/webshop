from django.views import generic
from django.shortcuts import reverse

from .forms import RegistrationForm


class RegistrationView(generic.CreateView):
    template_name = 'accounts/registration.html'
    form_class = RegistrationForm

    def get_success_url(self):
        return reverse('catalogue:list')
