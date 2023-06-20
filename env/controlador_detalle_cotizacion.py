from bd import obtener_conexion


def insertar_detalle_cotizacion(cantidad,precio_venta,descuento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO detalle_cotizacion(cantidad,precio_venta,descuento) VALUES (%s, %s,%s)",
                       (cantidad,precio_venta,descuento))
    conexion.commit()
    conexion.close()


def obtener_detalle_cotizacion():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT iddetalle_cotizacion,cantidad,precio_venta,descuento FROM detalle_cotizacion")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_detalle_cotizacion(iddetalle_cotizacion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM detalle_cotizacion WHERE iddetalle_cotizacion = %s", (iddetalle_cotizacion,))
    conexion.commit()
    conexion.close()


def obtener_detalle_cotizacion_por_id(iddetalle_cotizacion):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT iddetalle_cotizacion,cantidad,precio_venta,descuento FROM detalle_cotizacion WHERE iddetalle_cotizacion = %s", (iddetalle_cotizacion,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_detalle_cotizacion(iddetalle_cotizacion,cantidad,precio_venta,descuento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE detalle_cotizacion SET  cantidad= %s, precio_venta= %s,descuento=%s WHERE iddetalle_cotizacion = %s",
                       (iddetalle_cotizacion,cantidad,precio_venta,descuento ))
    conexion.commit()
    conexion.close()