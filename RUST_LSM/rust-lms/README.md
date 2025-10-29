
# Rust Programming LMS

A Django-based Learning Management System for teaching Rust programming.

## Features

### Pre-Training Setup Module
Complete guides for setting up a Rust development environment:

1. **Requirements Overview** - Introduction to S/W and H/W requirements
2. **Hardware Requirements** - Detailed hardware specifications
3. **Software Requirements** - Essential software and tools
4. **Operating Systems** - Platform-specific support information
5. **Development Tools** - IDEs, editors, and productivity tools
6. **Installation Guide** - Step-by-step installation for Windows, macOS, and Linux
7. **Verification & Testing** - Verify installation and create first programs

## Project Structure

```
rust-lms/
├── courses/                    # Main courses application
│   ├── templates/
│   │   ├── base.html          # Base template with navigation
│   │   └── courses/           # Course templates
│   │       ├── course_list.html
│   │       ├── course_detail.html
│   │       ├── requirements_overview.html
│   │       ├── hardware_requirements.html
│   │       ├── software_requirements.html
│   │       ├── operating_systems.html
│   │       ├── development_tools.html
│   │       ├── installation_guide.html
│   │       └── verification_testing.html
│   ├── models.py              # Course, Lesson, Enrollment models
│   ├── views.py               # View functions
│   ├── urls.py                # URL routing
│   └── admin.py               # Django admin configuration
├── lms/                       # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── users/                     # User management
├── manage.py                  # Django management script
└── requirements.txt           # Python dependencies
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 4. Run Development Server

```bash
python manage.py runserver
```

### 5. Access the Application

- Homepage: http://127.0.0.1:8000/
- Requirements Overview: http://127.0.0.1:8000/courses/requirements/
- Admin Panel: http://127.0.0.1:8000/admin/

## Available URLs

### Course URLs
- `/` - Course list (homepage)
- `/courses/` - Course list
- `/courses/course/<id>/` - Course detail

### Pre-Training Setup URLs
- `/courses/requirements/` - Requirements overview
- `/courses/requirements/hardware/` - Hardware requirements
- `/courses/requirements/software/` - Software requirements
- `/courses/requirements/operating-systems/` - OS support
- `/courses/requirements/development-tools/` - Development tools
- `/courses/requirements/installation/` - Installation guide
- `/courses/requirements/verification/` - Verification & testing

## Technologies Used

- **Backend**: Django 4.x
- **Frontend**: HTML5, CSS3 (responsive design)
- **Database**: SQLite (default, configurable)
- **Styling**: Custom CSS with gradient themes

## Features of the Pre-Training Module

### Interactive Design
- Beautiful gradient UI with purple theme
- Responsive card-based layout
- Hover effects and smooth transitions
- Mobile-friendly design

### Comprehensive Content
- Detailed hardware specifications with comparison tables
- Step-by-step installation guides for all major OS
- Tool recommendations for different skill levels
- Troubleshooting sections for common issues
- Code examples and command blocks
- Visual verification steps

### Educational Focus
- Beginner-friendly explanations
- Pro tips and best practices
- Warning boxes for common pitfalls
- Success indicators for verification
- Links to additional resources

## Future Enhancements

- [ ] Rust Fundamentals course
- [ ] Ownership & Borrowing module
- [ ] Interactive code editor
- [ ] Progress tracking
- [ ] Quizzes and assessments
- [ ] User authentication
- [ ] Course completion certificates

## License

This project is for educational purposes.

## Project Structure

```
rust-lms/
├── lms/                  # Main Django project directory
│   ├── __init__.py      # Marks the lms directory as a Python package
│   ├── settings.py      # Configuration settings for the Django project
│   ├── urls.py          # URL patterns for the Django project
│   ├── asgi.py          # ASGI entry point for asynchronous capabilities
│   └── wsgi.py          # WSGI entry point for deployment
├── courses/             # App for managing courses
│   ├── __init__.py      # Marks the courses directory as a Python package
│   ├── admin.py         # Admin site configuration for courses
│   ├── apps.py          # App configuration for courses
│   ├── models.py        # Data models for courses
│   ├── tests.py         # Test cases for courses
│   ├── views.py         # View functions for courses
│   └── urls.py          # URL patterns for courses
├── users/               # App for managing users
│   ├── __init__.py      # Marks the users directory as a Python package
│   ├── admin.py         # Admin site configuration for users
│   ├── apps.py          # App configuration for users
│   ├── models.py        # Data models for users
│   ├── tests.py         # Test cases for users
│   ├── views.py         # View functions for users
│   └── urls.py          # URL patterns for users
├── manage.py             # Command-line utility for the Django project
└── requirements.txt      # Project dependencies
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd rust-lms
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Start the development server:**
   ```
   python manage.py runserver
   ```

## Usage

- Access the LMS at `http://127.0.0.1:8000/`.
- Users can register, log in, and enroll in Rust programming courses.
- Admins can manage courses and users through the Django admin interface.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.