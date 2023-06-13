from bd import obtener_conexion


def insertar_venta(fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,valorUnitario,descripcion,subtotal):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO elgreco(fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,valorUnitario,descripcion,subtotal) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)",
                       (fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,valorUnitario,descripcion,subtotal))
    conexion.commit()
    conexion.close()


def obtener_venta():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idventa,fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,valorUnitario,descripcion,subtotal FROM venta")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_venta(idventa):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM elgreco WHERE idventa = %s", (idventa,))
    conexion.commit()
    conexion.close()


def obtener_venta_por_id(idventa):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idventa,fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,valorUnitario,descripcion,subtotal FROM elgreco WHERE idventa = %s", (idventa,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_venta(idcliente,num_cliente,aPaterno,aMaterno,nombres,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE elgreco SET  num_cliente = %s, aPaterno = %s, aMaterno = %s, nombres = %s, telefono = %s, email = %s, calle = %s, numero_exterior = %s, numero_interior = %s, colonia = %s, CP= %s, RFC = %s, regimen = %s WHERE idcliente = %s",
                       (idcliente,num_cliente,aPaterno,aMaterno,nombres,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen))
    conexion.commit()
    conexion.close()