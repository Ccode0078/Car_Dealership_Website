from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Fetch a particular Query request from views
urlpatterns = [
    path('listings/', views.listings, name='listings'),  # Home page or main listings page
    path('', views.index, name='index'),
    path('create/', views.create_listing, name='create_listing'),
    path('listing-detail/<int:id>/', views.listing_detail, name='listing_detail'),  # Detail view of a listing
    path('listing/<id>/', views.listing, name='listing'),  # Alternative listing view
    path('update/<id>/', views.update, name='update'),
    path('delete/<id>/', views.delete, name='delete'),
    path('car_details/<int:pk>/', views.car_details, name='car_details'),
    path('carousel-test/', views.carousel_test, name='carousel_test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Allows to view uploaded media files without configuring a separate media server
# Django automatically handles media files, so it can test functionality without setting up a dedicated media server.
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   
