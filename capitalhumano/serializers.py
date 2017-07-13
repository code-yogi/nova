
# Librerias Django
from rest_framework import serializers

# Librerias Python:
import sys
import json

# Modelos
from .models import PerfilPuestoDocumento
from .models import Archivo
from .models import TipoDocumento
from .models import DocumentoPersonal
from .models import DocumentoCapacitacion
from .models import Curso
from ebs.models import VIEW_EMPLEADOS_FULL

from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import resolve
from rest_framework.fields import Field
from django.urls import reverse
from django.http import Http404
from django.core.exceptions import MultipleObjectsReturned
from django.core.exceptions import ObjectDoesNotExist
from generic_relations.relations import GenericRelatedField


class PerfilPuestoDocumentoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PerfilPuestoDocumento
        fields = (
            'pk',
            'empleado_puesto_desc',
            'reporta',
            'proposito',
            'funciones',
            'responsabilidades',
            'reporte',
            'edad_minima',
            'edad_maxima',
            'nivel_estudio',
            'estado_civil',
            'genero',
            'cambio_residencia',
            'disponibilidad_viajar',
            'requerimentos',
        )


class DocumentoPersonalSerializers(serializers.HyperlinkedModelSerializer):
    tipo_documento = serializers.PrimaryKeyRelatedField(
        queryset=TipoDocumento.objects.all())

    class Meta:
        model = DocumentoPersonal
        fields = (
            'pk',
            'numero_empleado',
            'tipo_documento',
            'agrupador',
            'vigencia_inicio',
            'vigencia_fin',
            'created_by',
        )


class DocumentoCapacitacionSerializers(serializers.HyperlinkedModelSerializer):
    curso = serializers.PrimaryKeyRelatedField(
        queryset=Curso.objects.all())

    class Meta:
        model = DocumentoCapacitacion
        fields = (
            'pk',
            'numero_empleado',
            'curso',
            'proveedor',
            'modalidad',
            'lugar',
            'costo',
            'moneda',
            'departamento',
            'fecha_inicio',
            'fecha_fin',
            'duracion',
            'observaciones',
            'agrupador',
            'area',
            'created_by',
        )


# /api-capitalhumano/documentopersonal/64/
class ArchivoSerializers(serializers.HyperlinkedModelSerializer):
    content_object = GenericRelatedField({
        DocumentoPersonal: serializers.HyperlinkedRelatedField(
            queryset=DocumentoPersonal.objects.all(),
            view_name='documentopersonal-detail',
        ),
        DocumentoCapacitacion: serializers.HyperlinkedRelatedField(
            queryset=DocumentoCapacitacion.objects.all(),
            view_name='documentocapacitacion-detail',
        )
    })

    class Meta:
        model = Archivo
        fields = (
            'pk',
            'tipo_archivo',
            'archivo',
            'content_object',
            'created_by',
        )


class ArchivoPersonalSerializer(serializers.HyperlinkedModelSerializer):
    numero_empleado = serializers.SerializerMethodField()
    tipo_documento = serializers.SerializerMethodField()
    agrupador = serializers.SerializerMethodField()
    vigencia_inicio = serializers.SerializerMethodField()
    vigencia_fin = serializers.SerializerMethodField()
    tipo_archivo = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()

    class Meta:
        model = Archivo
        fields = (
            'numero_empleado',
            'tipo_documento',
            'agrupador',
            'vigencia_inicio',
            'vigencia_fin',
            'tipo_archivo',
            'pk',
            'archivo',
            'object_id',
            'created_by',
            'created_date',
            'updated_by',
            'updated_date',
        )

    def get_numero_empleado(self, obj):
        try:
            return obj.content_object.numero_empleado
        except Exception as e:
            print str(e)
            return ""

    def get_tipo_documento(self, obj):
        try:
            return obj.content_object.tipo_documento.tipo_documento
        except Exception as e:
            print str(e)
            return " "

    def get_tipo_archivo(self, obj):
        try:
            tipo = ''
            if obj.tipo_archivo == 'per':
                tipo = 'Personal'
            elif obj.tipo_archivo == 'cap':
                tipo = 'Capacitacion'
            return tipo
        except Exception as e:
            print str(e)
            return " "

    def get_agrupador(self, obj):
        try:
            agrupador = ''
            if obj.content_object.agrupador == 'per':
                agrupador = 'Personal'
            elif obj.content_object.agrupador == 'qhse':
                agrupador = 'QHSE'
            elif obj.content_object.agrupador == 'amo':
                agrupador = 'Amonestacion'
            elif obj.content_object.agrupador == 'adm':
                agrupador = 'Administracion'
            elif obj.content_object.agrupador == 'ope':
                agrupador = 'Operaciones'
            elif obj.content_object.agrupador == 'rec':
                agrupador = 'Reconocimiento'
            return agrupador
        except Exception as e:
            print str(e)
            return " "

    def get_vigencia_inicio(self, obj):
        try:
            if obj.content_object.vigencia_inicio is None:
                return '---'
            else:
                return obj.content_object.vigencia_inicio.strftime('%d/%m/%Y')
        except Exception as e:
            print str(e)
            return " "

    def get_vigencia_fin(self, obj):
        try:
            if obj.content_object.vigencia_fin is None:
                return '---'
            else:
                return obj.content_object.vigencia_fin.strftime('%d/%m/%Y')
        except Exception as e:
            print str(e)
            return " "

    def get_created_by(self, obj):
        try:
            return obj.created_by.usuario.get_full_name()
        except Exception as e:
            print str(e)
            return " "

    def get_updated_by(self, obj):
        try:
            return obj.updated_by.usuario.get_full_name()
        except Exception as e:
            print str(e)
            return " "


