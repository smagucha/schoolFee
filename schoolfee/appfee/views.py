from django.shortcuts import render
from .models import Fee, Term
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy


class ListTerm(ListView):
    model = Term
    context_object_name = "allterms"


class CreateTerm(CreateView):
    model = Term
    success_url = reverse_lazy("allstudent")
    fields = "__all__"


class DeleteTerm(DeleteView):
    model = Term
    success_url = reverse_lazy("allstudent")


class ListFee(ListView):
    model = Fee
    context_object_name = "allfee"


class CreateFee(CreateView):
    model = Fee
    success_url = reverse_lazy("allstudent")
    fields = "__all__"
