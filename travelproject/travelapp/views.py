from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Bground, Foods

def demo(request):
    places = Place.objects.all()
    backgrounds = Bground.objects.all()
    food_image = Foods.objects.all()

    return render(request, 'index.html', {'result': places, 'result2': backgrounds, 'result3':food_image })

