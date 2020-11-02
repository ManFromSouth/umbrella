from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
# Вьюха для регистрации
class register_request(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# Вьюха для логина
# def login_request(request):
#     data = request.POST
#
