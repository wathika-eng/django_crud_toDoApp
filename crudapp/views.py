from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Tag
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Test view
def test_view(request):
    return HttpResponse("Hello, world!")


def landing_page(request):
    return render(request, "base.html")


@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user, deleted_at__isnull=True)

    priority = request.GET.get("priority")
    if priority:
        notes = notes.filter(priority=priority)

    tag_id = request.GET.get("tag")
    if tag_id:
        notes = notes.filter(tags__id=tag_id)
    filter_status = request.GET.get("filter", "all")
    if filter_status == "completed":
        notes = notes.filter(is_completed=True)
    elif filter_status == "incomplete":
        notes = notes.filter(is_completed=False)

    search_query = request.GET.get("search", "")
    if search_query:
        notes = notes.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
        )

    sort_by = request.GET.get("sort", "created_at")
    if sort_by == "due_date":
        notes = notes.order_by("due_date")
    elif sort_by == "is_completed":
        notes = notes.order_by("is_completed")
    else:
        notes = notes.order_by("created_at")

    return render(
        request, "note_list.html", {"notes": notes, "search_query": search_query}
    )


@login_required
def note_detail(request, note_id):
    note = get_object_or_404(
        Note, id=note_id, user=request.user, deleted_at__isnull=True
    )
    return render(request, "note_detail.html", {"note": note})


@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            form.save_m2m()
            return redirect("note_list")
    else:
        form = NoteForm()
    return render(request, "note_form.html", {"form": form})


@login_required
def note_update(request, note_id):
    note = get_object_or_404(
        Note, id=note_id, user=request.user, deleted_at__isnull=True
    )
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_detail", note_id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, "note_form.html", {"form": form})


@login_required
def note_check_off(request, note_id):
    note = get_object_or_404(
        Note, id=note_id, user=request.user, deleted_at__isnull=True
    )
    note.is_completed = not note.is_completed
    note.save()
    return redirect("note_list")


@login_required
def note_delete(request, note_id):
    note = get_object_or_404(
        Note, id=note_id, user=request.user, deleted_at__isnull=True
    )
    if request.method == "POST":
        note.deleted_at = timezone.now()
        note.save()
        return redirect("note_list")
    return render(request, "note_confirm_delete.html", {"note": note})


@login_required
def trash_list(request):
    trash_notes = Note.objects.filter(user=request.user, deleted_at__isnull=False)
    return render(request, "trash_list.html", {"notes": trash_notes})


@login_required
def note_restore(request, note_id):
    note = get_object_or_404(
        Note, id=note_id, user=request.user, deleted_at__isnull=False
    )
    note.deleted_at = None
    note.save()
    return redirect("trash_list")


@login_required
def note_permanent_delete(request, note_id):
    note = get_object_or_404(
        Note, id=note_id, user=request.user, deleted_at__isnull=False
    )
    if request.method == "POST":
        note.delete()
        return redirect("trash")
    return render(request, "note_permanent_delete.html", {"note": note})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("note_list")
    else:
        form = UserCreationForm()
    return render(request, "account/signup.html", {"form": form})


class CustomLoginView(LoginView):
    template_name = "account/login.html"


def logout_view(request):
    logout(request)
    return redirect("login")


def error_404(request, exception):
    return redirect("note_list", status=404)
