# -*- coding: utf-8 -*-

# Django forms:
from django.forms import TextInput
from django.forms import Select
from django.forms import Form
from django.forms import CharField
from django.forms import IntegerField
from django.forms import NumberInput
from django.forms import ChoiceField
from django.forms import RadioSelect
from django.forms import CheckboxInput
from django.forms import ClearableFileInput
from django.forms import DateInput
from django.forms import DateField
from django.forms import FileField
from django.forms import Textarea

# Modelos
from jde.models import VIEW_UNIDADES
from ebs.models import VIEW_TIPO_PERSONAS
from ebs.models import VIEW_PUESTOS
from ebs.models import VIEW_ORGANIZACIONES
from ebs.models import VIEW_GRADO_ACADEMICO
from ebs.models import VIEW_COMPETENCIAS
from administracion.models import Empresa
from administracion.models import Asunto
from capitalhumano.models import PerfilPuestoDocumento
from ebs.models import VIEW_COMPANIAS
from ebs.models import VIEW_EMPLEADOS_FULL
from capitalhumano.models import PerfilIndicadores
from capitalhumano.models import EvaluacionPlantillas
from capitalhumano.models import Curso



# Business
from .business import EmpleadoBusiness


class OrganizacionesFilterForm(Form):
    organizaciones = ChoiceField(label='Organizaciones', widget=Select(
        attrs={'class': 'select2 nova-select2'}))

    def __init__(self, *args, **kwargs):
        super(OrganizacionesFilterForm, self).__init__(*args, **kwargs)
        self.fields['organizaciones'].choices = self.get_Organizaciones()

    def get_Organizaciones(self):
        valores = [('', 'TODAS LAS ORGANIZACIONES')]

        organizaciones = VIEW_ORGANIZACIONES.objects.using('ebs_p').all()
        for organizacion in organizaciones:

            valores.append(
                (
                    organizacion.clave_org,
                    str(int(organizacion.clave_org)) +
                    ' : ' + organizacion.desc_org
                )
            )
        return valores


class EmpresasFilterForm(Form):
    empresas = ChoiceField(label='Empresas', widget=Select(
        attrs={'class': 'select2 nova-select2'}))

    def __init__(self, *args, **kwargs):
        super(EmpresasFilterForm, self).__init__(*args, **kwargs)
        self.fields['empresas'].choices = self.get_Empresas()

    def get_Empresas(self):
        valores = [('', 'TODAS LAS EMPRESAS')]

        empresas = VIEW_COMPANIAS.objects.using('ebs_p').all()
        for empresa in empresas:

            valores.append(
                (
                    empresa.desc_compania,
                    empresa.desc_compania,
                )
            )
        return valores


