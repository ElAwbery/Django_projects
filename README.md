This is a public copy of the set-up for some of my Django projects. The project hierarchy I use separates configuration from project management. It's a stripped down version of one of the [Django cookiecutters](https://cookiecutter-django.readthedocs.io/en/latest/) recommended in [Two Scoops of Django](https://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/0981467342) 

This is a hierarchy map showing the relationship of the most important apps and files: 
```
charlieawbery (repository root)
- apps settings
- secrets.json
- init.py
- .venv (all my Django virtual environments here)
- config 
     - - basesettings.py
     - - productionsettings.py
     - - devsettings.py
     - - init.py
     - - urls.py
- .gitignore
- activity log
- manage.py
- readme
- requirements.txt (pip freeze)
- passenger_wsgi.py
- wsgi.py
- hubapp (lamding page and redirection app)
    - - init.py
    - - models.py
    - - views.py
    - - urls.py
    - - templates folder
        - - - html files
    - - static
        - - - css folder
        - - - images folder

```

In production I keep static files in a separate directory at the same level as the root directory. This is generally considered good practice, though it doesn't really matter for projects this small. However, it does make for a simple view of the overall project and an easily accessible, unique path to access all static files. 

Other Django apps live at the same level as hubapp in the above hierarchy. Not all of them are public yet. I work on the principle of keeping modularity as small and as contained as possible. All of the apps are designed to be easily pluggable. 



