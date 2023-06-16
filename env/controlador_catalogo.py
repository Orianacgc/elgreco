from bd import obtener_conexion


def insertar_catalogo(nombre,descripcion,caracteristicas,estado,imagen):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO catalogo(nombre,descripcion,caracteristicas,estado,imagen) VALUES (%s, %s, %s,%s, %s)",
                       (nombre,descripcion,caracteristicas,estado,imagen))
    conexion.commit()
    conexion.close()


def obtener_catalogo():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idcatalogo,nombre,descripcion,caracteristicas,estado,imagen FROM catalogo")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_catalogo(idcatalogo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM catalogo WHERE idcatalogo = %s", (idcatalogo,))
    conexion.commit()
    conexion.close()


def obtener_catalogo_por_id(idcatalogo):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idcatalogo,nombre,descripcion,caracteristicas,estado,imagen FROM catalogo WHERE idcatalogo = %s", (idcatalogo,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_catalogo(idcatalogo,nombre,descripcion,caracteristicas,estado,imagen):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE catalogo SET  nombre = %s, descripcion = %s, caracteristicas = %s, estado = %s, imagen = %s WHERE idcatalogo = %s",
                       (idcatalogo,nombre,descripcion,caracteristicas,estado,imagen))
    conexion.commit()
    conexion.close()