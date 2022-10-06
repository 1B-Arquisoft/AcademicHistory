from django.urls import path
from . import views

urlpatterns = [
    path('academic_history/', views.academic_histories,  name='academic_histories'),
    path('academic_history/<str:id>/', views.academic_history,  name='academic_history'),
]