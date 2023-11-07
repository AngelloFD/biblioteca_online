from usuario.models import Usuario,User
from django.db import DatabaseError
from django.contrib import messages

def DALC_GetusuariobyUser(user:User)->Usuario:
    Usuario(usuario)
    usuario = Usuario.objects.filter(user=user)
    return usuario

def DALC_CheckUsuarioDNI(usuario:Usuario)->bool:
    return usuario.dni is None 

#TO-DO: Angello revisa porfavor
def DALC_Updateusuariodata(user):
    try:
        Usuario.objects.filter(user=user).update(
            dni=user.dni,
            fecha_nacimiento=user.fecha_nacimiento,
            compuesto=user.compuesto,
            fecha_actualizacion=user.fecha_actualizacion,
        )
        return True
    except DatabaseError: #TO-DO: ver que excepciones tenemos que botar
        raise DatabaseError

