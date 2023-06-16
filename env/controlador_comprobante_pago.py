from bd import obtener_conexion


def insertar_comprobante_pago(precio_venta,cantidad):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO comprobante_pago(precio_venta,cantidad) VALUES (%s,%s)",
                       (precio_venta,cantidad))
    conexion.commit()
    conexion.close()


def obtener_comprobante_pago():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idcomprobante_pago,precio_venta,cantidad  FROM comprobante_pago")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_comprobante_pago(idcomprobante_pago):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM comprobante_pago WHERE idcomprobante_pago = %s", (idcomprobante_pago,))
    conexion.commit()
    conexion.close()


def obtener_comprobante_pago(idcomprobante_pago):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idcomprobante_pago,precio_venta,cantidad FROM comprobante_pago WHERE idcomprobante_pago = %s", (idcomprobante_pago,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_comprobante_pago(idcomprobante_pago,precio_venta,cantidad):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE comprobante_pago SET  precio_venta = %s, cantidad = %s WHERE idcomprobante_pago = %s",
                       (idcomprobante_pago,precio_venta,cantidad))
    conexion.commit()
    conexion.close()





  