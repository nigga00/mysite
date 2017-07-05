from django.shortcuts import render, HttpResponse, redirect
from poll.forms import registrationform, editprofileform
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail



def home(request):
    numbers = [1,2,3,4,5,6]
    name = "Ashwar Gupta"
    arg = {'myname': name, 'nos': numbers}
    return render(request, 'poll/home.html', arg)

def reg(request):
    return render(request, 'poll/form1.html')

def register(request):
    if request.method == 'POST':
        form = registrationform(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Registration Confirmation',
                'You have been registered as a user.',
                'admin@kcti.com',
                ['ashwargupta007@gmail.com',request.POST.get("email")],
                fail_silently=False,
            )
            return redirect('/poll')

    else:
        form = registrationform()
        args = {'form': form}
        return render(request, 'poll/reg_page.html', args)

@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'poll/profile.html', args)


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = editprofileform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            return redirect('../')

    else:
        form = editprofileform(instance=request.user)
        args = {'form': form}
        return render(request, 'poll/edit.html', args)


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('http://127.0.0.1:8000/poll/profile/', permanent=True)
        else:
            return redirect('/poll/change-password/')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'poll/change_pass.html', args)

