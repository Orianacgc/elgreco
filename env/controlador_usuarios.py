from bd import obtener_conexion


def insertar_usuario(usuario,password,nombre,apellido,imagen,estado,roluser):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuario(usuario,password,nombre,apellido,imagen,estado,idtipo_usuario) VALUES (%s, %s, %s,%s,%s,%s,%s)",
                       (usuario,password,nombre,apellido,imagen,estado,roluser))
    conexion.commit()
    conexion.close()


def obtener_usuario():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idUsuario,usuario,password,nombre,apellido,imagen,estado FROM usuario")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_usuario(idUsuario):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuario WHERE idUsuario= %s", (idUsuario,))
    conexion.commit()
    conexion.close()


def obtener_usuario_por_id(idUsuario):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idUsuario,usuario,password,nombre,apellido,imagen,estado FROM usuario WHERE idUsuario = %s", (idUsuario,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_usuario(idUsuario,usuario,password,nombre,apellido,imagen,estado):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuario SET  usuario = %s, password = %s, nombre = %s, apellido= %s,imagen= %s, estado = %s WHERE idUsuario = %s",
                       (idUsuario,usuario,password,nombre,apellido,imagen,estado))
    conexion.commit()
    conexion.close()