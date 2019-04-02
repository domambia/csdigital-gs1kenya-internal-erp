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
