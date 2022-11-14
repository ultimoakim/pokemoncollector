"""pokemoncollector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# Don't forget to add the "include" function to the import!
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Remember, an empty string '' represents the "starts with" path in Django. A bit different from Express, as you can see.
    # Also, don't forget about the trailing backslash. That's another Django thing.
    path('', include('main_app.urls')),
]
