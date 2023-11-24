def separar_ids(cadena):
    ids_separadas = cadena.split(',')
    ids_sin_espacios = [id.strip() for id in ids_separadas]
    return ids_sin_espacios