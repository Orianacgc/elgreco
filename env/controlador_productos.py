from bd import obtener_conexion


def insertar_producto(codigo,nombre,stock,descripcion,color,medida,imagen,costo_venta,estado,categoria):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO producto(codigo,nombre,stock,descripcion,color,medida,imagen,costo_venta,estado,idcategoria) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s)",
                       (codigo,nombre,stock,descripcion,color,medida,imagen,costo_venta,estado,categoria))
    conexion.commit()
    conexion.close()


def obtener_producto():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idproducto,codigo,nombre,stock,descripcion,color,medida,imagen,costo_venta,estado FROM producto")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_producto(idproducto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM producto WHERE idproducto = %s", (idproducto,))
    conexion.commit()
    conexion.close()


def obtener_producto_por_id(idproducto):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idproducto,codigo,nombre,stock,descripcion,color,medida,imagen,costo_venta,estado FROM producto WHERE idproducto = %s", (idproducto,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_producto(codigo,nombre,stock,descripcion,color,medida,imagen,costo_venta,estado,idproducto):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE producto SET codigo = %s, nombre = %s, stock = %s, descripcion %s, color %s, medida = %s, imagen = %s , costo_venta = %s ,estado = %s  WHERE idproducto = %s",
                       (codigo,nombre,stock,descripcion,color,medida,imagen,costo_venta,estado,idproducto))
    conexion.commit()
    conexion.close()