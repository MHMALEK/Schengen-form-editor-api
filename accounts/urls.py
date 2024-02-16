from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("list", views.list, name="list"),
    path("<int:account_id>/detail", views.get_account, name="detail"),
    path("<int:account_id>/update", views.update_account, name="edit"),
    path("<int:account_id>/delete", views.delete_account, name="delete"),
]
