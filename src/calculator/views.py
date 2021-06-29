from django.shortcuts import render, redirect, HttpResponse
from .forms import Metic_UnitsForm, English_UnitsForm
from django.views.generic.base import TemplateView
from pint import UnitRegistry
from django.http import JsonResponse
import json

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

        
        
       
        return JsonResponse({'bmi': bmi}, status=201)
    return render(request, 'calculator/index.html')



        
        
   

    











# class JSONResponseMixin:
#     """
#     A mixin that can be used to render a JSON response.
#     """
#     def render_to_json_response(self, context, **response_kwargs):
#         """
#         Returns a JSON response, transforming 'context' to make the payload.
#         """
#         return JsonResponse(
#             self.get_data(context),
#             **response_kwargs
#         )
#     def get_data(self, context):
#         """
#         Returns an object that will be serialized as JSON by json.dumps().
#         """
#         # Note: This is *EXTREMELY* naive; in reality, you'll need
#         # to do much more complex handling to ensure that arbitrary
#         # objects -- such as Django model instances or querysets
#         # -- can be serialized as JSON.
#         return context
# def _get_form(request, formcls, prefix):
#     data = request.POST if prefix in request.POST else None
#     return formcls(data, prefix=prefix)

# class MyView(JSONResponseMixin, TemplateView):
#     template_name = 'calculator/index.html'
    
#     def get(self, request, *args, **kwargs):
#         return self.render_to_response({'english_units_form': English_UnitsForm(prefix='eu_form'), 'metric_units_form': Metic_UnitsForm(prefix='mu_form')})

#     def post(self, request, *args, **kwargs):
        
#         ureg = UnitRegistry()
#         english_units_form = _get_form(request, English_UnitsForm, 'eu_form')
#         metric_units_form = _get_form(request, Metic_UnitsForm, 'mu_form')
#         if english_units_form.is_bound and english_units_form.is_valid():
#             weight = english_units_form.cleaned_data['weight_lbs'] * ureg('pound')

#             height_ft = english_units_form.cleaned_data['height_ft'] * ureg.foot
#             height_in = english_units_form.cleaned_data['height_in'] * ureg.inch
#             height = height_ft + height_in

#             mass = weight.to('kilograms')
#             height_m = height.to('meters')

#             bmi = str(mass / height_m ** 2)

            
#             with open('calculator/bmi.txt', 'w') as f:
#                 f.write(bmi)
#                 f.seek(0)
                
#                 f.close
#             return redirect('/calculate/')
                


            
            
#         elif metric_units_form.is_bound and metric_units_form.is_valid():
#             weight_kg = metric_units_form.cleaned_data['weight_kg'] * ureg.kilograms
#             height_cm = metric_units_form.cleaned_data['height_cm'] * ureg.cm

#             bmi = weight_kg / height_cm.to('meters') ** 2   
    
    
    
        



            
            
        
        
#         return self.render_to_response({'metric_units_form': metric_units_form, 'english_units_form': english_units_form})

# def send_bmi(request):
#     with open('calculator/bmi.txt', 'r+') as f:
#         f.seek(0)
#         bmi = f.read()
#         f.close()

#         if request.is_ajax():
#             return JsonResponse({'bmi': bmi}, status=200)

            
            




    
        


