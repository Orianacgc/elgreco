from bd import obtener_conexion


def insertar_forma_pago(nombre_forma_pago):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO forma_pago(nombre_forma_pago) VALUES (%s)",
                       (nombre_forma_pago))
    conexion.commit()
    conexion.close()


def obtener_forma_pago():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idforma_pago,nombre_forma_pago  FROM forma_pago")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_forma_pago(idforma_pago):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM forma_pago WHERE idforma_pago = %s", (idforma_pago,))
    conexion.commit()
    conexion.close()


def obtener_forma_pago_por_id(idforma_pago):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idforma_pago,nombre_forma_pago  FROM forma_pago WHERE idforma_pago = %s", (idforma_pago,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_forma_pago(idforma_pago,nombre_forma_pago ):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE forma_pago SET  nombre_forma_pago = %s WHERE idforma_pago = %s",
                       (idforma_pago,nombre_forma_pago ))
    conexion.commit()
    conexion.close()





  