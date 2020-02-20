from django.shortcuts import render

# Create your views here.

def jagi_list(request):
    return render(request, 'blog/jagi_list.html', {})
