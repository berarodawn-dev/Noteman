from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import LoginForm, SignupForm, NoteCreationForm, TaskCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from .models import Note, Task
from django.shortcuts import get_object_or_404


from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout


def login(request: HttpRequest) -> HttpResponse:
    """
    lOGIN REQUEST HANDLER

    1. Checks if request method is POST. If POST then it authenticates
    2. If not POST, it returns the Login screen

    """

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                auth_login(request, user)
                return redirect("home")
        form.add_error(None, "Invalid username or password")

    else:
        form = LoginForm()
    return render(request, "accounts/login.html", {"form": form})


def signup(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("home")
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


@login_required
def home(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        notes = Note.objects.filter(author=request.user)
        tasks = Task.objects.filter(author=request.user)
        return render(
            request,
            "accounts/home.html",
            {"user": request.user, "notes": notes, "tasks": tasks},
        )


def logout(request: HttpRequest) -> HttpResponse:
    auth_logout(request)
    return redirect("login")


@login_required
def delete_note(request: HttpRequest, note_id: int) -> HttpResponse:
    if request.method == "POST":
        if request.user.is_authenticated:
            note = get_object_or_404(Note, id=note_id, author=request.user)
            note.delete()

    return redirect("home")


@login_required
def create_note(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        if request.method == "POST":
            form = NoteCreationForm(request.POST)
            if form.is_valid():
                note = form.save(commit=False)
                note.author = request.user
                note.save()
                return redirect("home")
        else:
            form = NoteCreationForm()
    return render(request, "accounts/create_note.html", {"form": form})


@login_required
def create_task(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author = request.user
            task.save()
            return redirect("home")

    else:
        form = TaskCreationForm()

    return render(request, "accounts/create_task.html", {"form": form})


@login_required
def delete_task(request: HttpRequest, task_id) -> HttpResponse:
    if request.method == "POST":
        (Task.objects.filter(author=request.user, id=task_id)).delete()
        return redirect("home")
    else:
        return HttpResponseNotAllowed(["POST"])
