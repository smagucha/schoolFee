from django.urls import path
from . import views

urlpatterns = [
    path("term/", views.ListTerm.as_view(), name="terms"),
    path("createterm/", views.CreateTerm.as_view(), name="createterms"),
    path("deleteterm/<int:pk>/", views.DeleteTerm.as_view(), name="deleteterms"),
]
