from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('scan/', views.scan_qr, name='scan_qr'),
    path('records/', views.attendance_records, name='attendance_records'),
]