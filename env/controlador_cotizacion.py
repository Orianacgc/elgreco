from bd import obtener_conexion


def insertar_compras(codigo,nombre,descripcion,hora,fecha_compra,total):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO compras(codigo,nombre,descripcion,hora,fecha_compra,total) VALUES (%s, %s, %s,%s, %s, %s)",
                       (codigo,nombre,descripcion,hora,fecha_compra,total))
    conexion.commit()
    conexion.close()


def obtener_compras():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idcompras,codigo,nombre,descripcion,hora,fecha_compra,total FROM compras")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_compras(idcompras):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM compras WHERE idcompras = %s", (idcompras,))
    conexion.commit()
    conexion.close()


def obtener_compras_por_id(idcompras):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idcompras,codigo,nombre,descripcion,hora,fecha_compra,total FROM compras WHERE idcompras = %s", (idcompras,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_compras(idcompras,codigo,nombre,descripcion,hora,fecha_compra,total):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE compras SET  codigo= %s, nombre= %s, descripcion = %s, hora = %s, fecha_compra = %s, total = %s WHERE idcompras = %s",
                       (idcompras,codigo,nombre,descripcion,hora,fecha_compra,total ))
    conexion.commit()
    conexion.close()