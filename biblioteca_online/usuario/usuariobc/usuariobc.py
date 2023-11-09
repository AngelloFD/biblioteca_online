from usuario.usuariodalc.usuariodalc import DALC_GetusuariobyUser,DALC_CheckUsuarioDNI,DALC_Updateusuariodata
from usuario.models import Usuario,User
from django.db import DatabaseError
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def BC_GetusuariobyUser(user)->Usuario:
    try:
        usuario:Usuario
        usuario = DALC_GetusuariobyUser(user)
        return usuario
    except ObjectDoesNotExist:
        raise f"Error en BC_GetusuariobyUser -> {ObjectDoesNotExist}"
    except MultipleObjectsReturned:
        raise f"Error en BC_GetusuariobyUser -> {MultipleObjectsReturned}"


def BC_CheckUsuarioDNI(usuario:Usuario)->bool:
    return DALC_CheckUsuarioDNI(usuario)

def BC_Updateusuariodata(user)->bool:
    try:
        DALC_Updateusuariodata(user)
    except DatabaseError:
        messages.success(f"No se pudo actualizar: {user} no es válido")