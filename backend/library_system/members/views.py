from django.shortcuts import render, redirect, get_object_or_404
from .models import Member

def member_list(request):
    members = Member.objects.all()
    return render(request, "members/member_list.html", {"members": members})

def add_member(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]

        Member.objects.create(name=name, email=email, phone=phone)
        return redirect("member_list")

    return render(request, "members/add_member.html")

def edit_member(request, pk):
    member = get_object_or_404(Member, id=pk)

    if request.method == "POST":
        member.name = request.POST["name"]
        member.email = request.POST["email"]
        member.phone = request.POST["phone"]
        member.save()
        return redirect("member_list")

    return render(request, "members/edit_member.html", {"member": member})

def delete_member(request, pk):
    member = get_object_or_404(Member, id=pk)
    member.delete()
    return redirect("member_list")