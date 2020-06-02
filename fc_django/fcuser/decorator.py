from django.shortcuts import redirect
from .models import Fcuser

def login_requerid(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        return function(request, *args, **kwargs)

    return wrap

def admin_requerid(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')

        user = Fcuser.objects.get(email=user)

        if user.level != 'admin':
            return redirect('/login')

        return function(request, *args, **kwargs)

    return wrap