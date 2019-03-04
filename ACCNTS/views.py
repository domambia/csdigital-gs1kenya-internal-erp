from django.shortcuts import render
from django.contrib.auth.models import User 
from django.urls import reverse_lazy
from accounts.models import Employee
from ACCNTS.models import Invoice
from django.views.generic import (ListView,
                                  DeleteView,
                                  UpdateView,
                                  CreateView,
                                  DetailView)
from easy_pdf.rendering import render_to_pdf_response



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
    return render_to_pdf_response(request, "accnts/invoice/profoma.html",{'name': "omambia"})

