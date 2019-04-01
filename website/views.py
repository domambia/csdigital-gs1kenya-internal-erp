from django.shortcuts import render

# Create your views here.
def indexPage(request):
    return render(request, 'website/index.html')