from django.urls import path
from . import views

urlpatterns = [
    path("", views.liste_employee, name="employee_list"),
    path("add_employee/", views.add_employee, name="employee_add"),
    path("modify_employee/<int:id>/", views.modify_employee, name="modify_employee"),
    path("delete_employee/<int:id>/", views.delete_employee, name='delete_employee'),
]