class EmpleadoFilterForm(Form):
    GENERO = (
        ('F', 'Femenino'),
        ('M', 'Masculino'),
    )
    NOMINA = (
        ('ADMINISTRATIVA', 'Administrativa'),
        ('OPERATIVA', 'Operativa'),
    )

    pers_primer_nombre = CharField(
        label='Primer nombre',
        widget=TextInput(
            attrs={'class': 'form-control input-xs'}))

    pers_segundo_nombre = CharField(
        label='Segundo nombre',
        widget=TextInput(
            attrs={'class': 'form-control input-xs'}))

    pers_apellido_paterno = CharField(
        label='Apellido paterno',
        widget=TextInput(
            attrs={'class': 'form-control input-xs'}))

    pers_apellido_materno = CharField(
        label='Apellido materno',
        widget=TextInput(
            attrs={'class': 'form-control input-xs'}))

    pers_genero_clave = ChoiceField(
        label='Género',
        widget=RadioSelect, choices=GENERO)

    pers_empleado_numero = IntegerField(
        label='Número de empleado',
        widget=NumberInput(
            attrs={'class': 'form-control input-xs', 'min': '1'}))

    pers_tipo_codigo = ChoiceField(
        label='Tipo',
        widget=Select(
            attrs={'class': 'select2 nova-select2'}))

    asig_puesto_clave = ChoiceField(
        label='Puesto',
        widget=Select(
            attrs={'class': 'select2 nova-select2'}))

    asig_organizacion_clave = ChoiceField(
        label='Organización',
        widget=Select(
            attrs={'class': 'select2 nova-select2'}))

    # fecha_contratacion = CharField(
    #     label='Fecha de contratación',
    #     widget=TextInput(
    #         attrs={'name': 'fecha_contratacion',
    #                'class': 'form-control input-xs', 'readonly': ''}
    #     ),
    # )
    contratacion_desde = CharField(
        widget=TextInput(
            attrs={'class': 'form-control input-xs', 'readonly': 'readonly'})
    )

    contratacion_hasta = CharField(
        widget=TextInput(
            attrs={'class': 'form-control input-xs', 'readonly': 'readonly'})
    )

    grup_compania_jde = ChoiceField(
        label='Compañia',
        widget=Select(
            attrs={'class': 'select2 nova-select2'}))

    # zona = CharField(
    #     label='Zona',
    #     widget=TextInput(
    #         attrs={'class': 'form-control input-xs'}))

    grup_fase_jde = ChoiceField(
        label='Centro de costos',
        widget=Select(
            attrs={'class': 'select2 nova-select2'}))

    grup_nomina_jde = ChoiceField(
        label='Nómina',
        widget=RadioSelect, choices=NOMINA)

    def __init__(self, *args, **kwargs):
        super(EmpleadoFilterForm, self).__init__(
            *args, **kwargs)
        self.fields['pers_tipo_codigo'].choices = self.get_Tipos()
        self.fields['asig_puesto_clave'].choices = self.get_Puestos()
        self.fields['asig_organizacion_clave'].choices = self.get_Organizacion()
        self.fields['grup_compania_jde'].choices = self.get_Compania()
        self.fields['grup_fase_jde'].choices = self.get_Sucursal()

    def get_Tipos(self):

        valores = [('', '-------')]

        tipos = VIEW_TIPO_PERSONAS.objects.using('ebs_p').all()

        for tipo in tipos:

            valores.append(
                (
                    tipo.clave_tipo,
                    str(int(tipo.clave_tipo)) + ' - ' + tipo.desc_tipo,
                )
            )
        return valores

    def get_Puestos(self):

        valores = [('', '-------')]

        puestos = VIEW_PUESTOS.objects.using('ebs_p').all()

        for puesto in puestos:

            valores.append(
                (
                    puesto.clave_puesto,
                    str(int(puesto.clave_puesto)) + ' - ' + puesto.desc_puesto,
                )
            )
        return valores

    def get_Organizacion(self):

        valores = [('', '-------')]

        organizaciones = VIEW_ORGANIZACIONES.objects.using('ebs_p').all()

        for organizacion in organizaciones:

            valores.append(
                (
                    organizacion.clave_org,
                    str(int(organizacion.clave_org)) +
                    ' - ' + organizacion.desc_org,
                )
            )
        return valores

    def get_Compania(self):

        valores = [('', '-------')]

        companias = Empresa.objects.all()

        for compania in companias:

            valores.append(
                (
                    compania.descripcion_jde,
                    str(int(compania.clave)) + ' - ' + compania.descripcion,
                )
            )
        return valores

    def get_Sucursal(self):

        valores = [('', '-------')]

        unidades = VIEW_UNIDADES.objects.using('jde_p').all()

        for unidad in unidades:

            valores.append(
                (
                    unidad.clave,
                    '(' + unidad.clave + ')' + ' ' + unidad.desc_corta,
                )
            )
        return valores


