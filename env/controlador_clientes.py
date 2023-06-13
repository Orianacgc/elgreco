from bd import obtener_conexion


def insertar_cliente(aPaterno,aMaterno,nombres,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO cliente(aPaterno,aMaterno,nombres,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s)",
                       (aPaterno,aMaterno,nombres,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen))
    conexion.commit()
    conexion.close()


def obtener_cliente():
    conexion = obtener_conexion()
    elgreco = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idcliente,aPaterno,aMaterno,nombres,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen FROM cliente")
        elgreco = cursor.fetchall()
    conexion.close()
    return elgreco

def eliminar_cliente(idcliente):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM cliente WHERE idcliente = %s", (idcliente,))
    conexion.commit()
    conexion.close()


def obtener_cliente_por_id(idcliente):
    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT idcliente,aPaterno,aMaterno,nombres,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen FROM cliente WHERE idcliente = %s", (idcliente,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco


def actualizar_cliente(idcliente,aPaterno,aMaterno,nombres,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE cliente SET  aPaterno = %s, aMaterno = %s, nombres = %s, telefono = %s, email = %s, calle = %s, numero_exterior = %s, numero_interior = %s, colonia = %s, CP= %s, RFC = %s, regimen = %s WHERE idcliente = %s",
                       (idcliente,aPaterno,aMaterno,nombres,telefono,email,calle,numero_exterior,numero_interior,colonia,CP,RFC,regimen))
    conexion.commit()
    conexion.close()



#Buscar cliente
def buscar_cliente(idcliente,aPaterno,aMaterno,nombres):

    conexion = obtener_conexion()
    elgreco = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM cliente WHERE nombres='%s' ORDER BY idcliente  DESC" % (search,))
        elgreco = cursor.fetchone()
    conexion.close()
    return elgreco

  