from django.views import generic
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

from .forms import RegistrationForm


class RegistrationView(generic.CreateView):
    template_name = 'accounts/registration.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)

        return redirect('catalogue:list')
