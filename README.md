<<<<<<< HEAD
<!-- # nyc-guide
# READ ME #

# This is our NYC GUIDE PROJECT #

# Group Members are : -->
<!-- Jonathan Wrenn & Mikayla Munn

Instructions:

1. Set up your virtual enviroment
To create virtual environment, first you need to install python3-venv. Run:
$ sudo apt update
$ sudo apt-get install python3-venv

Create a virtual environment named myenv via running:
$ python3 -m venv myenv

To activate myenv, run:
$ source myenv/bin/activate

from:https://py-vscode.readthedocs.io/en/latest/files/venv.html
2. How to install Django 
Update pip in the virtual environment by running the following command in the VS Code Terminal:

python -m pip install --upgrade pip
Install Django in the virtual environment by running the following command in the VS Code Terminal:

python -m pip install django

from:https://code.visualstudio.com/docs/python/tutorial-django
3. How to run Django Site
In the VS Code Terminal where your virtual environment is activated, run the following command:

django-admin startproject web_project .
This startproject command assumes (by use of . at the end) that the current folder is your project folder, and creates the following within it:

manage.py: The Django command-line administrative utility for the project. You run administrative commands for the project using python manage.py <command> [options].

A subfolder named web_project, which contains the following files:

__init__.py: an empty file that tells Python that this folder is a Python package.
asgi.py: an entry point for ASGI-compatible web servers to serve your project. You typically leave this file as-is as it provides the hooks for production web servers.
settings.py: contains settings for Django project, which you modify in the course of developing a web app.
urls.py: contains a table of contents for the Django project, which you also modify in the course of development.
wsgi.py: an entry point for WSGI-compatible web servers to serve your project. You typically leave this file as-is as it provides the hooks for production web servers.
Create an empty development database by running the following command:

python manage.py migrate

When you run the server the first time, it creates a default SQLite database in the file db.sqlite3 that is intended for development purposes, but can be used in production for low-volume web apps. For additional information about databases, see the Types of databases section.

To verify the Django project, make sure your virtual environment is activated, then start Django's development server using the command python manage.py runserver. The server runs on the default port 8000, and you see output like the following output in the terminal window:

Performing system checks...

System check identified no issues (0 silenced).

January 15, 2021 - 14:33:31
Django version 3.1.5, using settings 'web_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Django's built-in web server is intended only for local development purposes. When you deploy to a web host, however, Django uses the host's web server instead. The wsgi.py and asgi.py modules in the Django project take care of hooking into the production servers.

When you're done, close the browser window and stop the server in VS Code using Ctrl+C as indicated in the terminal output window.

4. How to run Django App

In the VS Code Terminal with your virtual environment activated, run the administrative utility's startapp command in your project folder (where manage.py resides):

python manage.py startapp hello
The command creates a folder called hello that contains a number of code files and one subfolder. Of these, you frequently work with views.py (that contains the functions that define pages in your web app) and models.py (that contains classes defining your data objects). The migrations folder is used by Django's administrative utility to manage database versions as discussed later in this tutorial. There are also the files apps.py (app configuration), admin.py (for creating an administrative interface), and tests.py (for creating tests), which are not covered here.

Modify hello/views.py to match the following code, which creates a single view for the app's home page:

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Django!")
Create a file, hello/urls.py, with the contents below. The urls.py file is where you specify patterns to route different URLs to their appropriate views. The code below contains one route to map root URL of the app ("") to the views.home function that you just added to hello/views.py:

from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
]
The web_project folder also contains a urls.py file, which is where URL routing is actually handled. Open web_project/urls.py and modify it to match the following code (you can retain the instructive comments if you like). This code pulls in the app's hello/urls.py using django.urls.include, which keeps the app's routes contained within the app. This separation is helpful when a project contains multiple apps.

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("hello.urls")),
    path('admin/', admin.site.urls)
]
Save all modified files.

In the VS Code Terminal, again with the virtual environment activated, run the development server with python manage.py runserver and open a browser to http://127.0.0.1:8000/ to see a page that renders "Hello, Django". -->

=======
# NYC-Guide
>>>>>>> dd62cacf44f1da742d7f138be76b748f682eb557
