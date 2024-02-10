from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from .models import AidName, FeeAid
from django.urls import reverse_lazy

# from django.http import HttpResponseBadRequest
from django.http import Http404, HttpResponse


class CreateAid(CreateView):
    model = AidName
    fields = "__all__"
    success_url = reverse_lazy("allstudent")


class ListAid(ListView):
    model = AidName


def deleteaid(request, id):
    try:
        deleteaid = AidName.objects.get(pk=id).delete()
    except AidName.DoesNotExist:
        return render(request, "aid/aid_not_found.html")
    return render(request, "aid/aidname_confirm_delete.html", {"deleteaid": deleteaid})


class CreateFeeAid(CreateView):
    model = FeeAid
    fields = "__all__"


class ListFeeAid(ListView):
    model = FeeAid


def deletefeeaid(request, id):
    try:
        deletefeeaid = FeeAid.objects.get(pk=id).delete()
    except AidName.DoesNotExist:
        return render(request, "aid/feeaid_not_found.html")
    return render(
        request, "aid/feeaid_confirm_delete.html", {"deletefeeaid": deletefeeaid}
    )
