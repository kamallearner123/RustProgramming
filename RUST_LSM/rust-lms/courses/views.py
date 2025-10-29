from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/course_detail.html', {'course': course})

def course_create(request):
    return render(request, 'courses/course_create.html')

def course_edit(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'courses/course_edit.html', {'course': course})

# Pre-Training Setup Views
def requirements_overview(request):
    return render(request, 'courses/requirements_overview.html')

def hardware_requirements(request):
    return render(request, 'courses/hardware_requirements.html')

def software_requirements(request):
    return render(request, 'courses/software_requirements.html')

def operating_systems(request):
    return render(request, 'courses/operating_systems.html')

def development_tools(request):
    return render(request, 'courses/development_tools.html')

def installation_guide(request):
    return render(request, 'courses/installation_guide.html')

def verification_testing(request):
    return render(request, 'courses/verification_testing.html')

# Rust Fundamentals Views
def rust_fundamentals_overview(request):
    return render(request, 'courses/rust_fundamentals/overview.html')

def rust_variables(request):
    return render(request, 'courses/rust_fundamentals/variables.html')

def rust_data_types(request):
    return render(request, 'courses/rust_fundamentals/data_types.html')

def rust_functions(request):
    return render(request, 'courses/rust_fundamentals/functions.html')

def rust_control_flow(request):
    return render(request, 'courses/rust_fundamentals/control_flow.html')