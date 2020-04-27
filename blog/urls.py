from django.urls import path
from . import views


#URL-шаблон 
#мы связали view под именем post_list с корневым URL-адресом ('')
urlpatterns = [
	path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]