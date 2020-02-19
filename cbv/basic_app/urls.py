from django.urls import path , re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('' , views.WorksiteView.as_view(), name = 'list'),
    path('<int:pk>/' , views.WorksiteDetailView.as_view(), name = 'detail'),
]
