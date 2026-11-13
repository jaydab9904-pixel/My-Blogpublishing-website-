# Blog Publishing Platform

A Django-based blogging platform where users can create, manage, search, and explore blog posts.

## Features

- **User authentication:** User registration, login, and logout.
- **Post management:** Create, view, edit, and delete blog posts.
- **Ownership permissions:** Users can edit and delete their own posts.
- **Categories and tags:** Organize posts by category and tags.
- **Search:** Search posts by title, content, author, category, and tags.
- **Pagination:** Browse posts across multiple pages.
- **Django Admin:** Manage application data through the admin interface.
- **Responsive styling:** Custom HTML and CSS styling.
- **Static file handling:** WhiteNoise for serving static files in production.

## Technologies Used

- Python
- Django
- HTML
- CSS
- SQLite for local development
- PostgreSQL for production deployment
- WhiteNoise
- Gunicorn
- Git and GitHub

## Screenshots

### Homepage
![Homepage](screenshots/Screenshot (191).png)

### Blog Detail
![Blog Detail](screenshots/Screenshot (196).png)


### Login
![Login](screenshots/Screenshot (198).png)

<!-- Add screenshots in this section after creating the screenshots folder. -->

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/jaydab9904-pixel/My-Blogpublishing-website-.git
cd My-Blogpublishing-website-
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add your own values:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
CSRF_TRUSTED_ORIGINS=
```

Never commit your real `.env` file or secret key to GitHub.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Production

The project includes a deployment build script (`build.sh`), Gunicorn, PostgreSQL database configuration, and WhiteNoise static-file handling.

A live deployment link will be added here once deployment is complete.

## Author

Developed as a Django web development project.