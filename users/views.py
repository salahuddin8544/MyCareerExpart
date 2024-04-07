from django.shortcuts import redirect, render
from users.forms import StepOneForm, StepTwoForm
from django.shortcuts import render
from .models import Profile, Interest, User
from django.shortcuts import render


def step_one(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = StepOneForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            form.save_m2m() 
            return redirect('step_two')
    else:
        form = StepOneForm(instance=profile)
    return render(request, 'account/step_one.html',  {'form': form})



def step_two(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = StepTwoForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            form.save_m2m()
            return redirect('step_three')
    else:
        form = StepTwoForm(instance=profile)
    return render(request, 'account/step_two.html', {'form': form})

def step_three(request):
    interests = Interest.objects.all()
    return render(request, 'account/step_three.html', {'interests': interests})


 
def save_interests(request):
    if request.method == 'POST':
        selected_interests = request.POST.getlist('interests')
        profile = Profile.objects.get(user=request.user)
        profile.interested.clear()  
        for interest_id in selected_interests:
            interest = Interest.objects.get(id=interest_id)
            profile.interested.add(interest)
        return redirect('dashboard_myprofile')  
    return render(request, 'account/step_three.html')   

    