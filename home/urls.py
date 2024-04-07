from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from home import views as home_views
from home import views

urlpatterns = [
    path('', home_views.home, name='home'),
    path('price/', views.price, name='price'),
    path('how-it-works/', views.how_it_works, name='how_it_works'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog-details/<int:blog_id>/', views.blog_details, name='blog_details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)