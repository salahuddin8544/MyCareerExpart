from django.urls import path
from dashboard import views

urlpatterns = [
    path('', views.home, name='dashboard_home'),
    path('my-profile/', views.my_profile, name='dashboard_myprofile'),

    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('my_opportunities', views.my_opportunities, name='my_opportunities'),
    path('my_plan', views.my_plan, name='my_plan'),
    path('billing', views.billing, name='billing'),
    path('invoices_plan/', views.invoices_plan, name='invoices_plan'),
    path('cv_templates', views.cv_templates, name='cv_templates'),
    path('settings', views.settings, name='settings'),
    path('my_rewords', views.my_rewords, name='my_rewords'),
]
