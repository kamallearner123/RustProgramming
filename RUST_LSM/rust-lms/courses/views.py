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

# Cargo & Package Management Views
def cargo_overview(request):
    return render(request, 'courses/cargo_package_management/overview.html')

def cargo_intro(request):
    return render(request, 'courses/cargo_package_management/intro.html')

def cargo_getting_started(request):
    return render(request, 'courses/cargo_package_management/getting_started.html')

def cargo_project_structure(request):
    return render(request, 'courses/cargo_package_management/project_structure.html')

def cargo_toml_guide(request):
    return render(request, 'courses/cargo_package_management/cargo_toml.html')

def cargo_dependencies(request):
    return render(request, 'courses/cargo_package_management/dependencies.html')

def cargo_commands(request):
    return render(request, 'courses/cargo_package_management/commands.html')

def cargo_build_modes(request):
    return render(request, 'courses/cargo_package_management/build_modes.html')

def cargo_workspaces(request):
    return render(request, 'courses/cargo_package_management/workspaces.html')

def cargo_publishing(request):
    return render(request, 'courses/cargo_package_management/publishing.html')

def cargo_best_practices(request):
    return render(request, 'courses/cargo_package_management/best_practices.html')

# Embedded Development Environment Views
def installing_rust_embedded(request):
    return render(request, 'courses/embedded_dev_environment/installing_rust_embedded.html')

def configuring_toolchains(request):
    return render(request, 'courses/embedded_dev_environment/configuring_toolchains.html')

def microcontroller_platforms(request):
    return render(request, 'courses/embedded_dev_environment/microcontroller_platforms.html')

def mcu_ecosystem(request):
    return render(request, 'courses/embedded_dev_environment/mcu_ecosystem.html')

def real_world_projects(request):
    return render(request, 'courses/embedded_dev_environment/real_world_projects.html')

# Rust Essentials for Embedded Views
def embedded_syntax_overview(request):
    return render(request, 'courses/rust_essentials_embedded/embedded_syntax_overview.html')

def ownership_borrowing_lifetimes(request):
    return render(request, 'courses/rust_essentials_embedded/ownership_borrowing_lifetimes.html')

def memory_management_embedded(request):
    return render(request, 'courses/rust_essentials_embedded/memory_management.html')

def nostd_environments(request):
    return render(request, 'courses/rust_essentials_embedded/nostd_environments.html')

def interrupts_lowlevel(request):
    return render(request, 'courses/rust_essentials_embedded/interrupts_lowlevel.html')

def blinky_lab(request):
    return render(request, 'courses/rust_essentials_embedded/blinky_lab.html')