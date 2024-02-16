from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pdf_file_id>/detail", views.detail, name="detail"),
    path("<int:pdf_file_id>/edit", views.edit, name="edit"),
    path("<int:pdf_file_id>/delete", views.delete, name="delete"),
]
