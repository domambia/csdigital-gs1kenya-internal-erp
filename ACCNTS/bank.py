from ACCNTS.models import Payment
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


def list_invoice_payments(request):
    banks = Payment.objects.all()
