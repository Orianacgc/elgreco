from bd import obtener_conexion


def insertar_detalle_venta(cantidad,precio_venta,descuento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO detalle_venta(cantidad,precio_venta,descuento) VALUES (%s, %s,%s)",
                       (cantidad,precio_venta,descuento))
    conexion.commit()
    conexion.close()


def obtener_detalle_venta():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT iddetalle_venta,cantidad,precio_venta,descuento FROM detalle_venta")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_detalle_venta(iddetalle_venta):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM detalle_venta WHERE iddetalle_venta = %s", (iddetalle_venta,))
    conexion.commit()
    conexion.close()


def obtener_detalle_venta_por_id(iddetalle_venta):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT iddetalle_venta,cantidad,precio_venta,descuento FROM detalle_venta WHERE iddetalle_venta = %s", (iddetalle_venta,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_detalle_venta(iddetalle_venta,cantidad,precio_venta,descuento):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE detalle_venta SET  cantidad= %s, precio_venta= %s,descuento=%s WHERE iddetalle_venta = %s",
                       (iddetalle_venta,cantidad,precio_venta,descuento ))
    conexion.commit()
    conexion.close()