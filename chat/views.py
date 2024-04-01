# from django.shortcuts import render, redirect
# from chat.models import Room, Message
# from django.http import HttpResponse, JsonResponse

# # Create your views here.
# def home(request):
#     return render(request, 'home.html')


# def room(request, room):
#     username = request.GET['username']
#     room_details = Room.objects.get(name=room)
#     return render(request, 'room.html', {
#         'username':username,
#         'room_details':room_details,
#         'room':room
#     })


# def checkview(request):
#     room = request.POST['room_name']
#     username = request.POST['username']

#     if Room.objects.filter(name=room).exists():
#         return redirect(f"/{room}/?username={username}")

#     else:
#         new_room = Room.objects.create(name=room)
#         new_room.save()
#         return redirect(f"/{room}/?username={username}")


# def send(request):
#     if request.method == 'POST':
#         message = request.POST['message']
#         username = request.POST['username']
#         room_id = request.POST['room_id']

#         new_message = Message.objects.create(value=message, user=username, room=room_id)
#         new_message.save()

#         return HttpResponse("message': 'Message sent successfully")


# def getMessages(request, room):
#     room_details = Room.objects.get(name=room)

#     messages = Message.objects.filter(room=room_details.id)
#     return JsonResponse({"messages":list(messages.values())})

# username= "admin123"
# room_details="123"
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from .forms import UserRegistrationForm

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET['username']
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username':username,
        'room_details':room_details,
        'room':room
    })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect(f"/{room}/?username={username}")

    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect(f"/{room}/?username={username}")


def send(request):
    if request.method == 'POST':
        message = request.POST['message']
        username = request.POST['username']
        room_id = request.POST['room_id']

        new_message = Message.objects.create(value=message, user=username, room=room_id)
        new_message.save()

        return HttpResponse("message': 'Message sent successfully")


def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', 'admin')
        password = request.POST.get('password', 'amin123')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Invalid login")
    return render(request, 'login.html')

def logout_view(request):
    # logout(request)
    return redirect('/')
