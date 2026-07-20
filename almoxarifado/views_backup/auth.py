from django.shortcuts import redirect

from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


class MeuLoginView(LoginView):

    template_name = 'almoxarifado/login.html'


def logout_view(request):

    logout(request)

    return redirect('/login/')