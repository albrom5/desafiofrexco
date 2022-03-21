from django.contrib import admin
from django.urls import path, include

from desafioFrexco.core import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('users_json/', views.users_list),
    path('users_csv/', views.users_list_csv),
    path('users_xlsx/', views.UsersListXLSX.as_view()),
    path('create_user/', views.user_create),
]
