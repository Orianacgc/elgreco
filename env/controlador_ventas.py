from bd import obtener_conexion

#recibir selperfil, selvidrio y todos los demas, ancho y largo, total, etc
""" def insertar_venta(fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,subtotal,txtlargo,txtancho,selperfil,selvidrio,selml,selsoporte,txtprecioventa,txtanticipo,txtadeudo,txtcant,idcliente,idproducto,idventa, cantidad, precio_venta):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO venta(fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,subtotal) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)",
                       (fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,subtotal))
        cursor.execute('SELECT LAST_INSERT_ID()') # Add this
        cursor.lastrowid = cursor.fetchone()[0]
        print('last id:', cursor.lastrowid)
        cursor.execute("INSERT INTO detalle_venta(idproducto,idventa, cantidad, precio_venta, ancho, largo) VALUES (%s, %s, %s,%s, %s, %s)", 
                       (selperfil,idventa, txtcant, txtprecioventa, txtancho, txtlargo))
        cursor.execute("INSERT INTO detalle_venta(idproducto,idventa, cantidad, precio_venta, ancho, largo)  VALUES (%s, %s, %s,%s, %s, %s)", 
                       (selvidrio,idventa, txtcant, txtprecioventa, txtancho, txtlargo))
        cursor.execute("INSERT INTO detalle_venta(idproducto,idventa, cantidad, precio_venta, ancho, largo)  VALUES (%s, %s, %s,%s, %s, %s)", 
                       (selml,idventa, txtcant, txtprecioventa, txtancho, txtlargo))
        cursor.execute("INSERT INTO detalle_venta(idproducto,idventa, cantidad, precio_venta, ancho, largo) VALUES (%s, %s, %s,%s,%s,%s)", 
                       (selsoporte,idventa, txtcant, txtprecioventa, txtancho, txtlargo)) 
        
       
        #repetir 4 veces idproducto es selperfil, idventa es cursor.lastrowid
        #en la segunda vez otro insert igual, pero 
        #   idproducto seria selvidrio y el idventa es curso.lartrowid
        #la tercer igual pero selmarialuisa
        #cuarto selsoporte


    conexion.commit()
    conexion.close() """



def insertar_venta(fecha_venta,txtfechaentrega,total_venta,hora,txtanticipo,txtadeudo,IVA,subtotal,txtancho,txtlargo,selperfil,selvidrio,selml,selsoporte,txtprecioventa,txtcant,idcliente):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO venta(fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,IVA,subtotal) VALUES (%s, %s, %s,%s, %s, %s,%s, %s)",
                       (fecha_venta,txtfechaentrega,total_venta,hora,txtanticipo,txtadeudo,IVA,subtotal))
        cursor.execute('SELECT LAST_INSERT_ID()') # Add this
        cursor.lastrowid = cursor.fetchone()[0]
        print('last id:', cursor.lastrowid)

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