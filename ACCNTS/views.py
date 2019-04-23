from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from accounts.models import Employee
from ACCNTS.models import Invoice, PayRoll, Payment, Deduction
from ERP import settings
from django.views.generic import (ListView,
                                  DeleteView,
                                  UpdateView,
                                  CreateView,
                                  DetailView)
from easy_pdf.rendering import render_to_pdf_response
from ACCNTS.forms import PaymentForm, PayRollForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from helpers.utils import render_to_pdf
from helpers.help import check_user_login
#imports for creating pdf

def dashboard(request):
    if not request.session.get('username'):
        messages.info(request, "Please login again.")
        return HttpResponseRedirect(reverse("accounts:login"))

    current = User.objects.get(username = request.session['username'])
    employee = Employee.objects.get(user = current.id)
    return render(request, "accnts/dashboard.html", {"employee": employee })

# profoma invoice Views
class CreateInvoiceView(SuccessMessageMixin, CreateView):
    model = Invoice
    success_message  = "Sucessfully! Opened a profoma invoice"
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

class UpdateInvoiceView(SuccessMessageMixin, UpdateView):
    model = Invoice
    success_message = "Sucessfully! Updated a profoma invoice"
    fields = ('member', 'description', 'VAT')
    template_name = "accnts/invoice/invoice_form.html"
    def get_context_data(self, **kwargs):
        context = super(UpdateInvoiceView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user=self.request.user.id)
        return context

class DeleteInvoiceView(SuccessMessageMixin, DeleteView):
    model = Invoice
    sucess_message = "Successfully! Deleted a profoma invoice"
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
    if not request.session.get('username'):
        messages.info(request, "Please login again.")
        return HttpResponseRedirect(reverse("accounts:login"))

    profoma = Invoice.objects.get(id = pk)
    category = int(profoma.member.category)
    tax = 0;
    if profoma.VAT == "Yes":tax = 0.16
    else:tax = 0
    total_tax = (tax * category)
    balance = (category + total_tax)
    pdf = render_to_pdf("accnts/invoice/profoma.html",
                                  {'profoma': profoma,
                                   'total_tax': total_tax, 'tax':tax,
                                   'balance': balance,})
    return HttpResponse(pdf, content_type = 'appliation/pdf')
'''
So
'''
def make_payment(request, pk):
    if not request.session.get('username'):
        messages.info(request, "Please login again.")
        return HttpResponseRedirect(reverse("accounts:login"))

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
    if not request.session.get('username'):
        messages.info(request, "Please login again.")
        return HttpResponseRedirect(reverse("accounts:login"))

    base_url = "file://" + settings.STATIC_URL
    invoice = Payment.objects.get(id = pk)
    category = int(invoice.member.category)
    tax = 0;
    if invoice.VAT == "Yes":tax = 0.16
    else:tax = 0
    total_tax = (tax * category)
    total_paid = invoice.amount
    balance = (total_tax + category)
    total_balance = ((total_tax + category) - total_paid)
    pdf = render_to_pdf("accnts/invoice/invoice.html",
                                  {'invoice': invoice,
                                   'base_url':base_url,
                                   'total_tax': total_tax,
                                   'tax':tax,
                                   'balance': balance,
                                   'total_balance': total_balance,
                                   'total_paid': total_paid, })
    return HttpResponse(pdf, content_type = 'appliation/pdf')
'''
List All invoices
'''

def list_invoices(request):
    if not request.session.get('username'):
        messages.info(request, "Please login again.")
        return HttpResponseRedirect(reverse("accounts:login"))

    invoices = Invoice.objects.all()
    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    return render(request, "accnts/invoice/list_all_invoices.html",
                  {'invoices': invoices, "employee": employee,})


'''
PayRoll Views Implementations
'''

# get tax from taxable income
def get_tax(taxable_income):
    tax = 0
    if (taxable_income >= 0) and (taxable_income <= 12298):
        tax = (0.1 * taxable_income)
    elif (taxable_income > 12298) and (taxable_income <= 23885):
        tax = (0.15 * (taxable_income-12298)) + (0.1 * 12298)
    elif (taxable_income > 23885) and (taxable_income <= 35472):
        tax = (0.2 * (taxable_income-23885)) + (0.15 * 11587) + (0.1 * 12298)
    elif (taxable_income > 35472) and (taxable_income <= 47059):
        tax = (0.3 * (taxable_income - 35472)) + (0.2* 11587) + (0.15 *11587) + (0.1 * 12298)
    elif (taxable_income > 47059):
        tax = (0.3 * 11587) + (0.2 * 11587) + (0.15 * 11587) + (0.1 * 12298)

    return tax

