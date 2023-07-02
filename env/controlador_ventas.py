from bd import obtener_conexion


def insertar_venta(fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,subtotal):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO venta(fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,subtotal) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)",
                       (fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,subtotal))
    conexion.commit()
    conexion.close()


def obtener_venta():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idventa,fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,subtotal FROM venta")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_venta(idventa):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM venta WHERE idventa = %s", (idventa,))
    conexion.commit()
    conexion.close()


def obtener_venta_por_id(idventa):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idventa,fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,subtotal FROM elgreco WHERE idventa = %s", (idventa,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_venta(idventa,fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,subtotal):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE venta SET  idventa = %s, fecha_venta = %s, fecha_entrega = %s, total_venta = %s, hora = %s, anticipo = %s, adeudo = %s, IVA = %s, subtotal = %s WHERE idventa = %s",
                       (idventa,fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,subtotal))
    conexion.commit()
    conexion.close()