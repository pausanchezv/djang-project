from django.http import HttpResponseRedirect
from django.urls import reverse


def base_redirect(request):
    """ Redirect to main page """
    return HttpResponseRedirect(reverse('home:home'))