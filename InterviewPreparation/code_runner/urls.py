from django.urls import path
from . import views

app_name = 'code_runner'

urlpatterns = [
    path('editor/', views.code_editor, name='editor'),
    path('api/execute/', views.execute_code, name='execute_code'),
    path('api/templates/', views.get_templates, name='get_templates'),
    path('api/template/<str:language>/', views.get_template, name='get_template'),
]
