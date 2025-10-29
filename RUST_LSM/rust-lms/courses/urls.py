from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/new/', views.course_create, name='course_create'),
    path('course/<int:course_id>/edit/', views.course_edit, name='course_edit'),
    
    # Pre-Training Setup URLs
    path('requirements/', views.requirements_overview, name='requirements_overview'),
    path('requirements/hardware/', views.hardware_requirements, name='hardware_requirements'),
    path('requirements/software/', views.software_requirements, name='software_requirements'),
    path('requirements/operating-systems/', views.operating_systems, name='operating_systems'),
    path('requirements/development-tools/', views.development_tools, name='development_tools'),
    path('requirements/installation/', views.installation_guide, name='installation_guide'),
    path('requirements/verification/', views.verification_testing, name='verification_testing'),
    
    # Rust Fundamentals URLs
    path('rust-fundamentals/', views.rust_fundamentals_overview, name='rust_fundamentals_overview'),
    path('rust-fundamentals/variables/', views.rust_variables, name='rust_variables'),
    path('rust-fundamentals/data-types/', views.rust_data_types, name='rust_data_types'),
    path('rust-fundamentals/functions/', views.rust_functions, name='rust_functions'),
    path('rust-fundamentals/control-flow/', views.rust_control_flow, name='rust_control_flow'),
]