from django.db import models

# Create your models here.
class Habitacion(models.Model):
	numeroHabitacion = models.CharField(max_length=4)
	descripcion = models.CharField(max_length=200)
	imagen = models.URLField()
	precio = models.DecimalField(max_digits=6, decimal_places=2)
	estado = models.CharField(max_length=1)


	def __str__(self):
		return self.numeroHabitacion



class Usuario(models.Model):
	Dni = models.CharField(max_length=20)
	nombre = models.CharField(max_length=200)
	correo = models.CharField(max_length=200)
	celular = models.CharField(max_length=200)

	def __str__(self):
		return self.Dni

class Reserva(models.Model):
	Dni = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	numeroHabitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
	numeroPersonas = models.IntegerField()
	fecha_inicio = models.DateField()
	fecha_final = models.DateField()
	contra = models.CharField(max_length=200)

class Testimonio(models.Model):
	imagen = models.URLField()
	usuario = models.CharField(max_length=200)
	testimonio = models.CharField(max_length=400)

	