class PerfilPuestoDocumentoForm(Form):

    asig_puesto_clave = ChoiceField(widget=Select(
        attrs={'class': 'select2'}))

    GENERO = (
        ('muj', 'Femenino'),
        ('hom', 'Masculino'),
        ('ind', 'Indistinto'),
    )

   
    cambio_residencia = CharField(
        label="Disponibilidad para cambiar de residencia",
        widget=CheckboxInput()
    )

    disponibilidad_viajar = CharField(
        label="Disponibilidad para viajar",
        widget=CheckboxInput(attrs={'class': 'form-checkbox inline'})
    )

    posicion = CharField(
        label="Posicion Staff",
        widget=CheckboxInput(attrs={'class': 'form-checkbox inline'})
    )

    edad_minima = CharField(
        label="Edad Minima",
        widget=TextInput(
            attrs={'class': 'form-control input-xs',
                   'placeholder': 'edad minima'}
        )
    )

    edad_maxima = CharField(
        label="Edad Maxima",
        widget=TextInput(
            attrs={'class': 'form-control input-xs',
                   'placeholder': 'edad maxima'}
        )
    )

    requerimentos = CharField(
        widget=Textarea(attrs={'class': 'form-control input-xs', 'rows': '6'}))

    objetivo = CharField(
        label="Proposito",
        widget=Textarea(attrs={'class': 'form-control input-xs', 'rows': '6'}))

    funciones = CharField(
        widget=Textarea(attrs={'class': 'form-control input-xs', 'rows': '6'}))

    responsabilidades = CharField(
        widget=Textarea(attrs={'class': 'form-control input-xs', 'rows': '6'}),
        required=False)

    desc_puesto = ChoiceField(label='Puesto', widget=Select(
        attrs={'class': 'select2'}))

    reporta = ChoiceField(label='Reporta', widget=Select(
        attrs={'class': 'select2'}))

    nivel_estudio = ChoiceField(widget=Select(
        attrs={'class': 'select2 nova-select2'}))

    estado_civil = ChoiceField(widget=Select(
        attrs={'class': 'select2 nova-select2'}))

    genero = ChoiceField(
        label='Género',
        widget=RadioSelect, choices=GENERO)

    def __init__(self, *args, **kwargs):
        super(PerfilPuestoDocumentoForm, self).__init__(
            *args, **kwargs)
        self.fields['reporta'].choices = self.get_Puestos()
        self.fields['desc_puesto'].choices = self.get_Puestos()
        self.fields['nivel_estudio'].choices = self.get_Nivel()
        self.fields['estado_civil'].choices = self.get_EstadoCivil()
        # self.fields['zona'].choices = self.get_Zonas()

    def get_Puestos(self):

        valores = [('', '-------')]

        puestos = VIEW_PUESTOS.objects.using('ebs_p').all()

        for puesto in puestos:

            valores.append(
                (
                    puesto.clave_puesto,
                    puesto.desc_puesto,
                    #str(int(puesto.clave_puesto)) + ' - ' + puesto.desc_puesto,
                )
            )
        return valores

    def get_Nivel(self):

        valores = [('', '-------')]

        niveles = VIEW_GRADO_ACADEMICO.objects.using('ebs_p').all().order_by('clave_grado')

        for nivel in niveles:

            valores.append(
                (
                    nivel.clave_grado,
                    str(int(nivel.clave_grado)) + ' - ' + nivel.desc_grado,
                )
            )
        return valores

    def get_EstadoCivil(self):

        valores = [('', '-------'), ('ind', 'Indistinto'), ('sol', 'Soltero'), ('cas', 'Casado'),
                   ('uni', 'Union Libre'), ('viu', 'Viudo'), ('div', 'Divorciado')]

        return valores


class ExpedientesFilterForm(Form):

    TIPO_CHOICES = (
        ('', '------------'),
        ('1120', 'ADMINISTRATIVO'),
        ('1123', 'EX-EMPLEADO'),
        ('1124', 'EX-EMPLEADO Y CANDIDATO'),
        ('1125', 'CONTACTO'),
        ('1118', 'CANDIDATO'),
    )

    asig_organizacion_clave = ChoiceField(
        label="Organización",
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )
    grup_fase_jde = CharField(
        label="Unidad de negocio",
        widget=TextInput(
            attrs={'class': 'form-control input-xs'}
        )
    )
    pers_empleado_numero = ChoiceField(
        label="Numero de empleado",
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )
    pers_tipo_codigo = ChoiceField(
        label="Tipo de empleado",
        choices=TIPO_CHOICES,
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )

    def __init__(self, *args, **kwargs):
        super(ExpedientesFilterForm, self).__init__(*args, **kwargs)
        self.fields[
            'asig_organizacion_clave'].choices = EmpleadoBusiness.get_Organizaciones()
        self.fields[
            'pers_empleado_numero'].choices = EmpleadoBusiness.get_Empleados()


