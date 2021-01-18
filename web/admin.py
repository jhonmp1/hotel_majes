from django.contrib import admin

# Register your models here.
from .models import Habitacion
from .models import Usuario
from .models import Reserva
from .models import Testimonio

admin.site.register(Habitacion)
admin.site.register(Usuario)
admin.site.register(Reserva)
admin.site.register(Testimonio)