def get_nssf(basic_salary):
    nssf = 0
    if (basic_salary >= 3000):
        nssf = 0.06 * 3000
    elif (basic_salary > 3000) and (basic_salary <= 4500):
        nssf = 0.06 * 4500
    elif (basic_salary > 4500) and (basic_salary <= 6000):
        nssf = 0.06 * 6000
    elif (basic_salary > 6000) and (basic_salary <= 10000):
        nssf = 0.06 * 10000
    elif (basic_salary > 10000) and (basic_salary <= 14000):
        nssf = 0.06 * 14000
    elif (basic_salary > 14000) and (basic_salary <= 18000):
        nssf = 0.06 * 14000
    elif (basic_salary > 18000):
        nssf = 0.06 * 18000
    else:
        return nssf
    return nssf

'''
Get your NHIF fee
'''
def get_nhif(basic_salary):
    nhif = 0
    if (basic_salary > 0) and (basic_salary <= 5999):
        nhif = 150
    elif (basic_salary >= 6000) and (basic_salary <= 7999):
        nhif = 300
    elif (basic_salary >= 8000) and (basic_salary <= 11999):
        nhif = 400
    elif (basic_salary >= 12000) and (basic_salary <= 14999):
        nhif = 400
    elif (basic_salary >= 15000) and (basic_salary <= 19999):
        nhif = 500
    elif (basic_salary >= 20000) and (basic_salary <= 24999):
        nhif = 600
    elif (basic_salary >= 25000) and (basic_salary <= 29999):
        nhif = 750
    elif (basic_salary >= 30000) and (basic_salary <= 34999):
        nhif = 850
    elif (basic_salary >= 35000) and (basic_salary <= 39999):
        nhif = 900
    elif (basic_salary >= 40000) and (basic_salary <= 44999):
        nhif = 1000
    elif (basic_salary >= 45000) and (basic_salary <= 49999):
        nhif = 1100
    elif (basic_salary >= 50000) and (basic_salary <= 59999):
        nhif = 1200
    elif (basic_salary >= 60000) and (basic_salary <= 69999):
        nhif = 1300
    elif (basic_salary >= 70000) and (basic_salary <= 79999):
        nhif = 1400
    elif (basic_salary >= 80000) and (basic_salary <= 89999):
        nhif = 1500
    elif (basic_salary >= 90000) and (basic_salary <= 99999):
        nhif = 1600
    elif (basic_salary >= 100000):
        nhif = 1700

    return nhif


