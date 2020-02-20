from django.urls import path
from hubapp import views

# This worked for the test run. I have now updated to import all views from hubapp
# from .views import frontpage

# The app name and the name variable together uniquely identify the views to point to
# They are used in the project html templates/they should be used in the hubapp html templates, which may need updating

app_name = "hubapp"

urlpatterns = [
    # This is the testview that I created, charlieawbery homepage. It originally had the '' path connection to frontpage. I have now changed that to 'frontpage' url extension. If something goes badly wrong, change the frontpage view back to ''. If all works ok, nuke the frontpage path.
    path('frontpage', views.frontpage, name='frontpage'),
    # int is a path converter, it type checks pk
    # the angle brackets lift the final part of the url after 'projects/'
    path('<int:pk>', views.project_detail, name="project_detail"),
    path('vajrayana', views.vajrayana_redirect, name="vajrayana_redirect"),
    # path('lucky_egg', views.lucky_egg_redirect, name="lucky_egg_redirect"),
    # path('idletwilight', views.idletwilight_redirect, name="idletwilight_redirect"),
    # Empty string dispatcher must always come last
    # If the path is an empty string then the url 'projects/' gets here
    path('', views.all_projects, name="all_projects"),
]