class SolicitudesFilterForm(Form):
    STATUS = (
        ('cap', '------------'),
        ('cap', 'En captura'),
        ('act', 'Actualizado'),
        ('rech', 'Rechazado'),
        ('eli', 'Eliminado'),
    )
    asunto = ChoiceField(
        label="Asunto",
        widget=Select(attrs={'class': 'select2 nova-select2'}))

    folio = CharField(
        label="Folio",
        widget=TextInput(attrs={'class': 'form-control input-xs'}))

    numero_empleado = ChoiceField(
        label="Numero empleado",
        widget=Select(attrs={'class': 'select2 nova-select2'}))

    status = ChoiceField(
        label="Estatus",
        choices=STATUS,
        widget=Select(attrs={'class': 'select2 nova-select2'}))

    oficina = ChoiceField(
        label="Oficina",
        widget=Select(attrs={'class': 'select2 nova-select2'}))

    def __init__(self, *args, **kwargs):
        super(SolicitudesFilterForm, self).__init__(*args, **kwargs)
        self.fields['asunto'].choices = self.get_Asuntos()
        self.fields['oficina'].choices = self.get_Oficina()
        self.fields[
            'numero_empleado'].choices = EmpleadoBusiness.get_Empleados()

    def get_Asuntos(self):
        valores = [('', '------------')]

        asuntos = Asunto.objects.all()
        for asunto in asuntos:

            valores.append(
                (
                    asunto.pk,
                    asunto.nombre
                )
            )
        return valores

    def get_Oficina(self):
        valores = []

        oficinas = VIEW_EMPLEADOS_FULL.objects.using('ebs_p').all()
        for oficina in oficinas:
            valores.append((oficina.asig_ubicacion_clave,
                            oficina.asig_ubicacion_desc)
                           )
        nueva_lista = dict.fromkeys(valores).keys()
        nueva_lista.insert(0, ('', '------------'))

        return nueva_lista


class SolicitudesEditarForm(Form):
    STATUS = (
        ('cap', 'En captura'),
        ('act', 'Actualizado'),
        ('rech', 'Rechazado'),
    )

    observaciones = CharField(
        label="Observaciones:",
        widget=Textarea(attrs={'class': 'form-control input-xs', 'rows': '4'}))

    status_editar = ChoiceField(
        label="Estatus",
        choices=STATUS,
        widget=Select(attrs={'class': 'select2 nova-select2'}))

    archivo = FileField(
        label="Archivo",
        widget=ClearableFileInput(attrs={'class': 'dropzone dz-clickable dz-started', 'type': 'file', 'multiple': True}))

    def __init__(self, *args, **kwargs):
        super(SolicitudesEditarForm, self).__init__(*args, **kwargs)
        self.fields['observaciones'].required = False


class GradoAcademicoFilterForm(Form):

    GRADO_ACADEMICO_CHOICES = (
        ('', '------------'),
        ('NINGUNA', 'NINGUNA'),
        ('LEER Y ESCRIBIR', 'LEER Y ESCRIBIR'),
        ('PRIMARIA', 'PRIMARIA'),
        ('SECUNDARIA', 'SECUNDARIA'),
        ('TECNICA', 'TECNICA'),
        ('BACHILLERATO', 'BACHILLERATO'),
        ('LICENCIATURA', 'LICENCIATURA'),
        ('MAESTRIA', 'MAESTRIA'),
        ('DOCTORADO', 'DOCTORADO'),
    )
    pers_empleado_numero = ChoiceField(
        label="Numero de empleado",
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )
    qua_grado_academico = ChoiceField(
        label="Grado academico",
        choices=GRADO_ACADEMICO_CHOICES,
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )
    qua_especialidad = ChoiceField(
        label="Disciplina academica",
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )
    asig_organizacion_id = ChoiceField(
        label="Organización",
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )

    def __init__(self, *args, **kwargs):
        super(GradoAcademicoFilterForm, self).__init__(*args, **kwargs)
        self.fields[
            'asig_organizacion_id'].choices = EmpleadoBusiness.get_Organizaciones()
        self.fields['asig_organizacion_id'].required = False
        self.fields[
            'qua_especialidad'].choices = EmpleadoBusiness.get_Especialidades()
        self.fields[
            'pers_empleado_numero'].choices = EmpleadoBusiness.get_Empleados()


class DocPersonalFilterForm(Form):

    AGRUPADOR_CHOICES = (
        ('', '------------'),
        ('per', 'Personal'),
        ('med', 'Medico'),
        ('amo', 'Faltas al reglamento'),
        ('adm', 'Documentos Administrativos'),
        ('gra', 'Grados Academicos'),
        ('com', 'Comprobantes laborales'),
        ('cre', 'Credenciales'),
        ('equ', 'Equipo Asignado'),
    )
    ESTATUS = (
        ('', '------------'),
        ('ven', 'VENCIDOS'),
        ('por', 'POR VENCER'),
    )
    agrupador = ChoiceField(
        label="Agrupador",
        choices=AGRUPADOR_CHOICES,
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )
    numero_empleado = ChoiceField(
        label="Numero de empleado",
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )
    asig_organizacion_clave = ChoiceField(
        label="Organización",
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )

    tipo_documento = ChoiceField(
        label="Tipo documento",
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )
    estatus = ChoiceField(
        label="Vencimiento",
        choices=ESTATUS,
        widget=Select(attrs={'class': 'select2 nova-select2'}
                      )
    )

    def __init__(self, *args, **kwargs):
        super(DocPersonalFilterForm, self).__init__(*args, **kwargs)
        self.fields[
            'asig_organizacion_clave'].choices = EmpleadoBusiness.get_Organizaciones()
        self.fields['asig_organizacion_clave'].required = False
        self.fields[
            'tipo_documento'].choices = EmpleadoBusiness.get_TipoDocumento()
        self.fields['tipo_documento'].required = False
        self.fields[
            'numero_empleado'].choices = EmpleadoBusiness.get_Empleados()


