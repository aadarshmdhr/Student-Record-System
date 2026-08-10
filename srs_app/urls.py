from django.urls import path

from srs_app import views

urlpatterns = [
    path("", views.student_list, name="student-list"),
    path("delete/<int:pk>/", views.delete_student, name="delete-student"),
    path("create/", views.create_student, name="create-student"),
    path("update/<int:id>/", views.update_student, name="update-student"),
]
