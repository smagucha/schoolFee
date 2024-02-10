from django.urls import path
from . import views

urlpatterns = [
    path("createaid/", views.CreateAid.as_view(), name="createaid"),
    path("listaid/", views.ListAid.as_view(), name="listaid"),
    path("deleteaid/<int:id>/", views.deleteaid, name="deleteaid"),
    # path("deleteaid/<int:pk>/", views.AidDeleteView.as_view(), name="deleteaid"),
]
