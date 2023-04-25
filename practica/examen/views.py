from django.shortcuts import render

# Create your views here.

from .models import Opcion, Pregunta, Alumno, Nota

def index(request):
    lista_preguntas = Pregunta.objects.all()
    context={
        'preguntas':lista_preguntas
    }
    return render(request, 'index.html', context)

def resolver(request):
    preguntas = Pregunta.objects.all()
    nota = 0
    for pregunta in preguntas:
        nota +=  int(request.POST['pregunta_'+str(pregunta.id)])

    context = {
        'nota':nota
    }

    return render(request,'resultados.html', context)

def registro(request):
    data_nota = request.POST['nota']
    data_nombre = request.POST['nombre']
    data_email = request.POST['email']

    objAlumno = Alumno.objects.create(
        nombre = data_nombre,
        email = data_email
    )

    objNota = Nota()
    objNota.alumno = objAlumno
    objNota.nota = int(data_nota)
    objNota.save()
    
    context = {
        'notas':Nota.objects.all()
    }

    return render(request, 'posiciones.html', context)