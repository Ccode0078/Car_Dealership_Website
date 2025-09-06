from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listings/', views.listings, name='listings'),
    path('car_details/<int:id>/', views.car_details, name='car_details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


























# # listings/urls.py
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from . import views

# urlpatterns = [
#     path('', views.index, name='index'),                    # homepage
#     path('listings/', views.listings, name='listings'),     # list page
#     path('car_details/<int:id>/', views.car_details, name='car_details'),  # detail page
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# # Only serve /static in dev
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

   
