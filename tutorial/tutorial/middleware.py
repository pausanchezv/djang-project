from django.http import HttpResponseRedirect
from django.urls import reverse
import re


from tutorial import settings


class LoginRedirectMiddleware(object):
    """ Login redirections """

    def __init__(self, get_response):
        """ Middleware Constructor """
        self.get_response = get_response

    def __call__(self, request):
        """ Middleware callable """
        response = self.get_response(request)
        return response

    @staticmethod
    def process_view(request, view_func, view_args, view_kwargs):
        """ Before accessing view functions """

        assert hasattr(request, 'user')  # user exist?

        current_url = request.path_info.lstrip('/')
        is_session_active = request.user.is_authenticated()

        compiled_private_when_logged_in = map(lambda url: re.compile(url), settings.PRIVATE_URLS_IF_LOGGED_IN)
        compiled_private_when_logged_out = map(lambda url: re.compile(url), settings.PRIVATE_URLS_IF_LOGGED_OUT)

        is_private_when_logged_in = any(url.match(current_url) for url in compiled_private_when_logged_in)
        is_private_when_logged_out = any(url.match(current_url) for url in compiled_private_when_logged_out)

        if is_session_active and is_private_when_logged_in:
            return HttpResponseRedirect(reverse('accounts:profile'))

        elif not is_session_active and is_private_when_logged_out:
            return HttpResponseRedirect(reverse('accounts:login'))

        return None

