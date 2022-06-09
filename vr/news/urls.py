from django.urls import path
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.news, name='news'),
    path('<int:post_id>', views.detail, name='detail')
]
