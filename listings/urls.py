from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
# fetch a particular Query request from views
urlpatterns = [
    path('',views.listings,name='listings'),
    path('create/',views.create,name='create'),
    path('update/<id>/',views.update,name='update'),
    path('delete/<id>/',views.delete,name='delete'),
    path('listing/<id>/',views.listing,name='listing'),
]
#allows to view uploaded media files whithout configuring a seperat media server
#Django automatically handles media files, so it can test functionality without setting up a dedicated media server.
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)