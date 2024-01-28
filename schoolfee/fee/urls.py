from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("allstudent/", views.AllStudent.as_view(), name="allstudent"),
    path("addstudent/", views.CreateStudent.as_view(), name="addstudent"),
    path("studentview/<int:pk>/", views.StudentView.as_view(), name="detailview"),
    path(
        "updatestudent/<int:pk>/", views.UpdateStudent.as_view(), name="updatestudent"
    ),
    path(
        "deletestudent/<int:pk>/", views.DeleteStudent.as_view(), name="deletestudent"
    ),
]
