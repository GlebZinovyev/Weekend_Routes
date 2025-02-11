from django.shortcuts import render
# Импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView
from django.contrib.auth import logout
from django.http import HttpResponse

# Функция reverse_lazy позволяет получить URL по параметрам функции path()
# Берём, тоже пригодится
from django.urls import reverse_lazy

# Импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm

class SignUp(CreateView):
    form_class = CreationForm
    # После успешной регистрации перенаправляем пользователя на главную.
    success_url = reverse_lazy('index')
    template_name = 'users/signup.html' 


def logout_view(request):
    logout(request)
    return HttpResponse("Here's the text of the web page.")