import re
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Curso, Comision
# Create your views here.

def ListCurso(request):
    try:
        curso = Curso.objects.all()
        context={
            "cursos": curso
        }
        return render(request, "cursos/cursos.html", context)
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

def CreateCurso(request):
    try:
        if request.method == "POST":
            print(request.POST, request.FILES)        
            curso = Curso.objects.create(
                titulo = request.POST.get("titulo"),
                subtitulo = request.POST.get("subtitulo"),
                descripcion = request.POST.get("descripcion"),
                relevancia = request.POST.get("relevancia"),
                estado = request.POST.get("estado"),
                imagen = request.FILES.get("imagen")
            )
            return redirect("/cursos/")
        return render(request, "cursos/curso_create.html")
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

def ViewCursoId(request, pk):
    curso = Curso.objects.get(pk=pk)
    context = {
        "curso": curso 
    }
    try:
        if request.method == "POST":
            print(request.FILES.get("imagen"))
            curso.titulo = request.POST.get("titulo")
            curso.subtitulo = request.POST.get("subtitulo")
            curso.descripcion = request.POST.get("descripcion")
            if not request.FILES.get("imagen") is None:
                curso.imagen = request.FILES.get("imagen")
            curso.save()
            return redirect("/cursos/")
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
    return render(request, "cursos/curso_edit.html", context)

def DeleteCurso(request, pk):
    curso = Curso.objects.get(pk=pk)
    context ={
        "curso": curso
    }
    try:
        if request.method == "POST":
            curso.delete()
            return redirect("/cursos/")
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
    return render(request, "cursos/curso_delete.html", context)

def ComisionesView(request, slug):
    try:
        curso = Curso.objects.get(slug=slug)
        comision = Comision.objects.filter(curso_id=curso.id)
        context={
            "comisiones": comision
        }
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
    return render(request, "cursos/comisiones/comisiones.html", context)

def ComisionIdView(request, pk):
    try:
        comision = Comision.objects.get(pk=pk)
        context={
            "comision": comision
        }
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
    return render(request, "cursos/comisiones/comision_edit.html", context)