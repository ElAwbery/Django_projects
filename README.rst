This is a public copy of the set-up for some of my Django projects. The project hierarchy I use separates configuration from project management. It's a stripped down version of one of the (Django cookiecutter)[https://cookiecutter-django.readthedocs.io/en/latest/] hierarchies. 

charlieawbery (repository root)
 - .venv (for all my django project virtual environments. Each django project may have its own environment.)
 - management app (includes admin.py and init)
 - config (configuration root directory)
 - gitignore
 - activity log
 - manage.py
 - readme
 - requirements.txt
 - hubapp sets up the landing page for all my sites and projects
