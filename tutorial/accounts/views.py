# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse

from accounts.forms import RegistrationForm, EditProfileForm

'''
def home(request):
    return render(request, 'accounts/home.html')
'''

def logout(request):
    """ Logout Session """
    auth.logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))


def register(request):
    """ Register user """

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('accounts:profile'))

    # method get or invalid form always redirect to the register page again
    form = RegistrationForm()
    args = {'form': form}
    return render(request, 'accounts/register.html', args)


#@login_required
def profile(request):
    """ Profile page """
    return render(request, 'accounts/profile.html')


def edit_profile(request):
    """ Edit Profile """

    if request.method == 'POST':

        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:profile'))

    # method get or invalid form always redirect to the same page again
    form = EditProfileForm(instance=request.user)
    args = {'form': form}
    return render(request, 'accounts/edit_profile.html', args)


def change_password(request):
    """ Edit Profile """

    if request.method == 'POST':

        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse('accounts:profile'))

    # method get or invalid form always redirect to the same page again
    form = PasswordChangeForm(user=request.user)
    args = {'form': form}
    return render(request, 'accounts/change_password.html', args)