class DocCapacitacionFilterForm(Form):

    AGRUPADOR_CHOICES = (
        ('', '------------'),
        ('per', 'Personal'),
        ('qhse', 'QHSE'),
        ('amo', 'Amonestación'),
        ('adm', 'Administración'),
        ('ope', 'Operaciones'),
        ('rec', 'Reconocimiento'),
    )
    AREA_CHOICES = (
        ('', '------------'),
        ('administrativa', 'Administrativa'),
        ('operativa', 'Operativa'),
    )
    ESTATUS = (
        ('', '------------'),
        ('ven', 'VENCIDOS'),
        ('por', 'POR VENCER'),
    )

    agrupador = ChoiceField(
        label="Agrupador",
        choices=AGRUPADOR_CHOICES,
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )
    area = ChoiceField(
        label="Area",
        choices=AREA_CHOICES,
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )
    numero_empleado = ChoiceField(
        label="Numero de empleado",
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )
    asig_organizacion_clave = ChoiceField(
        label="Organización",
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )
    curso = ChoiceField(
        label="Curso",
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )
    estatus = ChoiceField(
        label="Vencimiento",
        choices=ESTATUS,
        widget=Select(attrs={'class': 'select2 nova-select2'}
                      )
    )
    proveedor = ChoiceField(
        label="Proveedor",
        widget=Select(attrs={'class': 'select2 nova-select2'}
                      )
    )

    def __init__(self, *args, **kwargs):
        super(DocCapacitacionFilterForm, self).__init__(*args, **kwargs)
        self.fields[
            'asig_organizacion_clave'].choices = EmpleadoBusiness.get_Organizaciones()
        self.fields['asig_organizacion_clave'].required = False
        self.fields['curso'].choices = EmpleadoBusiness.get_Curso()
        self.fields['curso'].required = False
        self.fields['proveedor'].choices = EmpleadoBusiness.get_Proveedores()
        self.fields[
            'numero_empleado'].choices = EmpleadoBusiness.get_Empleados()


class NuevoPerfilForm(Form):

    archivo = FileField(
        label="Foto de perfil",
        widget=ClearableFileInput(attrs={'class': 'dropzone dz-clickable dz-started', 'type': 'file'}))


class NuevoDocumentoPersonalForm(Form):

    AGRUPADOR = (
        ('', '------------'),
        ('per', 'Personal'),
        ('med', 'Medico'),
        ('amo', 'Faltas al reglamento'),
        ('adm', 'Documentos Administrativos'),
        ('gra', 'Grados Academicos'),
        ('com', 'Comprobantes laborales'),
        ('cre', 'Credenciales'),
        ('equ', 'Equipo Asignado'),
    )

    tipo_documento = ChoiceField(
        label="Tipo documento",
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )
    agrupador = ChoiceField(
        label="Agrupador",
        choices=AGRUPADOR,
        widget=Select(attrs={'class': 'select2 nova-select2'}))

    vigencia_inicio = DateField(
        label="Vigencia",
        widget=DateInput(format=('%d/%m/%Y'),
                         attrs={'class': 'form-control input-xs'}))
    vigencia_fin = DateField(
        widget=DateInput(format=('%d/%m/%Y'),
                         attrs={'class': 'form-control input-xs'}))

    archivo = FileField(
        label="Archivo",
        widget=ClearableFileInput(attrs={'class': 'dropzone dz-clickable dz-started', 'type': 'file', 'multiple': True}))

    def __init__(self, *args, **kwargs):
        super(NuevoDocumentoPersonalForm, self).__init__(*args, **kwargs)
        self.fields['vigencia_inicio'].required = False
        self.fields['vigencia_fin'].required = False
        self.fields[
            'tipo_documento'].choices = self.get_TipoDocumento()

    def get_TipoDocumento(self):
        valores = [('', '------------')]
        return valores


