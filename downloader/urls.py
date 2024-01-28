# myapp/urls.py
from django.urls import path
from .views import convert

# Define URL patterns for the 'myapp' application
urlpatterns = [
    # Create a URL pattern for the 'my_view' view
    path('', convert, name='convert'),


    # You can add more URL patterns for other views as needed
    # For example:
    # path('another_view/', another_view, name='another_view'),
]