from django.shortcuts import render, redirect
from .models import Materia
from django.http import Http404
from django.contrib import messages

# Vista para mostrar la lista de materias
def lista_materias(request):
    materias = Materia.objects.all()
    return render(request, "app_crud_app/html/index.html", {'materias': materias})

# Vista para registrar una nueva materia
def registrarMateria(request):
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']
        foto = request.FILES['imgFoto']

        materia = Materia.objects.create(
            nombre=nombre, descripcion=descripcion, foto=foto)
        messages.success(request, 'Materia registrada')
        return redirect('/app_crud_app/')
    else:
        # Manejar la solicitud GET aquí si es necesario
        return render(request, "app_crud_app/html/index.html")

# Vista para ver los detalles de una materia
def leer(request, id):
    materia = Materia.objects.get(id=id)
    return render(request, 'app_crud_app/html/leer.html', {'materia': materia})


# Vista para editar una materia
def editar(request, id):
    try:
        materia = Materia.objects.get(id=id)
    except Materia.DoesNotExist:
        raise Http404("La materia no existe")
    if request.method == 'POST':
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']
        foto = request.FILES.get('imgFoto')  # Usamos get para manejar la ausencia de 'imgFoto'
        materia.nombre = nombre
        materia.descripcion = descripcion
        # Verificamos si se proporcionó una imagen
        if foto:
            materia.foto = foto
        materia.save()
        messages.success(request, 'Materia actualizada')
        return redirect('/app_crud_app/')
    else:
        # Manejar la solicitud GET aquí si es necesario
        return render(request, "app_crud_app/html/leer.html", {"materia": materia})

# Vista para eliminar una materia
def eliminar(request, id):
    if request.method == 'POST':
        materia = Materia.objects.get(id=id)
        materia.delete()
        messages.success(request, 'Materia eliminada')
        return redirect('/app_crud_app/')
    else:
        # Si llega una solicitud GET a esta vista, redirige a donde sea apropiado
        return redirect('/app_crud_app/')  # redirige nuevamente a la lista de materias