class ArchivoCapacitacionSerializer(serializers.HyperlinkedModelSerializer):
    numero_empleado = serializers.SerializerMethodField()
    agrupador = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()
    curso = serializers.SerializerMethodField()
    proveedor = serializers.SerializerMethodField()
    modalidad = serializers.SerializerMethodField()
    lugar = serializers.SerializerMethodField()
    costo = serializers.SerializerMethodField()
    moneda = serializers.SerializerMethodField()
    departamento = serializers.SerializerMethodField()
    fecha_inicio = serializers.SerializerMethodField()
    fecha_fin = serializers.SerializerMethodField()
    duracion = serializers.SerializerMethodField()
    observaciones = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    updated_by = serializers.SerializerMethodField()

    class Meta:
        model = Archivo
        fields = (
            'pk',
            'numero_empleado',
            'agrupador',
            'area',
            'curso',
            'proveedor',
            'modalidad',
            'lugar',
            'costo',
            'moneda',
            'departamento',
            'fecha_inicio',
            'fecha_fin',
            'duracion',
            'observaciones',
            'tipo_archivo',
            'archivo',
            'object_id',
            'created_by',
            'created_date',
            'updated_by',
            'updated_date',
        )

    def get_numero_empleado(self, obj):
        try:
            return obj.content_object.numero_empleado
        except Exception as e:
            print str(e)
            return ""

    def get_agrupador(self, obj):
        try:
            agrupador = ''
            if obj.content_object.agrupador == 'per':
                agrupador = 'Personal'
            elif obj.content_object.agrupador == 'qhse':
                agrupador = 'QHSE'
            elif obj.content_object.agrupador == 'amo':
                agrupador = 'Amonestacion'
            elif obj.content_object.agrupador == 'adm':
                agrupador = 'Administracion'
            elif obj.content_object.agrupador == 'ope':
                agrupador = 'Operaciones'
            elif obj.content_object.agrupador == 'rec':
                agrupador = 'Reconocimiento'
            return agrupador
        except Exception as e:
            print str(e)
            return " "

    def get_area(self, obj):
        try:
            area = ''
            if obj.content_object.area == 'administrativa':
                area = 'Administrativa'
            elif obj.content_object.area == 'operativa':
                area = 'Operativa'
            return area
        except Exception as e:
            print str(e)
            return " "

    def get_curso(self, obj):
        try:
            return obj.content_object.curso.nombre_curso
        except Exception as e:
            print str(e)
            return " "

    def get_proveedor(self, obj):
        try:
            return obj.content_object.proveedor
        except Exception as e:
            print str(e)
            return " "

    def get_modalidad(self, obj):
        try:
            titulo = ''
            if obj.content_object.modalidad == 'pre':
                titulo = 'Presencial'
            elif obj.content_object.modalidad == 'vir':
                titulo = 'Virtual'
            elif obj.content_object.modalidad == 'prev':
                titulo = 'Previo'
            return titulo
        except Exception as e:
            print str(e)
            return " "

    def get_lugar(self, obj):
        try:
            return obj.content_object.lugar
        except Exception as e:
            print str(e)
            return " "

    def get_costo(self, obj):
        try:
            return obj.content_object.costo
        except Exception as e:
            print str(e)
            return " "

    def get_moneda(self, obj):
        try:
            moneda = ''
            if obj.content_object.moneda == 'mxn':
                moneda = 'Moneda nacional'
            elif obj.content_object.moneda == 'usd':
                moneda = 'Dolares'
            elif obj.content_object.moneda == 'eur':
                moneda = 'Euros'
            return moneda
        except Exception as e:
            print str(e)
            return " "

    def get_departamento(self, obj):
        try:
            return obj.content_object.departamento
        except Exception as e:
            print str(e)
            return " "

    def get_fecha_inicio(self, obj):
        try:
            return obj.content_object.fecha_inicio.strftime('%d/%m/%Y')
        except Exception as e:
            print str(e)
            return " "

    def get_fecha_fin(self, obj):
        try:
            return obj.content_object.fecha_fin.strftime('%d/%m/%Y')
        except Exception as e:
            print str(e)
            return " "

    def get_duracion(self, obj):
        try:
            return obj.content_object.duracion
        except Exception as e:
            print str(e)
            return " "

    def get_observaciones(self, obj):
        try:
            return obj.content_object.observaciones
        except Exception as e:
            print str(e)
            return " "

    def get_tipo_archivo(self, obj):
        try:
            tipo = ''
            if obj.tipo_archivo == 'per':
                tipo = 'Personal'
            elif obj.tipo_archivo == 'cap':
                tipo = 'Capacitacion'
            return tipo
        except Exception as e:
            print str(e)
            return " "

    def get_created_by(self, obj):
        try:
            return obj.created_by.usuario.get_full_name()
        except Exception as e:
            print str(e)
            return " "

    def get_updated_by(self, obj):
        try:
            return obj.updated_by.usuario.get_full_name()
        except Exception as e:
            print str(e)
            return " "


