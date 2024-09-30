"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp.views import user_list
from myapp.views import user_table_view, index_view, user_edit_view, delete_user_view, update_user_view


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home),  # Add this line to point to the home view
    path('api/users/', user_list, name='user-list'),
    path('', index_view, name='index'),  # Main page
    path('users/', user_table_view, name='user-table'),  # User list page
    path('users/edit/', user_edit_view, name='user-edit'),  # Edit user list page
    path('users/delete/<int:user_id>/', delete_user_view, name='delete-user'),  # Delete user
    path('users/update/<int:user_id>/', update_user_view, name='update-user'),  # Update user
]
