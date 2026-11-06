# CampusConnect - First Django Application

**Name:** Dave Laurence Repe
**Section:** G5
**Course:** CSIT327

A Django app with sign-up, login, a role-based dashboard, and an editable
profile page, styled with Bootstrap 5 (CDN).

## Features
- Sign-up with validation and a success message (Django messages framework)
- Login / logout (POST logout with CSRF protection)
- Profile page using UpdateView; login required, users can only edit their own profile
- Role-based access (Student / Administrator) with a protected admin panel
- Shared base.html with Bootstrap 5 navbar

## How to run
1. Clone the repo and open the folder:
       git clone https://github.com/davelaurencerepe/CSIT327-G5-Repe-DaveLaurence-FirstDjango.git
       cd CSIT327-G5-Repe-DaveLaurence-FirstDjango
2. Create and activate a virtual environment (Python 3.12+):
       python -m venv .venv
       .venv\Scripts\activate
3. Install dependencies:
       pip install -r requirements.txt
4. Set up the database and an admin account:
       python manage.py migrate
       python manage.py createsuperuser
5. Start the server:
       python manage.py runserver
6. Open http://127.0.0.1:8000/
   (In /admin, set your superuser's Role to Administrator to open the admin panel.)
