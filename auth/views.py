from django.shortcuts import render
from django.contrib.auth.views import (
    LoginView,
    LogoutView as Logout
)
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from auth import forms
from django.contrib.auth import login
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

class Login(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True


class Signup(View):
    def get(self, request):
        context = {
            'form' : forms.SignUpForm(),
        }
        return render(request, 'auth/signup.html', context)

    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            next = request.GET.get('next', '/blog')
            user=form.save()
            login(request, user)
            return HttpResponseRedirect(next)

        context = {
            'form' : form,
        }
        return render(request, 'auth/signup.html', context)
