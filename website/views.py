from django.shortcuts import render

# Create your views here.
def indexPage(request):

    return render(request, 'website/index.html')

def about(request):

    return render(request, "website/about.html")

def bod(request):

    return render(request, "website/bod.html")
def staff(request):

    return render(request, "website/staff.html")

def contact(request):
    return render(request, "website/contacts.html")

def standards(request):
    return render(request, "website/standards.html")

def history(request):
    return render(request, "website/history.html")
def memoradum(request):
    return render(request, "website/memorandum.html")

def identity(request):
    return render(request, "website/identity.html")
