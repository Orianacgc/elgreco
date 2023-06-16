from bd import obtener_conexion


def insertar_estado(descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO estado(descripcion) VALUES (%s)",
                       (descripcion))
    conexion.commit()
    conexion.close()


def obtener_estado():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idestado,descripcion  FROM estado")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_estado(idestado):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM estado WHERE idestado = %s", (idestado,))
    conexion.commit()
    conexion.close()


def obtener_estado_por_id(idestado):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idestado,descripcion FROM estado WHERE idestado = %s", (idestado,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_rol_estado(idestado,descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE estado SET  descripcion = %s WHERE idestado = %s",
                       (idestado,descripcion))
    conexion.commit()
    conexion.close()





  