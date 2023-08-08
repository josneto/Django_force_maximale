
# Import necessary modules and functions from Django
from django.contrib import admin
from django.urls import path, include
from Force import views

# Define the URL patterns for the project

# The path 'admin/' maps to the Django admin site, allowing access to the admin interface (e.g., http://example.com/admin/).
# The admin site is a built-in feature of Django for managing database records and site configurations.
urlpatterns = [
    path('admin/', admin.site.urls),

    # The 'include' function is used to include the URL patterns from another module (in this case, 'Force.urls').
    path('', include('Force.urls'))
]
