from bd import obtener_conexion


def insertar_categoria(descripcion,estado):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO categoria(descripcion,estado) VALUES (%s, %s)",
                       (descripcion,estado))
    conexion.commit()
    conexion.close()


def obtener_categoria():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idcategoria,descripcion,estado FROM categoria")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_categoria(idcategoria):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM categoria WHERE idcategoria = %s", (idcategoria,))
    conexion.commit()
    conexion.close()


def obtener_categoria_por_id(idcategoria):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idcategoria,descripcion,estado FROM categoria WHERE idcategoria = %s", (idcategoria,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_categoria(idcategoria,descripcion,estado):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE categoria SET  descripcion = %s, estado= %s  WHERE idcategoria = %s",
                       (idcategoria,descripcion,estado))
    conexion.commit()
    conexion.close()

  