from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('update_student/<str:pk_test>/', views.update_student, name='update_student'),
    path('delete_student/<str:pk_test>/', views.delete_student, name='delete_student'),
    path('', views.sign_in, name='sign_in'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('search_student/', views.search_student, name='search_student'),
]
