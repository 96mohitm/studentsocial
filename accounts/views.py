# from django.contrib.auth import login, logout
# from django.core.urlresolvers import reverse_lazy
# from django.views.generic import CreateView
#
# from . import forms
#
# class SignUp(CreateView):
#     form_class = forms.UserCreateForm
#     success_url = reverse_lazy("login")
#     template_name = "accounts/signup.html"

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# from django.http import HttpResponse
from .forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from .models import User_detail
from django import forms
# Create your views here.
#



# form form for registeration
def toRegister(request):
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)

            # sets one to one relation
            profile.user = user

            if 'profile_pic' in request.FILES:
                # same syntax for uplaoding any kind of file
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = Trueprofile_form = UserProfileForm()
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'accounts/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered,
    })