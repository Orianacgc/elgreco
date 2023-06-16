from bd import obtener_conexion


def insertar_proveedor(nombre,personaContacto,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,estado,municipio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO proveedor(nombre,personaContacto,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,estado,municipio) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)",
                       (nombre,personaContacto,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,estado,municipio))
    conexion.commit()
    conexion.close()


def obtener_proveedor():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idproveedor,nombre,personaContacto,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,estado,municipio FROM proveedor")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_proveedor(idproveedor):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM proveedor WHERE idproveedor = %s", (idproveedor,))
    conexion.commit()
    conexion.close()


def obtener_proveedor_por_id(idproveedor):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idproveedor,nombre,personaContacto,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,estado,municipio FROM proveedor WHERE idproveedor = %s", (idproveedor,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_proveedor(idproveedor,nombre,personaContacto,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,estado,municipio):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE proveedor SET  nombre = %s, personaContacto = %s, telefono = %s, email = %s, calle = %s, numero_exterior = %s, numero_interior = %s, colonia = %s, CP= %s, estado = %s, municipio = %s WHERE idproveedor = %s",
                       (idproveedor,nombre,personaContacto,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,estado,municipio))
    conexion.commit()
    conexion.close()