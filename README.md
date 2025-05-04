# Personal Portfolio Website

A Django-based personal portfolio website with blog and contact functionality.

## Features

- Homepage with profile information, skills, projects, and experience
- Blog section with list and detail views
- Contact form with database storage
- Admin interface for managing blog posts and contact messages
- Responsive design using Bootstrap

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On Windows
.\venv\Scripts\activate

# On Unix or MacOS
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

- Access the website at `http://127.0.0.1:8000/`
- Access the admin interface at `http://127.0.0.1:8000/admin/`
- Use the admin interface to add blog posts and manage contact messages

## Customization

- Update the profile information in `templates/home.html`
- Add your own projects and experience
- Customize the styling by modifying the Bootstrap classes in the templates 