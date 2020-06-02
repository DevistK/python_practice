from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .forms import RegisterFrom, LoginFrom
from .models import Fcuser


# Create your views here.


def index(request):
    return render(request, 'index.html', {'email': request.session.get('user')})


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterFrom
    success_url = '/'

    def form_valid(self, form):
        fcuser = Fcuser(
            email=form.data.get('email'),
            password=make_password(form.data.get('password')),
            level='user'
        )
        fcuser.save()

        return super().form_valid(form)

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginFrom
    success_url = '/'

    def form_valid(self, form):  # 로그인이 정상적으로 이루어졌을때 세션에 등록한다.
        self.request.session['user'] = form.data.get('email')
        return super().form_valid(form)

def logout(request):
    if 'user' in request.session:
        del(request.session['user'])
    return redirect('/')