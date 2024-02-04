from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from .models import AidName, FeeAid
from django.urls import reverse_lazy

# FeeAid


class CreateAid(CreateView):
    model = AidName
    fields = "__all__"
    success_url = reverse_lazy("allstudent")


class ListAid(ListView):
    model = AidName


class DeleteAid(DeleteView):
    model = AidName
    success_url = reverse_lazy("allstudent")


class CreateFeeAid(CreateView):
    model = FeeAid
    fields = "__all__"


class ListFeeAid(ListView):
    model = FeeAid


class DeleteAid(DeleteView):
    model = FeeAid
    success_url = reverse_lazy("allstudent")
