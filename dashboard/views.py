from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

from users.models import Profile
from .forms import ProfileUpdateForm, UserUpdateForm, EmailUpdateForm
from .models import Country, HighestDegree, Language, Specialization, SectorExperience, Job, CvTemplate
from django.contrib.auth import authenticate, update_session_auth_hash
from payment.models import Subscription, StripeWebHook
from datetime import datetime
from django.utils.timezone import make_aware
from datetime import timedelta
from django.utils import timezone
from django.db.models import Q
from users.models import Profile



@login_required
def home(request):
    if not request.user.profile.step_one_completed():
        return redirect('step_one')
    if not request.user.profile.step_two_completed():
        return redirect('step_two')
    return HttpResponse('dashboard')


@login_required
def my_profile(request):
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'dashboard/pages/profile.html', {'profile':profile})


@login_required
def my_opportunities(request):
    # time query 
    time_filter = request.GET.get('time_filter', 'all')
    if time_filter == '24':  # Last 24 hours
        filter_date = timezone.now() - timedelta(hours=24)
        jobs = Job.objects.filter(published_date__gte=filter_date)
    elif time_filter == '7':  # Last 7 days
        filter_date = timezone.now() - timedelta(days=7)
        jobs = Job.objects.filter(published_date__gte=filter_date)
    elif time_filter == '3':  # Last 3 days
        filter_date = timezone.now() - timedelta(days=3)
        jobs = Job.objects.filter(published_date__gte=filter_date)
    else:
        jobs = Job.objects.all()

    # job type query  
    job_types = request.GET.getlist('job_type')
    if job_types:
        jobs = jobs.filter(job_type__name__in=job_types)

    # specialization query
    specializations = request.GET.getlist('specializations') 
    if specializations:
        jobs = jobs.filter(specializations__name__in=specializations)

    # experience query
    min_experience = request.GET.get('experience')
    if min_experience:
        jobs = jobs.filter(experience__gte=min_experience)
    
    # search query
    search_query = request.GET.get('q')
    if search_query:
        jobs = jobs.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

     # Sort by query
    sort_by = request.GET.get('sort_by')
    if sort_by == 'relevant':
        jobs = jobs.order_by('-published_date')
    
    specialization_items = Specialization.objects.all()
    context = {
        'specialization_items': specialization_items,
        'jobs': jobs,
        'search_query': search_query
    }
    return render(request, 'dashboard/pages/my_opportunities.html', context)




@login_required
def my_plan(request):
    return render(request, 'dashboard/pages/my_plan.html')


@login_required
def billing(request):
    return render(request, 'dashboard/pages/billing.html')


@login_required
def edit_profile(request):
    countries = Country.objects.all()
    degrees = HighestDegree.objects.all()
    languages = Language.objects.all()
    specializations = Specialization.objects.all()
    sector_experiences = SectorExperience.objects.all()
    user = request.user
    profile = Profile.objects.get(user=request.user)

    user_form = UserUpdateForm(instance=user)
    profile_form = ProfileUpdateForm(instance=profile)

    if request.method == 'POST':
        if 'user_form_submit' in request.POST:
            user_form = UserUpdateForm(request.POST, instance=user)
            if user_form.is_valid():
                user_form.save()
        elif 'profile_form_submit' in request.POST:
            profile_form = ProfileUpdateForm(request.POST, instance=profile)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('dashboard_myprofile')
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'countries':countries,
        'degrees':degrees,
        'languages': languages, 
        'specializations': specializations, 
        'sector_experiences': sector_experiences,
    }
    return render(request, 'dashboard/pages/edit_profile.html', context)





def invoices_plan(request):
    stripe_invoices = StripeWebHook.objects.all()

    for webhook in stripe_invoices:
        if 'created' in webhook.checkout_response:
            created_timestamp = webhook.checkout_response['created']
            created = make_aware(datetime.fromtimestamp(created_timestamp))
            webhook.checkout_response['created'] = created
    
    return render(request, 'dashboard/pages/invoices_plan.html', {'stripe_invoices': stripe_invoices})

@login_required
def cv_templates(request):
    cv_templates = CvTemplate.objects.all
    return render(request, 'dashboard/pages/cv_templates.html',{'cv_templates': cv_templates})

# settings
@login_required
def settings(request):
    form = None  # Initialize form variable

    if request.method == 'POST':
        if 'email_form_submit' in request.POST:
            form = EmailUpdateForm(request.POST)
            if form.is_valid():
                old_email = form.cleaned_data.get('old_email')
                new_email = form.cleaned_data.get('new_email')
                password = form.cleaned_data.get('password_email')

                if old_email != request.user.email:
                    return redirect('settings')

                if not request.user.check_password(password):
                    return redirect('settings')

                if request.user.email == old_email:
                    request.user.email = new_email
                    request.user.save()
                    return redirect('dashboard_myprofile')

        elif 'password_change_submit' in request.POST:
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('dashboard_myprofile')
            else:
                messages.error(request, 'Please correct the error(s) below.')

    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'dashboard/pages/settings.html', {'form': form})
# my_rewords
@login_required
def my_rewords(request):
    return render(request, 'dashboard/pages/my_rewords.html')