from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User 
from django.urls import reverse_lazy, reverse
from accounts.models import Employee
from ACCNTS.models import Invoice
from django.views.generic import (ListView,
                                  DeleteView,
                                  UpdateView,
                                  CreateView,
                                  DetailView)
from easy_pdf.rendering import render_to_pdf_response
from ACCNTS.forms import PaymentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
def dashboard(request):
    current = User.objects.get(username = request.session['username'])
    employee = Employee.objects.get(user = current.id)
    return render(request, "accnts/dashboard.html", {"employee": employee })

# profoma invoice Views
class CreateInvoiceView(CreateView):
    model = Invoice
    fields = ('member', 'description', 'VAT')
    template_name = "accnts/invoice/invoice_form.html"
    def get_context_data(self, **kwargs):
        context = super(CreateInvoiceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=self.request.user.id)
        return context

class ListInvoiceView(ListView):
    model = Invoice
    context_object_name = "profomas"
    template_name = "accnts/invoice/invoice_list.html"
    def get_context_data(self, **kwargs):
        context = super(ListInvoiceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=self.request.user.id)
        return context

class UpdateInvoiceView(UpdateView):
    model = Invoice
    fields = ('member', 'description', 'VAT')
    template_name = "accnts/invoice/invoice_form.html"
    def get_context_data(self, **kwargs):
        context = super(UpdateInvoiceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=self.request.user.id)
        return context

class DeleteInvoiceView(DeleteView):
    model = Invoice
    template_name = "accnts/invoice/invoice_delete.html"
    success_url = reverse_lazy("ACCNTS:list_profoma")
    def get_context_data(self, **kwargs):
        context = super(DeleteInvoiceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=self.request.user.id)
        return context

class DetailInvoiceView(DetailView):
    model = Invoice
    context_object_name = "profoma"
    template_name = "accnts/invoice/invoice_detail.html"
    def get_context_data(self, **kwargs):
        context = super(DetailInvoiceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=self.request.user.id)
        return context

def print_profoma(request, pk):
    profoma = Invoice.objects.get(id = pk)
    category = int(profoma.member.category)
    tax = 0;
    if profoma.VAT == "Yes":tax = 0.16
    else:tax = 0
    total_tax = (tax * category)
    balance = (category + total_tax)
    return render_to_pdf_response(request, "accnts/invoice/profoma.html",
                                  {'profoma': profoma,
                                   'total_tax': total_tax, 'tax':tax,
                                   'balance': balance,})

'''
So
'''
def make_payment(request, pk):
    employee = Employee.objects.get(user= User.objects.get(username = request.session['username']).id)
    form = PaymentForm(request.POST or None,
                    instance = get_object_or_404(Invoice, pk=pk))
    invoice = Invoice.objects.get(id=pk)
    balance = invoice.balance
    if request.method == "POST":
        if form.is_valid():
            form.save()
            amount = form.cleaned_data['amount']
            invoice.amount = amount
            print("Amount:" + str(amount))
            invoice.balance = (int(invoice.member.category) - int(invoice.amount))
            invoice.save()
            print("new balance: " + str(invoice.balance))
            return HttpResponseRedirect(reverse("ACCNTS:list_profoma"))
    return render(request, "accnts/invoice/payment.html",
                  {'form': form,
                   'balance': balance,
                   'employee': employee})


def print_invoice(request, pk):
    invoice = Invoice.objects.get(id = pk)
    category = int(invoice.member.category)
    tax = 0;
    if invoice.VAT == "Yes":tax = 0.16
    else:tax = 0
    total_tax = (tax * category)
    total_paid = invoice.amount
    balance = (total_tax + category)
    total_balance = ((total_tax + category) - total_paid)
    return render_to_pdf_response(request, "accnts/invoice/invoice.html",
                                  {'invoice': invoice,
                                   'total_tax': total_tax,
                                   'tax':tax,
                                   'balance': balance,
                                   'total_balance': total_balance,
                                   'total_paid': total_paid, })

'''
List All invoices
'''

def list_invoices(request):
    invoices = Invoice.objects.all()
    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    return render(request, "accnts/invoice/list_all_invoices.html",
                  {'invoices': invoices, "employee": employee,})
