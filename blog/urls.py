from django.urls import path
from . import views


#URL-шаблон
urlpatterns = [
	path('', views.post_list, name = 'post_list'),
]