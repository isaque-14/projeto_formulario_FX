from django.shortcuts import render

def home(request):  
    return render(request, 'index.html')
    
def form(request):
    return render(request, 'form.html')