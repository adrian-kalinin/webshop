# Webshop

Quite basic but yet fully functioning online shop with following features:

- Catalogue with search and sorting.
- Detailed info about each product.
- Creating, updating and deleting products.
- Shopping cart implemented with AJAX reqeusts.
- Registration, authentication and permissions.
- Good-looking and responsive web design.

### Tech stack in a nutshell

Backend is built with Python and Django, database is MySQL. Package `django-environ` is used for managing environment variables. There are HTML templates with Tailwind CSS and vanilla JS on frontend.

# How to launch

1. Clone the repository (e. g. `git clone https://github.com/adrian-kalinin/webshop`)
2. Install requirements (e. g. `python -m pip install requirements.txt`)
3. In `webshop` app create `.env` file with variables based on `.template.env`. Or simply set all environment variables via terminal, and additianally set `READ_DOT_ENV_FILE` as `False`.
4. Run server with `python manage.py runserver`

