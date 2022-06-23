from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Evento
from helpers.helpers import correccion_fecha

# Create your views here.
def ListEvents(request):
    evento = Evento.objects.all()
    context = {
        "eventos": evento
    }
    return render(request, "eventos/eventos.html", context)

def EventView(request, pk):
    evento = Evento.objects.get(pk = pk)
    context = {
        "evento": evento
    }
    try:
        print(request.POST.get("titulo"))
        if request.method == "POST":
            new_titulo = request.POST.get("titulo")
            new_subtitulo = request.POST["subtitulo"]
            new_descripcion = request.POST["descripcion"]
            new_relevancia = request.POST["relevancia"]
            new_fec_inicio = request.POST["fecha_inicio"]
            new_fec_fin = request.POST["fecha_fin"]
            new_hora_in = request.POST["hora_inicio"]
            new_hora_fin = request.POST["hora_fin"]
            if request.POST.get("estado") is None:
                evento.estado = False
            else:
                evento.estado = True
            evento.titulo= new_titulo
            evento.subtitulo = new_subtitulo
            evento.descripcion = new_descripcion
            evento.relevancia = new_relevancia
            evento.fecha_inicio = new_fec_inicio
            evento.fecha_fin = new_fec_fin
            evento.hora_inicio = new_hora_in
            evento.hora_fin = new_hora_fin
            evento.save()
            return redirect("/eventos/")
    except Exception as ex:
        trace = []
        tb = ex.__traceback__
        while tb is not None:
            trace.append({
                "filename": tb.tb_frame.f_code.co_filename,
                "name": tb.tb_frame.f_code.co_name,
                "lineno": tb.tb_lineno
            })
            tb = tb.tb_next
        msg = str({
            'type': type(ex).__name__,
            'message': str(ex),
            'trace': trace
        })
        return HttpResponse(msg)
    else:
        return render(request, "eventos/evento_edit.html", context)

def deleteEvent(request, pk):
    evento = Evento.objects.get(pk= pk)
    context = {
        "evento": evento
    }
    try:
        if request.method == "POST":
            evento.delete()
            return redirect('/eventos/')
    except Exception as ex:
        trace = []
        tb = ex.__traceback__
        while tb is not None:
            trace.append({
                "filename": tb.tb_frame.f_code.co_filename,
                "name": tb.tb_frame.f_code.co_name,
                "lineno": tb.tb_lineno
            })
            tb = tb.tb_next
        msg = str({
            'type': type(ex).__name__,
            'message': str(ex),
            'trace': trace
        })
        return HttpResponse(msg)
    return render(request, "eventos/evento_delete.html", context)

def createEvent(request):
    try:
        if request.method == "POST":
            print(request.POST, request.FILES)
            fecha_inicio_correc = correccion_fecha(request.POST.get("fecha_inicio"))
            fecha_fin_correc = correccion_fecha(request.POST.get("fecha_fin"))
            evento = Evento.objects.create(
                titulo = request.POST.get("titulo"),
                subtitulo = request.POST.get("subtitulo"),
                descripcion = request.POST.get("descripcion"),
                estado = request.POST.get("estado"),
                relevancia = request.POST.get("relevancia"),
                fecha_inicio = fecha_inicio_correc,
                fecha_fin = fecha_fin_correc,
                hora_inicio = request.POST.get("hora_inicio"),
                hora_fin = request.POST.get("hora_fin"),
                imagen = request.FILES.get("imagen")
            )
            return redirect('/eventos/')
    except Exception as ex:
        trace = []
        tb = ex.__traceback__
        while tb is not None:
            trace.append({
                "filename": tb.tb_frame.f_code.co_filename,
                "name": tb.tb_frame.f_code.co_name,
                "lineno": tb.tb_lineno
            })
            tb = tb.tb_next
        msg = str({
            'type': type(ex).__name__,
            'message': str(ex),
            'trace': trace
        })
        return HttpResponse(msg)
    return render(request, "eventos/evento_create.html")
