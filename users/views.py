from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        #Show an empty form for registration
        form = UserCreationForm()
    else:
        #Process filled form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Aurherize the user and send him to the main page
            login(request, new_user)
            return redirect('learning_logs:index')
        
    #Show an empty or unvalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)