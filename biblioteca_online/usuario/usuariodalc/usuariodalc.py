from usuario.models import Usuario,User
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

def DALC_GetusuariobyUser(users:User)->Usuario:
    try:
        usuario:Usuario
        usuario = Usuario.objects.get(user=users)
        print(f"Usuario en DALC -> {usuario}")
        return usuario
    except ObjectDoesNotExist:
        raise f"Error en DALC_GetusuariobyUser -> {ObjectDoesNotExist}"
    except MultipleObjectsReturned:
        raise f"Error en DALC_GetusuariobyUser -> {MultipleObjectsReturned}"

def DALC_CheckUsuarioDNI(usuario:Usuario)->bool:
        return usuario.dni is not None 
    

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