class VIEW_ORGANIGRAMA_ORG_SERIALIZADO(object):

    def get_Descendencia(self, _daddies, _hijos, _nodo_jefe_nombre_completo):

        lista_descendencia = []

        for hijo in _hijos:

            nodo = {}
            hijos = []

            for persona in _daddies:
                if persona.jefe_nombre_completo == hijo.pers_nombre_completo:
                    hijos.append(persona)

                self.get_Estructura(nodo, hijo)

            if len(hijos):
                self.get_ColorNivel(nodo, hijo)
                nodo["children"] = self.get_Descendencia(_daddies, hijos, nodo)
            else:
                if hijo.tipo == 'STAFF':
                    nodo["staff"] = 'STAFF'
                    nodo["className"] = 'staff-level'
                else:
                    self.get_ColorNivel(nodo, hijo)

            lista_descendencia.append(nodo)

        return lista_descendencia

    def get_Json(self, _daddies):

        sys.setrecursionlimit(1500)

        hijos = []
        nodo = {}
        padre = self.get_Padre(_daddies)

        for dato in padre:
            for persona in _daddies:
                if persona.jefe_nombre_completo == dato.pers_nombre_completo:
                    hijos.append(persona)

        if len(hijos):
            for dato in padre:
                self.get_Estructura(nodo, dato)
                if dato.pers_empleado_numero == '200817':
                    nodo["className"] = 'nivel-1'
                else:
                    nodo["className"] = 'niveles'
            nodo["children"] = self.get_Descendencia(_daddies, hijos, nodo)
        else:
            self.get_Estructura(nodo, padre)
            self.get_ColorNivel(nodo, padre)

        lista_json = json.dumps(nodo)

        return lista_json

    def get_Estructura(self, _nodo, _datos):
        _nodo["nombre"] = "%s" % (_datos.pers_nombre_completo)
        _nodo["num_empleado"] = "%s" % (_datos.pers_empleado_numero)
        _nodo["compania"] = "%s" % (_datos.grup_compania_jde)
        _nodo["departamento"] = "%s" % (_datos.asig_organizacion_desc)
        _nodo["puesto"] = "%s" % (_datos.asig_puesto_desc)
        _nodo["centro_costos"] = "%s" % (_datos.grup_fase_jde)
        _nodo["ubicacion"] = "%s" % (_datos.asig_ubicacion_desc)

    def get_ColorNivel(self, _nodo, _dato):
        if _dato.nivel_estructura == 1:
            _nodo["className"] = 'nivel-1'
        elif (_dato.nivel_estructura == 2) or \
                (_dato.nivel_estructura == 3) or \
                (_dato.nivel_estructura == 4) or \
                (_dato.nivel_estructura == 5) or \
                (_dato.nivel_estructura == 6):
            _nodo["className"] = 'niveles'

    def get_Padre(self, _daddies):

        nivel = 6
        personaMenorNivel = []
        personasMismoNivel = []
        personasSinJefe = []
        padre = []

        for personaNivel in _daddies:
            if personaNivel.nivel_estructura < nivel:
                nivel = personaNivel.nivel_estructura
                personaMenorNivel = personaNivel

        for persona in _daddies:
            if persona.nivel_estructura == personaMenorNivel.nivel_estructura:
                personasMismoNivel.append(persona)

        personasSinJefe = personasMismoNivel

        for personaMismo in personasMismoNivel:
            for todo in _daddies:
                if personaMismo.jefe_nombre_completo == todo.pers_nombre_completo:
                    personasSinJefe.remove(personaMismo)

        for dato in personasSinJefe:

            padre = VIEW_EMPLEADOS_FULL.objects.using('ebs_d').filter(
                pers_clave=dato.asig_jefe_directo_clave)

        return padre


