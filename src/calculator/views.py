from django.shortcuts import render, redirect, HttpResponse
# from .forms import Metic_UnitsForm, English_UnitsForm
from django.views.generic.base import TemplateView
from pint import UnitRegistry
from django.http import JsonResponse
import json

def index(request):
    return render(request, 'calculator/index.html')

# Process english units form
def get_bmi_eng(request):
    
    ureg = UnitRegistry()

    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        

        weight = int(data['weight_lbs']) * ureg('pound')

        height_ft =int(data['height_ft']) * ureg.foot
        height_in = int(data['height_in']) * ureg.inch
        height = height_ft + height_in

        mass = weight.to('kilograms')
        height_m = height.to('meters')

        bmi = '{:~P}'.format(round((mass / height_m ** 2), 1))

        
        
       
        return JsonResponse({'bmi': bmi}, status=200)
    return render(request, 'calculator/index.html')


# Process metric units form
def get_bmi_metric(request):
    
    ureg = UnitRegistry()

    if request.method == 'POST':
        
        data = json.loads(request.body)
        
        weight_kg = int(data['weight_kg']) * ureg.kilograms
        height_cm = int(data['height_cm']) * ureg.cm

        
        bmi = '{:~P}'.format(round((weight_kg / height_cm.to('meters') ** 2), 1))

        
        
       
        return JsonResponse({'bmi': bmi}, status=200)
    return render(request, 'calculator/index.html')
    

