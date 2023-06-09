from bd import obtener_conexion


def insertar_usuario(num_cliente,aPaterno,aMaterno,nombre,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO elgreco(num_cliente,aPaterno,aMaterno,nombre,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen) VALUES (%s, %s, %s)",
                       (num_cliente,aPaterno,aMaterno,nombre,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen))
    conexion.commit()
    conexion.close()


def obtener_usuario():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idcliente,num_cliente,aPaterno,aMaterno,nombres,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen FROM cliente")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_usuario(idcliente):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM elgreco WHERE idcliente = %s", (idcliente,))
    conexion.commit()
    conexion.close()


def obtener_usuario_por_id(idcliente):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idcliente,num_cliente,aPaterno,aMaterno,nombres,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen FROM elgreco WHERE idcliente = %s", (idcliente,))
        juego = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_usuario(idcliente,num_cliente,aPaterno,aMaterno,nombres,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE elgreco SET  num_cliente = %s, aPaterno = %s, aMaterno = %s, nombres = %s, telefono = %s, email = %s, calle = %s, numero_exterior = %s, numero_interior = %s, colonia = %s, CP= %s, RFC = %s, regimen = %s WHERE idcliente = %s",
                       (idcliente,num_cliente,aPaterno,aMaterno,nombres,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen))
    conexion.commit()
    conexion.close()