#middleware to redirect user to login if  not logged in
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
class RedirectUnAthorizedUsers:
    def process_request(self, request):
        if not self.request.user.is_authenticated():
            return HttpResponseRedirect(reverse('accounts:login'))
        return None

# Expiry Session
class SessionExpiredMiddleware:
    def process_request(request):
        last_activity = request.session['last_activity']
        now = datetime.now()

        if (now - last_activity).minutes > 10:
            # Do logout / expire session
            # and then...
            return HttpResponseRedirect("accounts:login")

        if not request.is_ajax():
            # don't set this for ajax requests or else your
            # expired session checks will keep the session from
            # expiring :)
            request.session['last_activity'] = now
