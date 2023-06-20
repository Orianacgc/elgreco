from bd import obtener_conexion


def insertar_cotizacion(codigo,fecha_cotizacion,descripcion,total,estado):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO cotizacion(codigo,fecha_cotizacion,descripcion,total,estado) VALUES (%s, %s, %s,%s, %s)",
                       (codigo,fecha_cotizacion,descripcion,total,estado))
    conexion.commit()
    conexion.close()


def obtener_cotizacion():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idcotizacion,codigo,fecha_cotizacion,descripcion,total,estado FROM cotizacion")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_cotizacion(idcotizacion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM cotizacion WHERE idcotizacion = %s", (idcotizacion,))
    conexion.commit()
    conexion.close()


def obtener_cotizacion_por_id(idcotizacion):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idcotizacion,codigo,fecha_cotizacion,descripcion,total,estado  FROM cotizacion WHERE idcotizacion = %s", (idcotizacion,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_cotizacion(idcotizacion,codigo,fecha_cotizacion,descripcion,total,estado ):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE cotizacion SET  codigo= %s, fecha_cotizacion= %s, descripcion = %s, total = %s, estado = %s WHERE idcotizacion = %s",
                       (idcotizacion,codigo,fecha_cotizacion,descripcion,total,estado))
    conexion.commit()
    conexion.close()