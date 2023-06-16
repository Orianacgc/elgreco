from bd import obtener_conexion


def insertar_detalle_compras(cantidad,precio_compra):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO detalle_compras(cantidad,precio_compra) VALUES (%s, %s)",
                       (cantidad,precio_compra))
    conexion.commit()
    conexion.close()


def obtener_detalle_compras():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT iddetalle_compras,cantidad,precio_compra FROM detalle_compras")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_detalle_compras(iddetalle_compras):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM detalle_compras WHERE iddetalle_compras = %s", (iddetalle_compras,))
    conexion.commit()
    conexion.close()


def obtener_detalle_compras_por_id(iddetalle_compras):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT iddetalle_compras,cantidad,precio_compra FROM detalle_compras WHERE iddetalle_compras = %s", (iddetalle_compras,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_detalle_compras(iddetalle_compras,cantidad,precio_compra):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE detalle_compras SET  cantidad= %s, precio_compra= %s WHERE iddetalle_compras = %s",
                       (iddetalle_compras,cantidad,precio_compra ))
    conexion.commit()
    conexion.close()