# urls.py
from django.urls import path
from users import views

urlpatterns = [
    path('step-one/', views.step_one, name='step_one'),
    path('step-two/', views.step_two, name='step_two'),
    path('step-three/', views.step_three, name='step_three'),
    path('save_interests', views.save_interests, name='save_interests')
]
