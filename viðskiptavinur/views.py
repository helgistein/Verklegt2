from django.shortcuts import render
from viðskiptavinur.models import Viðskiptavinur
# Create your views here.

def index(request):
    return render(request, "viðskiptavinur/index.html", {
        'viðskiptavinir': Viðskiptavinur.objects.all()
    })