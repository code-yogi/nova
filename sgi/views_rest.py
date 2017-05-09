# Librerias/Clases de Terceros
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

# Librerias/Clases Propias

# Modelos:
from .models import IncidenciaDocumento
from .models import IncidenciaTipo
from .models import CentroAtencion
from .models import IncidenciaArchivo
from .models import IncidenciaResolucion

# Otros Modelos:
from ebs.models import VIEW_EMPLEADOS_FULL
from administracion.models import Zona
from administracion.models import Empresa

# Serializadores:
from .serializers import IncidenciaDocumentoSerializer
from .serializers import IncidenciaTipoSerializer
from .serializers import CentroAtencionSerializer
from .serializers import IncidenciaArchivoSerializer
from .serializers import IncidenciaResolucionSerializer

# Filtros:
from home.pagination import GenericPagination

# Paginacion:
from .filters import IncidenciaDocumentoFilter
from .filters import IncidenciaDocumentoFilter
from .filters import IncidenciaArchivoFilter
from .filters import IncidenciaResolucionFilter


# -------------- INCIDENCIA DOCUMENTO - API REST -------------- #

class IncidenciaDocumentoAPI(viewsets.ModelViewSet):
    queryset = IncidenciaDocumento.objects.all()
    serializer_class = IncidenciaDocumentoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = IncidenciaDocumentoFilter


class IncidenciaDocumentoByPageAPI(viewsets.ModelViewSet):
    queryset = IncidenciaDocumento.objects.all()
    serializer_class = IncidenciaDocumentoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = IncidenciaDocumentoFilter
    pagination_class = GenericPagination

# -------------- INCIDENCIA ANEXO - API REST -------------- #


class IncidenciaArchivoByPageAPI(viewsets.ModelViewSet):
    queryset = IncidenciaArchivo.objects.all()
    serializer_class = IncidenciaArchivoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = IncidenciaArchivoFilter
    pagination_class = GenericPagination


# -------------- INCIDENCIA TIPO - API REST -------------- #

class IncidenciaTipoAPI(viewsets.ModelViewSet):
    queryset = IncidenciaTipo.objects.all()
    serializer_class = IncidenciaTipoSerializer


class CentroAtencionAPI(viewsets.ModelViewSet):
    queryset = CentroAtencion.objects.all()
    serializer_class = CentroAtencionSerializer


# -------------- INCIDENCIA RESOLUCION - API REST -------------- #

class IncidenciaResolucionAPI(viewsets.ModelViewSet):
    queryset = IncidenciaResolucion.objects.all()
    serializer_class = IncidenciaResolucionSerializer
