from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from .forms import NoteForm
# from django.contrib.auth.decorators import login_required


def test_view(request):
    return HttpResponse("Hello, world!")

# @login_required
def note_list(request):
    notes =Note.objects.all()
    # newNotes = [note ]
    return render(request, 'note_list.html', {'notes': notes})

# @login_required
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'note_detail.html', {'note': note})

# @login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'note_form.html', {'form': form})


def note_update(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', note_id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_form.html', {'form': form})


def note_check_off(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.is_completed = not note.is_completed 
    note.save()
    return redirect('note_list')

# @login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        note.delete()
        return redirect('note_list')
    return render(request, 'note_confirm_delete.html', {'note': note})
