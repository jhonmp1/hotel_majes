from django.shortcuts import get_object_or_404,render
from .models import Habitacion
from .models import Testimonio
from .models import Reserva
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import HabitacionSerializer
from .serializers import ReservaSerializer
from .forms import ReservaForm

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def habitacion_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        habitaciones = Habitacion.objects.all()
        serializer = HabitacionSerializer(habitaciones, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HabitacionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def reserva_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        reservas = Reserva.objects.all()
        serializer = ReservaSerializer(reservas, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReservaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def habitacion_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        habitacion = Habitacion.objects.get(pk=pk)
    except Habitacion.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HabitacionSerializer(habitacion)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HabitacionSerializer(serie, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        habitacion.delete()
        return HttpResponse(status=204)

@csrf_exempt
def reserva_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        reserva = Reserva.objects.get(pk=pk)
    except Reserva.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ReservaSerializer(habitacion)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ReservaSerializer(reserva, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        reserva.delete()
        return HttpResponse(status=204)



# Create your views here.

def index(request):
	listaCuartos = Habitacion.objects.order_by('numeroHabitacion')[:6]
	context = {'listaCuartos': listaCuartos}
	return render(request, 'index.html', context)

def cuarto(request):
	habitacion = Reserva.objects.order_by('Dni')[:1]
	context = {'habitacion': habitacion}
	return render(request, 'cuarto.html', context)


def servicios(request):
	listaCuartos = Habitacion.objects.order_by('numeroHabitacion')[:3]
	context = {'listaCuartos': listaCuartos}
	return render(request, 'services.html', context)

def galeria(request):
	listaHabitaciones = Habitacion.objects
	return render(request, 'gallery.html')

def testimonios(request):
	listaTestimonios = Testimonio.objects.order_by('usuario')
	context = {'listaTestimonios': listaTestimonios}
	return render(request,'testimonials.html', context)

def booking(request):
	form = ReservaForm()
	context = {'form': form}

	if request.method == 'POST':
		form = ReservaForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			habitacion = Reserva.objects.order_by('-id')[:1]
			context = {'habitacion': habitacion}
			return render(request, 'cuarto.html', context)
		else:
			print(form.errors)

	return render(request,'booking.html', context)


