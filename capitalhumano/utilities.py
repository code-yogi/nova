# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
# Librerias Python
import os
from datetime import datetime

# Models
from ebs.models import VIEW_EMPLEADOS_FULL


def get_FilePath_Expedientes(instance, filename):
    fecha_hoy = datetime.now()
    numero_empleado = instance.content_object.numero_empleado
    empleado = VIEW_EMPLEADOS_FULL.objects.using(
        "ebs_p").filter(pers_empleado_numero=numero_empleado)
    nombre = ''
    for dato in empleado:
        nombre = dato.pers_nombre_completo

    upload_dir = os.path.join('capitalhumano', 'expedientes', "%s" % (nombre),)

    if instance.tipo_archivo == 'per':
        filename = "%s_%s_%s.pdf" % (instance.content_object.tipo_documento.tipo_documento, nombre, numero_empleado)
    elif instance.tipo_archivo == 'cap':
        filename = "C-%s_%s_%s.pdf" % (instance.content_object.curso.id, nombre, numero_empleado)
    elif instance.tipo_archivo == 'sol':
        fecha = '%s-%s-%s' % (fecha_hoy.day, fecha_hoy.month, fecha_hoy.year)
        filename = "%s_%s_%s.pdf" % (fecha,nombre, numero_empleado)
        return os.path.join('capitalhumano','solicitudes',filename)
    elif instance.tipo_archivo == 'res':
        fecha = '%s-%s-%s' % (fecha_hoy.day, fecha_hoy.month, fecha_hoy.year)
        filename = "R-%s_%s_%s.pdf" % (fecha,nombre, numero_empleado)
        return os.path.join('capitalhumano','solicitudes',filename)
    return os.path.join(upload_dir, filename)
 