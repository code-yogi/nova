# -*- coding: utf-8 -*-

# Django API REST
from rest_framework import filters
from django_filters import CharFilter
# from django_filters import DateFilter
# from django_filters import NumberFilter


# Modelos:
from .models import IncidenciaDocumento


class IncidenciaDocumentoFilter(filters.FilterSet):

    empleado_zona = CharFilter(
        name="empleado_zona",
        lookup_expr="icontains"
    )

    status = CharFilter(
        name="status",
        lookup_expr="icontains"
    )

    fecha_mayorque = CharFilter(
        name='fecha_mayorque',
        method='filter_fecha_mayorque'
    )

    fecha_menorque = CharFilter(
        name='fecha_menorque',
        method='filter_fecha_menorque'
    )

    empleado_nombre = CharFilter(
        name="empleado_nombre",
        lookup_expr="icontains"
    )

    empleado_proyecto_desc = CharFilter(
        name="empleado_proyecto_desc",
        lookup_expr="icontains"
    )

    empleado_puesto_desc = CharFilter(
        name="empleado_proyecto_desc",
        lookup_expr="icontains"
    )

    empleado_organizacion  = CharFilter(
        name="empleado_organizacion",
        lookup_expr="icontains"
    )

    centro_atencion = CharFilter(
        name="centro_atencion",
        lookup_expr="icontains"
    )

    class Meta:
        model = IncidenciaDocumento
        fields = [
            'id',
            'tipo',
            'fecha_mayorque',
            'fecha_menorque',
            'es_registrable',
            'empleado_zona',
            'status',
            'empleado_nombre',
            'empleado_proyecto_desc',
            'empleado_puesto_desc',
            'empleado_organizacion',
            'centro_atencion',
        ]

    def filter_fecha_mayorque(self, queryset, name, value):

        valor = "{}T00:00:00".format(value)

        if not value:
            return queryset
        else:
            consulta = queryset.filter(fecha__gte=valor)
            return consulta

    def filter_fecha_menorque(self, queryset, name, value):

        valor = "{}T23:59:59".format(value)

        if not value:
            return queryset
        else:
            consulta = queryset.filter(fecha__lte=valor)
            return consulta
