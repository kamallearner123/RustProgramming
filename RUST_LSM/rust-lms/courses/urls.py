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
    
    # Cargo & Package Management URLs
    path('cargo/', views.cargo_overview, name='cargo_overview'),
    path('cargo/intro/', views.cargo_intro, name='cargo_intro'),
    path('cargo/getting-started/', views.cargo_getting_started, name='cargo_getting_started'),
    path('cargo/project-structure/', views.cargo_project_structure, name='cargo_project_structure'),
    path('cargo/cargo-toml/', views.cargo_toml_guide, name='cargo_toml_guide'),
    path('cargo/dependencies/', views.cargo_dependencies, name='cargo_dependencies'),
    path('cargo/commands/', views.cargo_commands, name='cargo_commands'),
    path('cargo/build-modes/', views.cargo_build_modes, name='cargo_build_modes'),
    path('cargo/workspaces/', views.cargo_workspaces, name='cargo_workspaces'),
    path('cargo/publishing/', views.cargo_publishing, name='cargo_publishing'),
    path('cargo/best-practices/', views.cargo_best_practices, name='cargo_best_practices'),
    
    # Embedded Development Environment URLs
    path('embedded-dev/installing-rust/', views.installing_rust_embedded, name='installing_rust_embedded'),
    path('embedded-dev/configuring-toolchains/', views.configuring_toolchains, name='configuring_toolchains'),
    path('embedded-dev/microcontroller-platforms/', views.microcontroller_platforms, name='microcontroller_platforms'),
    path('embedded-dev/mcu-ecosystem/', views.mcu_ecosystem, name='mcu_ecosystem'),
    path('embedded-dev/real-world-projects/', views.real_world_projects, name='real_world_projects'),
    
    # Rust Essentials for Embedded URLs
    path('rust-essentials/syntax-overview/', views.embedded_syntax_overview, name='embedded_syntax_overview'),
    path('rust-essentials/ownership-borrowing-lifetimes/', views.ownership_borrowing_lifetimes, name='ownership_borrowing_lifetimes'),
    path('rust-essentials/memory-management/', views.memory_management_embedded, name='memory_management_embedded'),
    path('rust-essentials/nostd-environments/', views.nostd_environments, name='nostd_environments'),
    path('rust-essentials/interrupts-lowlevel/', views.interrupts_lowlevel, name='interrupts_lowlevel'),
    path('rust-essentials/blinky-lab/', views.blinky_lab, name='blinky_lab'),
]