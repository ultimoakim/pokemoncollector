from django.shortcuts import render

# Create your views here.

def home(request):
    # In Django, we include .html file extensions, unlike rendering .ejs templates. See how the format is different?
    # All view (controller, if it was Express) functions need to define a positional parameter to accept the request object that Django will be passing in. This request object is very much like the req object in Express functions.
    return render(request, 'home.html')