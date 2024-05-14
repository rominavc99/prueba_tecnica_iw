from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'cultivos_iw'

urlpatterns = [
    path('index/', views.Index.as_view(), name='index'),
    path('', views.Index.as_view(), name='index'),
    path('edit/<int:cultivo_id>/', views.CultivoEditar.as_view(), name='edit'),  
    path('cultivo/delete/<int:cultivo_id>/', views.CultivoEliminar.as_view(), name='delete_cultivo'),
    path('cultivo/details/<int:cultivo_id>/', views.CultivoDetail.as_view(), name='cultivo_details'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)