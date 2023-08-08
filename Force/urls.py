# Import the necessary modules and functions from Django
from django.urls import path
from . import views

# Define the URL patterns for the app

# The empty string '' as the URL pattern means that this URL will be matched for the base URL of the app (e.g., http://example.com/).
# When the base URL is accessed, the predict view function from the 'views' module will be called.
# The 'name' parameter is used to provide a name for this URL pattern, which can be used to reference this URL in Django templates or views.
urlpatterns = [
    path('', views.predict, name='form'),
]
