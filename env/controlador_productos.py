from bd import obtener_conexion


def insertar_producto(idproducto,codigo,nombre,stock,descripcion,medida,imagen,costo_venta,estado):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO elgreco(idproducto,codigo,nombre,stock,descripcion,medida,imagen,costo_venta,estado) VALUES (%s, %s, %s)",
                       (idproducto,codigo,nombre,stock,descripcion,medida,imagen,costo_venta,estado))
    conexion.commit()
    conexion.close()


def obtener_producto():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idproducto,codigo,nombre,stock,descripcion,medida,imagen,costo_venta,estado FROM producto")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_producto(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM elgreco WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_producto_por_id(id):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, nombre, descripcion, precio FROM elgreco WHERE id = %s", (id,))
        juego = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_producto(nombre, descripcion, precio, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE elgreco SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",
                       (nombre, descripcion, precio, id))
    conexion.commit()
    conexion.close()