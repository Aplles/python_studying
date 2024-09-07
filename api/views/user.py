from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.views import View
from service_objects.services import ServiceOutcome

from api.services.user.create import UserCreateService
from api.services.user.login import UserLoginService
from models_app.models import Page


def logout_user(request):
    """Log out"""
    logout(request)
    return redirect('index')


class UserLoginView(View):

    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(UserLoginService, request.POST)
        login(request, outcome.result)
        return redirect("index")


class UserRenderCreateView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'create_user.html')

    def post(self, request, *args, **kwargs):
        outcome = ServiceOutcome(UserCreateService, kwargs)
        return render(request, 'create_user.html', context={
            'username': outcome.result['username'],
            'password': outcome.result['password']
        })
