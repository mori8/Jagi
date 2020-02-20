from django.shortcuts import render

# Create your views here.

def jagi_list(request):
    return render(request, 'app_jagi/jagi_list.html', {})
