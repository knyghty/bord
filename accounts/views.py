from registration.backends.simple.views import RegistrationView

from .forms import UserCreationForm


class RegistrationView(RegistrationView):
    form_class = UserCreationForm
