
# Django Blog Project

This is a simple blog application built with Django. It allows users to create, edit, and delete posts. This README will guide you through setting up and running the project locally.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)

## Installation

Clone the repository from GitHub:
```bash
git clone https://github.com/dishajayaprakash/Blog-using-Django.git
cd Blog-using-Django
```

Set up a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

Install the required packages:
```bash
pip install -r requirements.txt
```

## Setup

Initialize the database:
```bash
python manage.py migrate
```

Create an admin user:
```bash
python manage.py createsuperuser
```

## Running the Application

Start the server:
```bash
python manage.py runserver
```

The blog will be available at `http://127.0.0.1:8000/`.

## Admin Interface

Access the admin interface at `http://127.0.0.1:8000/admin`. Use the superuser credentials you created earlier to login and manage the blog posts.

