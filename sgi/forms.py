# -*- coding: utf-8 -*-
# Django:
from django.forms import ModelForm
from django.forms import TextInput
# from django.forms import Textarea
from django.forms import Select
# from django.forms import Form
from django.forms import CharField
from django.forms import ChoiceField
from django.forms import IntegerField
from django.forms import BooleanField

from .models import IncidenciaDocumento
from .models import IncidenciaTipo

from django import forms


class IncidenciaDocumentoFilterForm(forms.Form):

    numero = IntegerField(label="No. Documento")
    tipo = ChoiceField(widget=Select())
    fecha_mayorque = CharField()
    fecha_menorque = CharField()
    es_registrable = BooleanField()
    empleado_zona = CharField()

    def __init__(self, *args, **kwargs):
        super(IncidenciaDocumentoFilterForm, self).__init__(
            *args, **kwargs)
        self.fields['tipo'].choices = self.get_Tipos()

    def get_Tipos(self):

        valores = [('', '------')]

        tipos = IncidenciaTipo.objects.all()

        for tipo in tipos:
            valores.append(
                (
                    tipo.id,
                    tipo.descripcion
                )
            )

        return valores


class IncidenciaDocumentoForm(ModelForm):

    class Meta:
        model = IncidenciaDocumento

        fields = ['tipo',
                  'es_registrable',
                  'fecha',
                  'empleado_id',
                  'empleado_nombre',
                  'empleado_zona',
                  'empleado_proyecto',
                  'empleado_proyecto_desc',
                  'empleado_puesto',
                  'empleado_puesto_desc',
                  'empleado_un',
                  'empleado_organizacion',
                  'area_id',
                  'area_descripcion',
                  'lugar',
                  'dias_incapcidad',
                  'centro_atencion',
                  'tiene_acr',
                  'status']
        # 'created_by',
        # 'created_date',
        # 'updated_by',
        # 'updated_date' ]

        labels = {'tipo': 'Tipo',
                  'es_registrable': 'Registrable',
                  'fecha': 'Fecha',
                  'empleado_id':'Empleado id ',
                  'empleado_nombre': 'Nombre',
                  'empleado_zona': 'Zona del Empleado',
                  'empleado_proyecto': 'Proyecto id',
                  'empleado_proyecto_desc': 'Proyecto',
                  'empleado_puesto': 'Puesto_id',
                  'empleado_puesto_desc': 'Puesto',
                  'empleado_un': 'Unidad de Negocio',
                  'empleado_organizacion': 'Organizacion',
                  'area': 'Area id',
                  'area_descripcion': 'Area',
                  'lugar': 'Lugar de Incidencia',
                  'dias_incapcidad': 'Dias Incapacidad',
                  'centro_atencion': 'Centro de Atencion',
                  'tiene_acr': 'acr Analisis Raiz Causa',
                  'status': 'Estado de la solicitud',
                  }

        widgets = {'tipo': TextInput(attrs={'class': 'form-control input-xs'}),
                   'es_registrable': TextInput(attrs={'class': 'form-control input-xs'}),
                   'fecha': TextInput(attrs={'class': 'form-control input-xs'}),
                   'empleado_id': TextInput(attrs={'class': 'form-control input-xs'}),
                   'empleado_nombre': TextInput(attrs={'class': 'form-control input-xs'}),
                   'empleado_zona': TextInput(attrs={'class': 'form-control input-xs'}),
                   'empleado_proyecto': TextInput(attrs={'class': 'form-control input-xs'}),
                   'empleado_proyecto_desc': TextInput(attrs={'class': 'form-control input-xs'}),
                   'empleado_puesto': TextInput(attrs={'class': 'form-control input-xs'}),
                   'empleado_puesto_desc': TextInput(attrs={'class': 'form-control input-xs'}),
                   'empleado_un': TextInput(attrs={'class': 'form-control input-xs'}),
                   'empleado_organizacion': TextInput(attrs={'class': 'form-control input-xs'}),
                   'area': TextInput(attrs={'class': 'form-control input-xs'}),
                   'area_descripcion': TextInput(attrs={'class': 'form-control input-xs'}),
                   'lugar': TextInput(attrs={'class': 'form-control input-xs'}),
                   'dias_incapacidad': TextInput(attrs={'class': 'form-control input-xs'}),
                   'centro_atencion': TextInput(attrs={'class': 'form-control input-xs'}),
                   'tiene_acr': TextInput(attrs={'class': 'form-control input-xs'}),
                   'status': TextInput(attrs={'class': 'form-control input-xs'}),
                   }
