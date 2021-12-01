from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Message
from .forms import UserRegisterForm

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			firstname = form.cleaned_data.get('first_name')
			lastname = form.cleaned_data.get('last_name')
			messages.success(request, f'Account successfully created for {firstname} {lastname}.')
			return redirect('login')
	else:
		form = UserRegisterForm()
    
	return render(request, 'registration/register.html', {'form':form})

@login_required
def room(request, room_name):
    username = request.user.username
    messages = Message.objects.filter(room=room_name)[0:25]
    context = {
        'room_name': room_name, 
        'username': username,
        'messages': messages 
    }
    return render(request, 'chat/room.html', context)