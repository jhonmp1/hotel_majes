from django import forms
from .models import Usuario
from .models import Habitacion
from .models import Reserva


class DateInput(forms.DateInput):
	input_type = 'date'


class ReservaForm(forms.ModelForm):
	Dni = forms.ModelChoiceField(queryset=Usuario.objects.all(), label='Tu DNI')
	numeroHabitacion = forms.ModelChoiceField(queryset=Habitacion.objects.all(), label='Tu Habitacion')
	numeroPersonas = forms.IntegerField(label='NumeroPersonas')
	fecha_inicio = forms.DateField(widget=DateInput)
	fecha_final = forms.DateField(widget=DateInput)
	contra = forms.CharField(label='Contraseña')

	class Meta:
		model = Reserva
		fields = ('Dni','numeroHabitacion','numeroPersonas','fecha_inicio','fecha_final','contra')