class NuevoDocumentoCapacitacionForm(Form):
    MODALIDAD = (
        ('', '------------'),
        ('pre', 'Curso presencial'),
        ('vir', 'Curso virtual'),
        ('prev', 'Curso previo'),
    )
    MONEDA = (
        ('', '------------'),
        ('mxn', 'Moneda nacional (MXN)'),
        ('usd', 'Dolares (USD)'),
        ('eur', 'Euro (EUR)'),
    )
    AREA = (
        ('', '------------'),
        ('ADMINISTRATIVA', 'Administrativa'),
        ('OPERATIVA', 'Operativa'),
    )
    AGRUPADOR = (
        ('', '------------'),
        ('per', 'Personal'),
        ('qhse', 'QHSE'),
        ('amo', 'Amonestación'),
        ('adm', 'Administración'),
        ('ope', 'Operaciones'),
        ('rec', 'Reconocimiento'),
    )

    curso = ChoiceField(
        label="Curso",
        widget=Select(attrs={'class': 'select2 nova-select2'}))

    proveedor = ChoiceField(
        label="Proveedor",
        widget=Select(attrs={'class': 'select2 nova-select2'}))

    agrupadorcap = ChoiceField(
        label="Agrupador",
        choices=AGRUPADOR,
        widget=Select(attrs={'class': 'select2 nova-select2'}))

    area = ChoiceField(
        label="Area",
        choices=AREA,
        widget=Select(attrs={'class': 'select2 nova-select2'}))

    modalidad = ChoiceField(
        label="Modalidad",
        choices=MODALIDAD,
        widget=Select(attrs={'class': 'select2 nova-select2'}))

    lugar = CharField(
        label="Lugar",
        widget=TextInput(attrs={'class': 'form-control input-xs', 'placeholder': 'Veracruz, Ver.'}))

    costo = CharField(
        label="Costo",
        widget=TextInput(attrs={'class': 'form-control input-xs', 'placeholder': '10000'}))

    moneda = ChoiceField(
        label="Moneda",
        choices=MONEDA,
        widget=Select(attrs={'class': 'select2 nova-select2'}))

    fecha_inicio = DateField(
        label="Vigencia",
        widget=DateInput(format=('%d/%m/%Y'),
                         attrs={'class': 'form-control input-xs'}))
    fecha_fin = DateField(
        widget=DateInput(format=('%d/%m/%Y'),
                         attrs={'class': 'form-control input-xs'}))

    duracion = CharField(
        label="Duración(hrs)",
        widget=TextInput(attrs={'class': 'form-control input-xs', 'placeholder': '10'}))

    observaciones = CharField(
        label="Observaciones",
        widget=TextInput(attrs={'class': 'form-control input-xs', 'placeholder': 'Ninguna'}))

    archivocap = FileField(
        label="Archivo",
        widget=ClearableFileInput(attrs={'class': 'dropzone dz-clickable dz-started', 'type': 'file', 'multiple': True}))

    def __init__(self, *args, **kwargs):
        super(NuevoDocumentoCapacitacionForm, self).__init__(*args, **kwargs)

        self.fields['proveedor'].choices = EmpleadoBusiness.get_Proveedores()
        self.fields['curso'].choices = EmpleadoBusiness.get_Curso()


class PerfilAgregarPuestoCargoForm(Form):

    desc_puesto2 = ChoiceField(label='Puesto', widget=Select(
        attrs={'class': 'select2 nova-select2'}))

    nivel_estudio = ChoiceField(widget=Select())

    def __init__(self, *args, **kwargs):
        super(PerfilAgregarPuestoCargoForm, self).__init__(
            *args, **kwargs)
        self.fields['desc_puesto2'].choices = self.get_Puestos()
        self.fields['nivel_estudio'].choices = self.get_Nivel()
        # self.fields['zona'].choices = self.get_Zonas()

    def get_Puestos(self):

        valores = [('', '-------')]

        puestos = VIEW_PUESTOS.objects.using('ebs_d').all()

        for puesto in puestos:

            valores.append(
                (
                    str(int(puesto.clave_puesto)) + ' - ' + puesto.desc_puesto,
                    # puesto.clave_puesto,
                    str(int(puesto.clave_puesto)) + ' - ' + puesto.desc_puesto,
                )
            )
        return valores

    def get_Nivel(self):

        valores = [('', '-------')]

        niveles = VIEW_GRADO_ACADEMICO.objects.using('ebs_d').all()

        for nivel in niveles:

            valores.append(
                (
                    nivel.clave_grado,
                    str(int(nivel.clave_grado)) + ' - ' + nivel.desc_grado,
                )
            )
        return valores    


