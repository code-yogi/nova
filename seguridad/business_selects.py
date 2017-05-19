
# Librerias Django
from django.contrib.auth.models import User


def get_Usuarios():
    """ Funcion que devuelve a todos los usuarios,
        ordenados por cuenta
    """

    valores = [('', '------')]

    usuarios = User.objects.all().order_by('username')

    for usuario in usuarios:
        valores.append(
            (
                usuario.username,
                usuario.get_full_name()
            )
        )

    return valores