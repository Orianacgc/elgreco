from bd import obtener_conexion


def insertar_categoria(descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO categoria(descripcion) VALUES (%s)",
                       (descripcion))
    conexion.commit()
    conexion.close()


def obtener_categoria():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idcategoria,descripcion FROM categoria")
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
            "SELECT idcategoria,descripcion FROM categoria WHERE idcategoria = %s", (idcategoria,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_categoria(idcategoria,descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE categoria SET  descripcion = %s WHERE idcategoria = %s",
                       (idcategoria,descripcion))
    conexion.commit()
    conexion.close()

  