class PerfilPuestoListaForm(Form):

    # TIPO_ESTUDIOS = (
    #     ('ind', 'Indistinto'),
    #     ('sol', 'Soltero'),
    #     ('cas', 'Casado'),
    #     ('uni', 'Union Libre'),
    #     ('viu', 'Viudo'),
    #     ('div', 'Divorciado'),
    # )
    #
    # asig_puesto_clave = ChoiceField(widget=Select(
    #     attrs={'class': 'select2 nova-select2'}))
    #
    # class Meta:
    #     model = PerfilPuestoDocumento
    #
    #     fields = [
    #         'asig_puesto_clave',
    #         'nivel_estudio',
    #         'reporta',
    #         'areas_experiencia_id',
    #         'departamento',
    #     ]
    #
    #     labels = {
    #         'asig_puesto_clave': 'Puesto:',
    #         'nivel_estudio': 'Nivel Estudio :',
    #         'reporta': 'Reporta :',
    #         'areas_experiencia_id': 'Areas_experiencia :',
    #         'departamento': 'Departamento:',
    #     }
    #
    # asig_puesto_clave = ChoiceField(label='Puesto', widget=Select(
    #     attrs={'class': 'select2 nova-select2'}))
    #
    # reporta = ChoiceField(label='Reporta', widget=Select(
    #     attrs={'class': 'select2 nova-select2'}))
    #
    # nivel_estudio = ChoiceField(
    #     label="Nivel de Estudios",
    #     choices=TIPO_ESTUDIOS,
    #     widget=Select(
    #         attrs={'class': 'select2 nova-select2'}
    #     )
    # )
    #
    # def __init__(self, *args, **kwargs):
    #     super(PerfilPuestoListaForm, self).__init__(
    #         *args, **kwargs)
    #     self.fields['reporta'].choices = self.get_Puestos()
    #     self.fields['asig_puesto_clave'].choices = self.get_Puestos()

    TIPO_ESTUDIOS = (
        ('n0', 'Indistinto'),
        ('n1', 'Trunco'),
        ('n2', 'Pasante'),
        ('n3', 'Titulado'),
    )

    DEPARTAMENTOS = (
        ('p1', 'Seleccione'),
        ('Corporativo',
            (
                ('p1', 'Capital Humano'),
                ('p2', 'Juridico'),
                ('p3', 'Tecnologias de Informacion'),
                ('p4', 'Gestion de Calidad'),
                ('p5', 'Licitaciones')
            )
         ),
    )

    AREAS_EXPERIENCIA = (
        ('p1', 'Seleccione'),
        ('n0', 'Administracion y Finanzas'),
        ('n1', 'Administracion general'),
        ('n2', 'Auditoria'),
        ('n3', 'Finanzas'),
    )

    asig_puesto_clave = ChoiceField(
        label='Puesto',
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )

    departamento = ChoiceField(
        choices=DEPARTAMENTOS,
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )

    pertenece = CharField(
        label='Pertenece a:',
        widget=Textarea(
            attrs={'class': 'form-control input-xs', 'rows': '5'}
        )
    )

    nivel_estudio = ChoiceField(
        label="Nivel de Estudios",
        choices=TIPO_ESTUDIOS,
        widget=Select(
            attrs={'class': 'select2 nova-select2', 'id': 'id_estudios'}
        )
    )

    area_experiencia = ChoiceField(
        label="Áreas de Experiencia",
        choices=AREAS_EXPERIENCIA,
        widget=Select(
            attrs={'class': 'select2 nova-select2', 'id': 'id_experiencia'}
        )
    )

    def __init__(self, *args, **kwargs):
        super(PerfilPuestoListaForm, self).__init__(
            *args, **kwargs)
        self.fields['asig_puesto_clave'].choices = self.get_Puestos()

    def get_Puestos(self):

        valores = [('', '-------')]

        puestos = VIEW_PUESTOS.objects.using('ebs_d').all()

        for puesto in puestos:

            valores.append(
                (
                    puesto.clave_puesto,
                    str(int(puesto.clave_puesto)) + ' - ' + puesto.desc_puesto,
                )
            )
        return valores


