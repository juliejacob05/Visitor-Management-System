from django.shortcuts import render, redirect, get_object_or_404
from .models import Visitor

def add_visitor(request):
    if request.method == "POST":
        Visitor.objects.create(
            name=request.POST.get("name"),
            phone=request.POST.get("phone"),
            purpose=request.POST.get("purpose"),
            person_to_meet=request.POST.get("person_to_meet"),
        )
        return redirect("visitor_list")

    return render(request, "add_visitor.html")


def visitor_list(request):
    visitors = Visitor.objects.all().order_by('-date', '-time')
    return render(request, "visitor_list.html", {"visitors": visitors})


def delete_visitor(request, id):
    visitor = get_object_or_404(Visitor, id=id)
    visitor.delete()
    return redirect("visitor_list")

def edit_visitor(request,id):
    visitor = Visitor.objects.get(id=id)