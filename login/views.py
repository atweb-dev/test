from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login
# Create your views here.


class LogInForm(forms.Form):
    name = forms.CharField(label='Username', min_length=4, max_length=14)
    psw = forms.CharField(widget=forms.PasswordInput,
                          label='Password', min_length=4, max_length=14)


def lgn(request):
    if request.user.is_authenticated:
        if request.user.is_staff is True:
            return HttpResponseRedirect('/admin/')
        else:
            return HttpResponseRedirect('/message/')
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            p = form.cleaned_data['psw']
            user = authenticate(username=n, password=p)
            if user is not None:
                login(request, user)
                if user.is_staff is True:
                    return HttpResponseRedirect('/admin/')
                else:
                    return HttpResponseRedirect('/message/')
            else:
                return render(request, 'error.html')
    else:
        form = LogInForm()
    return render(request, 'login.html', {'form': form})