class VIEW_ORGANIGRAMA_EMP_SERIALIZADO(object):

    def get_Descendencia(self, _daddies, _hijos, _nodo_jefe_nombre_completo):

        lista_descendencia = []

        for hijo in _hijos:

            nodo = {}
            hijos = []

            for persona in _daddies:
                if persona.jefe_nombre_completo == hijo.pers_nombre_completo:
                    hijos.append(persona)

                self.get_Estructura(nodo, hijo)
                self.get_ColorNivel(nodo, hijo)

            if len(hijos):
                self.get_ColorNivel(nodo, hijo)
                nodo["children"] = self.get_Descendencia(_daddies, hijos, nodo)
            else:
                if hijo.tipo == 'STAFF':
                    nodo["staff"] = 'STAFF'
                    nodo["className"] = 'staff-level'

            lista_descendencia.append(nodo)

        return lista_descendencia

    def get_Json(self, _daddies):

        sys.setrecursionlimit(1500)

        hijos = []
        nodo = {}
        padre = self.get_NivelPadre(_daddies)

        for persona in _daddies:
            if persona.jefe_nombre_completo == padre.pers_nombre_completo:
                hijos.append(persona)
                # print 'jefe'+persona.pers_nombre_completo.encode('utf-8')

        if len(hijos):
            self.get_Estructura(nodo, padre)
            self.get_ColorNivel(nodo, padre)
            nodo["children"] = self.get_Descendencia(_daddies, hijos, nodo)
        else:
            self.get_Estructura(nodo, padre)
            self.get_ColorNivel(nodo, padre)

        lista_json = json.dumps(nodo)

        return lista_json

    def get_Estructura(self, _nodo, _datos):
        _nodo["nombre"] = "%s" % (_datos.pers_nombre_completo)
        _nodo["num_empleado"] = "%s" % (_datos.pers_empleado_numero)
        _nodo["compania"] = "%s" % (_datos.grup_compania_jde)
        _nodo["departamento"] = "%s" % (_datos.asig_organizacion_desc)
        _nodo["puesto"] = "%s" % (_datos.asig_puesto_desc)
        _nodo["centro_costos"] = "%s" % (_datos.grup_fase_jde)
        _nodo["ubicacion"] = "%s" % (_datos.asig_ubicacion_desc)
        _nodo["foto"] = "' images/decoradores/no-image-user.jpg '"

    def get_ColorNivel(self, _nodo, _dato):
        if _dato.nivel_estructura == 1:
            _nodo["className"] = 'nivel-1'
        elif (_dato.nivel_estructura == 2) or \
                (_dato.nivel_estructura == 3) or \
                (_dato.nivel_estructura == 4) or \
                (_dato.nivel_estructura == 5) or \
                (_dato.nivel_estructura == 6):
            _nodo["className"] = 'niveles'

    def get_NivelPadre(self, _daddies):
        nivel = 6
        padre = _daddies[0]
        cont = 0

        for persona in _daddies:
            if persona.nivel_estructura < nivel:
                nivel = persona.nivel_estructura

        for posicion in _daddies:
            if posicion.nivel_estructura == nivel:
                padre = _daddies[cont]
            cont += 1

        return padre
