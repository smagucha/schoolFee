from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Student
from django.shortcuts import get_object_or_404
from django.http import Http404


def home(request):
    return HttpResponse("This is a school fee management system")


class AllStudent(ListView):
    model = Student
    context_object_name = "allstudents"
    template_name = "fee/student.html"

    def get_queryset(self):
        from datetime import date

        return Student.objects.filter(year=str(date.today().year))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "all student in the current year"
        return context


class StudentView(DetailView):
    model = Student
    context_object_name = "student"

    def get_object(self, queryset=None):
        try:
            get_object_or_404(Student, pk=self.kwargs["pk"])
        except Student.DoesNotExist:
            raise Http404("The requested student does not exist.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "student view"
        return context


class CreateStudent(CreateView):
    model = Student
    fields = "__all__"
    success_url = reverse_lazy("allstudent")


class UpdateStudent(UpdateView):
    model = Student
    fields = "__all__"
    success_url = reverse_lazy("allstudent")


class DeleteStudent(DeleteView):
    model = Student
    success_url = reverse_lazy("allstudent")
