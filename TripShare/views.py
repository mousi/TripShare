from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {}
    return render(request, 'index.html', context_dict)

def about(request):
    return render(request, 'about.html', {})

def test(request):
    context_dict = {}
    return render(request, 'test.html', context_dict)