# Django API REST
from rest_framework import filters
from django_filters import CharFilter
# from django_filters import DateFilter

# Modelos:
from .models import ViaticoCabecera


class ViaticoCabeceraFilter(filters.FilterSet):

    proposito_viaje = CharFilter(
        name="proposito_viaje",
        lookup_expr="icontains"
    )

    empleado_clave = CharFilter(
        name="empleado_clave",
        lookup_expr="icontains"
    )

    unidad_negocio_clave = CharFilter(
        name="unidad_negocio_clave",
        lookup_expr="icontains"
    )

    ciudad_destino = CharFilter(
        name="ciudad_destino",
        lookup_expr="icontains"
    )

    autorizador_clave = CharFilter(
        name="autorizador_clave",
        lookup_expr="icontains"
    )

    creacion_fecha_mayorque = CharFilter(
        label="Fecha Creacion mayor a",
        name="creacion_fecha_mayorque",
        method='filter_fecha_mayorque'
    )
    creacion_fecha_menorque = CharFilter(
        label="Fecha Creacion menor a",
        name="creacion_fecha_menorque",
        method='filter_fecha_menorque'
    )

    class Meta:
        model = ViaticoCabecera
        fields = [
            'proposito_viaje',
            'empleado_clave',
            'unidad_negocio_clave',
            'ciudad_destino',
            'autorizador_clave',
        ]

    def filter_fecha_mayorque(self, queryset, name, value):

        valor = "{}T00:00:00".format(value)

        if not value:
            return queryset
        else:
            consulta = queryset.filter(created_date__gte=valor)
            return consulta

    def filter_fecha_menorque(self, queryset, name, value):

        valor = "{}T23:59:59".format(value)

        if not value:
            return queryset
        else:
            consulta = queryset.filter(created_date__lte=valor)
            return consulta
