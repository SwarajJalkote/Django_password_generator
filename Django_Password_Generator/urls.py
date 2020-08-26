"""Django_Password_Generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
## Package need to be added in order to add that particular or something into the urlpatterns list
from passwordGenerator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    ## Following syntax must be followed to add url for any view
    ## add , at every path()'s end
    path('',views.home,name = 'index'),
    ## Following path() have new attribute called "name"
    ## which is used for reference to access the html file
    ## {% url 'password' %} is used in html to access views.password with 
    ## 'generatedPassword/' url
    path('generatedPassword/',views.password, name='password'),
    path('aboutus/',views.aboutus , name='aboutus'),
]
