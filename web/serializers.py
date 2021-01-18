from rest_framework import serializers
from .models import Habitacion
from .models import Reserva

class HabitacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Habitacion
		fields = ('id','numeroHabitacion','descripcion','imagen','precio','estado')

class ReservaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reserva
		fields = '__all__'