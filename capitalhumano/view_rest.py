
# Librerias de Terceros

# Django API Rest:
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

# Librerias Propias

# Modelos:
from .models import PerfilPuestoDocumento
from .models import DocumentoPersonal
from .models import DocumentoCapacitacion
from .models import Archivo


# Serializadores:
from .serializers import PerfilPuestoDocumentoSerializer
from .serializers import DocumentoPersonalSerializers
from .serializers import ArchivoPersonalSerializer
from .serializers import ArchivoCapacitacionSerializer
from .serializers import ArchivoSerializers
from .serializers import DocumentoCapacitacionSerializers

# Paginadores:
from .pagination import GenericPagination

# Filtros:
from .filters import PerfilpuestoDocumentoFilter
from .filters import ArchivoPersonalFilter
from .filters import ArchivoCapacitacionFilter


# -------------- DOCUMENTO PERFIL PUESTOS - API REST -------------- #

class VIEW_DOCUMENTO_PERFIL_PUESTO_ByPageAPI(viewsets.ModelViewSet):
    queryset = PerfilPuestoDocumento.objects.all()
    serializer_class = PerfilPuestoDocumentoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = PerfilpuestoDocumentoFilter
    pagination_class = GenericPagination
    permission_classes = (IsAuthenticated,)


class DocumentoPersonalAPI(viewsets.ModelViewSet):
    queryset = DocumentoPersonal.objects.all()
    serializer_class = DocumentoPersonalSerializers


class DocumentoCapacitacionAPI(viewsets.ModelViewSet):
    queryset = DocumentoCapacitacion.objects.all()
    serializer_class = DocumentoCapacitacionSerializers


class ArchivoAPI(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializers


class ArchivoPersonalByPageAPI(viewsets.ModelViewSet):
    queryset = Archivo.objects.filter(tipo_archivo='per')
    serializer_class = ArchivoPersonalSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = ArchivoPersonalFilter


class ArchivoCapacitacionByPageAPI(viewsets.ModelViewSet):
    queryset = Archivo.objects.filter(tipo_archivo='cap')
    serializer_class = ArchivoCapacitacionSerializer
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filter_class = ArchivoCapacitacionFilter