class CreatePayrollView(SuccessMessageMixin, CreateView):
    model = PayRoll
    success_message = "Successfully! Created %(employee)s payslip"
    fields = ('employee', 'pension', 'lunch', 'month')
    template_name  = 'accnts/payroll/payroll_form.html'
    def get_context_data(self, **kwargs):
        context = super(CreatePayrollView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context


# @login_required 
# def create_payroll(request):
#     form = PayRollForm()
#     employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
#     if request.method == "POST" and form.is_valid():


class ListPayrollView(ListView):
    model = PayRoll
    context_object_name  = "payrolls"
    template_name = 'accnts/payroll/payroll_list.html'
    def get_context_data(self,**kwargs):
        context = super(ListPayrollView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context

class UpdatePayrollView(SuccessMessageMixin, UpdateView):
    model = PayRoll
    success_message = "Sucessfully! Update  employee's payslip"
    fields = ('employee', 'pension', 'lunch', 'month')
    template_name  = 'accnts/payroll/payroll_form.html'
    def get_context_data(self,**kwargs):
        context = super(UpdatePayrollView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context
# list employee payslip

def payslip(request):
    if not request.session.get('username'):
        messages.info(request, "Please login again.")
        return HttpResponseRedirect(reverse("accounts:login"))

    employee = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    payslip = PayRoll.objects.filter(employee = employee.id)

    return render(request, "accnts/payroll/payslip.html", {'employee': employee, 'payslip': payslip})

"""

postings to the database
"""

def post_deductions(request, tax_id):
    payroll = PayRoll.objects.get(id = tax_id)
    payroll.is_taxed = 1
    payroll.save()
    lunch = payroll.lunch
    basic_salary  = int(payroll.employee.salary)
    nhif = get_nhif(basic_salary)
    nssf = get_nssf(basic_salary)
    gross_salary = basic_salary
    nhe = 0
    if (gross_salary * 0.015) > 5000: nhe = 2500
    else: nhe = (gross_salary * 0.015)
    nshe_contr = 0
    if (nhe*2) > 5000:nshe_contr = 5000
    else: nshe_contr = (nhe *2)
    month = payroll.month.strftime('%B')
    taxable_income = (gross_salary - nssf - payroll.pension)
    tax =  round((get_tax(taxable_income) - 1408),2)
    ded_data = Deduction(employee_id = payroll.employee.id, nssf = nssf, nhif=nhif, nhsb= nhe, paye = tax)
    ded_data.save()
    payroll.is_taxedb = 1
    payroll.save()
    messages.info(request, "Successfully! Recorded employee deductions.")
    return HttpResponseRedirect(reverse('ACCNTS:list_payroll'))

def generate_payroll(request, pk):
    if not request.session.get('username'):
        messages.info(request, "Please login again.")
        return HttpResponseRedirect(reverse("accounts:login"))

    employee  = Employee.objects.get(user = User.objects.get(username = request.session['username']).id)
    payroll = PayRoll.objects.get(id = pk)
    lunch = payroll.lunch
    basic_salary  = int(payroll.employee.salary)
    nhif = get_nhif(basic_salary)
    nssf = get_nssf(basic_salary)
    gross_salary = basic_salary
    nhe = 0
    if (gross_salary * 0.015) > 5000: nhe = 2500
    else: nhe = (gross_salary * 0.015)
    nshe_contr = 0
    if (nhe*2) > 5000:nshe_contr = 5000
    else: nshe_contr = (nhe *2)
    month = payroll.month.strftime('%B')
    print(month)
    print(nshe_contr)
    taxable_income = (gross_salary - nssf - payroll.pension)
    tax =  round((get_tax(taxable_income) - 1408),2)
    net_income = gross_salary - (lunch + nhif + tax + nshe_contr)
    ded_before_tax = (nssf + payroll.pension)
    ded_after_tax = (nhif + payroll.lunch)
    # total_ded = (nssf + payroll.pension + nhif + lunch + round(get_tax(taxable_income), 2) + nshe_contr)
    total_ded = (nssf + payroll.pension + nhif + lunch + nshe_contr)

    pdf = render_to_pdf( "accnts/payroll/print.html",{'payroll':  payroll,'gross_salary': gross_salary,
                                                      'taxable_income': taxable_income,
                                                      'tax': tax,
                                                      'nhebond': nhe,
                                                      'nhif': nhif,
                                                      'month':month,
                                                      'nssf': nssf,
                                                      'lunch': lunch,
                                                      'ded_after_tax': ded_after_tax,
                                                      'net_income':net_income,
                                                      'ded_before_tax': ded_before_tax,
                                                      'total_ded':total_ded})
    return  HttpResponse(pdf, content_type = "appliation/pdf")

# payment via invoice to users using using Payment model
# Creating invoice

class CreatePaymentView(SuccessMessageMixin, CreateView):
    model = Payment
    success_message  = "Successfully! Created and invoice for %(member)s"
    template_name  = "accnts/invoice/payment_form.html"
    fields = ('member', 'description', 'VAT', 'amount', 'payment_for',)
    def get_context_data(self, **kwargs):
        context = super(CreatePaymentView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context



class ListPaymentView(ListView):
    model = Payment
    context_object_name  = "payments"
    template_name = "accnts/invoice/payment_list.html"
    def get_context_data(self, **kwargs):
        context = super(ListPaymentView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context


class DetailPaymentView(DetailView):
    model = Payment
    context_object_name  = "payment"
    template_name  = "accnts/invoice/payment_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailPaymentView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context


class UpdatePaymentView(SuccessMessageMixin, UpdateView):
    model = Payment
    success_message = "Successfully! Updated member invoice"
    fields = ('member', 'description', 'VAT', 'amount', 'payment_for',)
    template_name  = "accnts/invoice/payment_form.html"

    def get_context_data(self, **kwargs):
        context = super(UpdatePaymentView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context


class DeletePaymentView(SuccessMessageMixin, DeleteView):
    model = Payment
    success_message  = "Successfully! Deleted an invoice"
    template_name  = "accnts/invoice/payment_delete.html"
    success_url = reverse_lazy('ACCNTS:payment_list')
    def get_context_data(self, **kwargs):
        context = super(DeletePaymentView, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.get(user = self.request.user.id)
        return context
