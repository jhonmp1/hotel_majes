from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'web'

urlpatterns = [
	path('index',views.index, name ='index'),
	path('cuarto',views.cuarto,name='cuarto'),
	path('services',views.servicios,name='services'),
	path('gallery',views.galeria,name='gallery'),
	path('testimonials',views.testimonios,name='testimonials'),
	path('booking',views.booking,name='booking'),
	url(r'^habitaciones/$', views.habitacion_list),
    url(r'^habitaciones/(?P<pk>[0-9]+)/$', views.habitacion_detail),
    url(r'^reservas/$', views.reserva_list),
    url(r'^reservas/(?P<pk>[0-9]+)/$', views.reserva_detail),

]