from bd import obtener_conexion


def insertar_rol_usuario(descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO rol_usuario(descripcion) VALUES (%s)",
                       (descripcion))
    conexion.commit()
    conexion.close()


def obtener_rol_usuario():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idtipo_usuario,descripcion  FROM rol_usuario")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_rol_usuario(idtipo_usuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM rol_usuario WHERE idtipo_usuario = %s", (idtipo_usuario,))
    conexion.commit()
    conexion.close()


def obtener_rol_usuario_por_id(idtipo_usuario):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idtipo_usuario,descripcion FROM rol_usuario WHERE idtipo_usuario = %s", (idtipo_usuario,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_rol_usuario(idtipo_usuario,descripcion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE rol_usuario SET  descripcion = %s WHERE idtipo_usuario = %s",
                       (idtipo_usuario,descripcion))
    conexion.commit()
    conexion.close()





  