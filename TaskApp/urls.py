"""
URL configuration for TaskApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Task.views import createTasks
from Task.views import home
from Task.views import createCategory
from Task.views import calendar
from Task.views import taskDetails
from Task.views import editTask
import Task.views.signUp as signUp
import Task.views.login as login
import Task.views.home as home
import Task.views.signOut as logOut


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signUp.signUp, name='signup'),
    path('signin/', login.signin, name='signin'),
    path('logout/', logOut.signout, name='logout'),
    path('', home.home, name ='home'),
    path('createTasks/', createTasks.createTasks, name = 'createTasks'),
    path('createCategory/', createCategory.createCategory, name = 'createCategory'),
    path('calendar/', calendar.calendar, name = 'calendar'),
    path('taskDetails/<int:tID>/', taskDetails.taskDetails, name = 'taskDetails'),
    path('editTask/<int:task_id>/', editTask.editTask, name='editTask'),

]
