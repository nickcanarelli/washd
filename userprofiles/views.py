from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserForm
from django.http import HttpResponseRedirect
from .models import Profile


# Create your views here.
@login_required
def logged_in(request):
    if request.user.profile.is_client:
       return render(request, "client/index.html")
    if request.user.profile.is_washr:
       return render(request, "washr/index.html")

@login_required
def profile(request):
    if request.user.profile.is_client:
       return HttpResponseRedirect("/user/editprofile")
       #return render(request, "client/profile.html")
    if request.user.profile.is_washr:
       return HttpResponseRedirect("washr/profile")
       #return render(request, "washr/profile.html")

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('settings:profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        if not Profile.objects.filter(user=request.user).exists():
                Profile.objects.create(user=request.user)
        user_form = UserForm(instance=request.user)

    return render(request, 'client/profile.html', {
        'user_form': user_form, 'user': request.user
    })
