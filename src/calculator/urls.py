from django.urls import path
from .views import get_bmi_eng, index, get_bmi_metric

urlpatterns = [
    path('', index),
    
    path('eng/', get_bmi_eng ),
    path('metric/', get_bmi_metric),
    
]