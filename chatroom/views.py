from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from .models import Room, rds
# from .models import Room


def index(request):
    rooms_name = [room.room_name for room in Room.objects.all()]
    context = {
        'rooms': rooms_name,
    }
    return render(request, "chatroom/index.html", context)


def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('chatroom:index')
    return render(request, 'chatroom/login.html', {'form': form})


@login_required
def logout(request):
    # request.session['user']
    auth_logout(request)
    return redirect('chatroom:index')


def signup(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chatroom:login')
    context = {
        'form': form,
        'user': request.user
    }
    return render(request, "chatroom/signup.html", context)


def room(request, room_name):
    if not request.user.is_authenticated:
        return redirect('chatroom:login')
    context = {
        'user': request.user,
        'room_name': room_name,
    }
    return render(request, "chatroom/room.html", context)


def userlist(request, room_name):
    user_list = rds.smembers('userlist_%s' % room_name)
    user_list = [x.decode('utf-8') for x in user_list]
    return JsonResponse(user_list, safe=False)
