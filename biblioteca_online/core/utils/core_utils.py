from usuario.usuariobc.usuariobc import BC_CheckUsuarioDNI,BC_GetusuariobyUser
from usuario.models import Usuario,User
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
def CheckUserDNI(user:User)->bool:
    try:
        usuarios:Usuario
        usuarios = BC_GetusuariobyUser(user)
        flag:bool
        flag = BC_CheckUsuarioDNI(usuarios)
        return flag
    except ObjectDoesNotExist:
        raise f"Error en BC_GetusuariobyUser -> {ObjectDoesNotExist}"
    except MultipleObjectsReturned:
        raise f"Error en BC_GetusuariobyUser -> {MultipleObjectsReturned}"