class PerfilAgregarCompetenciaForm(Form):

    OPCIONES = (
        ('adm', 'Administrativas'),
        ('tec', 'Tecnicas'),
    )

    tipo_competencia = ChoiceField(
        label="Tipo de Competencia",
        choices=OPCIONES,
        widget=Select(
            attrs={'class': 'select2 nova-select2'}
        )
    )

    id_perfil_id = CharField(
        label="Id de Perfil",
        widget=TextInput(
            attrs={'class': 'form-control input-xs'}
        )
    )

    porcentaje = CharField(
        label="Porcentaje",
        widget=NumberInput(attrs={'class': 'form-control input-xs', 'min': '1'})
    )

    descripcion = ChoiceField(label='idcompetencia', widget=Select(
        attrs={'class': 'select2 nova-select2'}))

    def __init__(self, *args, **kwargs):
        super(PerfilAgregarCompetenciaForm, self).__init__(
            *args, **kwargs)
        self.fields['descripcion'].choices = self.get_Competencias()

    def get_Competencias(self):

        valores = [('', '-------')]

        competencias = VIEW_COMPETENCIAS.objects.using('ebs_d').all()

        for competencia in competencias:

            valores.append(
                (
                    str(int(competencia.competence_id)) +
                    ' - ' + competencia.descripcion,
                    str(int(competencia.competence_id)) +
                    ' - ' + competencia.descripcion,
                )
            )
        return valores


class PerfilAgregarIndicadorForm(Form):



    departamento = CharField(
        label="Departamento",
        widget=TextInput(
            attrs={'class': 'form-control input-xs'}
        )
    )

    puesto = CharField(
        label="Puesto",
        widget=TextInput(
            attrs={'class': 'form-control input-xs'}
        )
    )

    objetivo_ind = CharField(
        label="Objetivo",
        widget=TextInput(
            attrs={'class': 'form-control input-xs', 'placeholder': 'Escribe Brevemente'}
        )
    )

    unidad_medida = CharField(
        label="Unidad Medida",
        widget=TextInput(
            attrs={'class': 'form-control input-xs', 'placeholder': 'Ejemplo: Porcentaje'}
        )
    )

    descripcion_kpi = CharField(
        label="Descripcion KPI",
        widget=TextInput(
            attrs={'class': 'form-control input-xs', 'placeholder': 'Escribe brevemente'}
        )
    )

    porcentaje_ind = CharField(
        label="Porcentaje",
        widget=NumberInput(attrs={'class': 'form-control input-xs', 'min': '1'})
    )

    meta_minima = CharField(
        label="Meta Minima",
        widget=NumberInput(attrs={'class': 'form-control input-xs', 'min': '1'})
    )

    meta_satisfactoria = CharField(
        label="Meta Satisfactoria",
        widget=NumberInput(attrs={'class': 'form-control input-xs', 'min': '1'})
    )

    meta_excelente = CharField(
        label="Meta Excelente",
        widget=NumberInput(attrs={'class': 'form-control input-xs', 'min': '1'})
    )



# ---------------------CONFIGURACION------------------------------ 


class NuevoCursoForm(Form):

    VIGENCIA = (
        ('1', '1 año'),
        ('2', '2 años'),
        ('3', '3 años'),
        ('10', '10 años'),
        ('ind', 'Indefinido'),
    )

    nombre_curso = CharField(
        label="Nombre curso",
        widget=TextInput(attrs={'class': 'form-control input-xs'})
    )

    vencimiento = ChoiceField(
        label="Vigencia",
        choices=VIGENCIA,
        widget=Select(attrs={'class': 'select2 nova-select2'})
    )


class CursoFilterForm(Form):

    VIGENCIA = (
        ('','------------'),
        ('1', '1 año'),
        ('2', '2 años'),
        ('3', '3 años'),
        ('10', '10 años'),
        ('ind', 'Indefinido'),
    )

    nombre_curso_filter = ChoiceField(
        label="Curso",
        widget=Select(attrs={'class': 'select2 nova-select2'})
    )

    vencimiento_filter = ChoiceField(
        label="Vigencia",
        choices=VIGENCIA,
        widget=Select(attrs={'class': 'select2 nova-select2'})
    )

    def __init__(self, *args, **kwargs):
        super(CursoFilterForm, self).__init__(*args, **kwargs)
        self.fields['nombre_curso_filter'].choices = self.get_NombreCurso()

    def get_NombreCurso(self):
        valores = [('', '------------')]

        cursos = Curso.objects.all()
        for curso in cursos:

            valores.append(
                (
                    curso.pk,
                    curso.nombre_curso
                )
            )
        return valores

