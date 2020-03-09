## Django projects snapshot

This is a public copy of the source code for some of my Django projects. All secret keys and settings have been replaced with dummies. The project hierarchy I use separates configuration from project management. I started with a stripped down version of one of the [Django cookiecutters](https://cookiecutter-django.readthedocs.io/en/latest/) recommended in [Two Scoops of Django.](https://www.amazon.com/Two-Scoops-Django-Best-Practices/dp/0981467342)

My website, charlieawbery.com, is mostly organized in the hubapp directory. Config is where I keep all settings files, separated out for production and development. I first develop new functionality in my local environment (Mac, MAMP, PhpMyAdmin, Django/Python in VSC). I then usually push changes to the git master, pull to the remote server and debug using debugsettings.py, but I also use FTP for negligable updates or transferring new static files. 

This is a hierarchy map showing the relationship of the most important apps and files: 
```
charlieawbery (repository root)
- charlieawbery_root
     - - contains secret key files
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
- hubapp (landing page and redirection app)
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

My local development set-up uses the typical Django structure for static files and templates, so that there is an extra folder mirroring the app name for templates and static files, for example as follows:

```
- hubapp
     - - templates
          - - - hubapp
               - - - - base.html
               - - - - all_projects.html
               - - - - resume.html 
     - - static
          - - - hubapp
               - - - - css folder
               - - - - images folder

```
Django keeps track of static files in a cache automatically created outside the main project folder. The extra folder ensures that any duplicate file names are recognized as belonging to their separate projects. This is not necessary to serve files from the remote server where static files are kept separately in a public_html folder at the same level as the root directory and Apache uses the file pathname to access templates. 

Other Django apps live at the same level as hubapp in the above hierarchy. Not all of them are public yet. I work on the principle of keeping modularity as small and as contained as possible. All of the apps are designed to be easily pluggable. 

This repo is a snapshot of the state of my Django projects at a particular point in time (February 2020), it is not a working project and is not regularly updated. 

