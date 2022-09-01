from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib import messages
from users.forms import UserForm, UserProfileForm


from django.contrib.auth.forms import AuthenticationForm



# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def user_logout(request):
    logout(request)
    return redirect("home")

def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()
    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)
        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            # form_profile.save()
            profile = form_profile.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "Register successful")
            login(request,user)

            return redirect('home')

    context = {
        'form_profile': form_profile,
        'form_user' : form_user
    }
    return render(request, "users/register.html", context)


def user_login(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        user = form.get_user()
        messages.success(request, "Login successful")
        login(request,user)
        return redirect('home')

    return render(request, 'users/user_login.html', {'form' : form})