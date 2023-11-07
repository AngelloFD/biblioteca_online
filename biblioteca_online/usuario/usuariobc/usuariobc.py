from usuario.usuariodalc.usuariodalc import DALC_GetusuariobyUser,DALC_CheckUsuarioDNI,DALC_Updateusuariodata
from usuario.models import Usuario,User
from django.db import DatabaseError
from django.contrib import messages

def BC_GetusuariobyUser(user:User)->Usuario:
    return DALC_GetusuariobyUser(user)

def BC_CheckUsuarioDNI(usuario:Usuario)->bool:
    return DALC_CheckUsuarioDNI(usuario)

def BC_Updateusuariodata(user)->bool:
    try:
        DALC_Updateusuariodata(user)
    except DatabaseError:
        messages.success(f"No se pudo actualizar: {user} no es válido")