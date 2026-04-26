from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone
from books.models import Book
from members.models import Member
from .models import Borrow
from datetime import timedelta

def borrow_book(request, book_id, member_id):
    book = get_object_or_404(Book, id=book_id)
    member = get_object_or_404(Member, id=member_id)

    Borrow.objects.create(
        book=book,
        member=member,
        due_date=timezone.now().date() + timedelta(days=7)
    )

    book.available -= 1
    book.save()

    return redirect("borrow_list")

def return_book(request, borrow_id):
    borrow = get_object_or_404(Borrow, id=borrow_id)

    borrow.returned = True
    borrow.return_date = timezone.now()
    borrow.save()

    book = borrow.book
    book.available += 1
    book.save()

    return redirect("borrow_list")

def save(self, *args, **kwargs):
    if not self.due_date:
        self.due_date = self.borrow_date + timedelta(days=7)
        super().save(*args, **kwargs)

overdue = Borrow.objects.filter(
    returned=False,
    due_date__lt=timezone.now().date()
)