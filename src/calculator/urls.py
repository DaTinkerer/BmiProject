from django.urls import path
from .views import get_bmi_eng

urlpatterns = [
    # path('', index),
    # path('', MyView.as_view()),
    path('eng/', get_bmi_eng ),
    
]