from django.urls import path
from . import views

from .views import HealthRecordDeleteView

app_name = 'health_data'

urlpatterns = [
    path('', views.health_record_list, name='health_record_list'),
    path('create/', views.health_record_create, name='health_record_create'),
    path('<int:pk>/', views.health_record_detail, name='health_record_detail'),
    path('<int:pk>/edit/', views.health_record_update, name='health_record_update'),
    path('record/<int:pk>/delete/', HealthRecordDeleteView.as_view(), name='health_record_delete'),
]

urlpatterns += [
    path('upload-pdf/', views.upload_health_pdf, name='upload_health_pdf'),
]