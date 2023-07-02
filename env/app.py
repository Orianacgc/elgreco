from flask import Flask, render_template,request,redirect
import controlador_clientes, controlador_productos,controlador_usuarios,controlador_rol_usuario,controlador_ventas, controlador_cotizaciones,controlador_compras, controlador_categorias
from bd import*

app=Flask(__name__, template_folder='Templates')

@app.route('/')
def main():
    return render_template('listado_productos.html')


@app.route("/principal")
def principal():
    return render_template("principal.html")

@app.route("/agregar_cliente")
def formulario_agregar_cliente():
    return render_template("agregar_cliente.html")


@app.route("/guardar_cliente", methods=["POST"])
def guardar_cliente():
    
    aPaterno = request.form["aPaterno"]
    aMaterno = request.form["aMaterno"]
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    email = request.form["email"]
    calle = request.form["calle"]
    numero_exterior = request.form["numero_exterior"]
    numero_interior = request.form["numero_interior"]
    colonia = request.form["colonia"]
    CP = request.form["CP"]
    RFC = request.form["RFC"]
    regimen = request.form["regimen"]
    controlador_clientes.insertar_cliente(aPaterno,aMaterno,nombre,telefono,email,calle,
                                          numero_exterior,numero_interior,colonia,CP,RFC,regimen)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/clientes")


@app.route("/clientes")
def clientes():
    clientes = controlador_clientes.obtener_cliente()
    return render_template("listado_clientes.html", clientes=clientes)

@app.route("/eliminar_cliente", methods=["POST"])
def eliminar_cliente():
    controlador_clientes.eliminar_cliente(request.form["idcliente"])
    return redirect("/clientes")


@app.route("/formulario_editar_cliente/<int:idcliente>")
def editar_cliente(idcliente):
    # Obtener el cliente por ID
    cliente = controlador_clientes.obtener_cliente_por_id(idcliente)
    return render_template("editar_cliente.html", cliente=cliente)


@app.route("/actualizar_cliente", methods=["POST"])
def actualizar_cliente():
    idcliente = request.form["idcliente"]
    aPaterno = request.form["aPaterno"]
    aMaterno = request.form["aMaterno"]
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    email = request.form["email"]
    calle = request.form["calle"]
    numero_exterior = request.form["numero_exterior"]
    numero_interior = request.form["numero_interior"]
    colonia = request.form["colonia"]
    CP = request.form["CP"]
    RFC = request.form["RFC"]
    regimen = request.form["regimen"]
    controlador_clientes.actualizar_cliente(aPaterno,aMaterno,nombre,telefono,email,calle,
                                          numero_exterior,numero_interior,colonia,CP,RFC,regimen, idcliente)
    return redirect("/clientes")



#Buscar cliente
@app.route('/buscar_cliente', methods=['GET','POST'])
def buscar_cliente():
  
    search = request.form['buscar']

    controlador_clientes.buscar_cliente()
    return render_template('buscar_cliente.html', busqueda = search)
    return redirect("/clientes")
   


#------------Usuarios-------------#

@app.route("/agregar_usuario")
def formulario_agregar_usuario():
    roles = controlador_rol_usuario.obtener_rol_usuario()
    return render_template("agregar_usuario.html", roles=roles)



@app.route("/usuarios")
def usuarios():
    usuarios = controlador_usuarios.obtener_usuario()
    return render_template("listado_usuarios.html", usuarios=usuarios)

@app.route("/eliminar_usuario", methods=["POST"])
def eliminar_usuario():
    controlador_usuarios.eliminar_usuario(request.form["idUsuario"])
    return redirect("/usuarios")


@app.route("/formulario_editar_usuario/<int:idUsuario>")
def editar_usuario(idUsuario):
    # Obtener el usuario por ID
    usuario = controlador_usuarios.obtener_usuario_por_id(idUsuario)
    return render_template("editar_usuario.html", usuario=usuario)


@app.route("/actualizar_usuario", methods=["POST"])
def actualizar_usuario():
    idUsuario = request.form["idUsuario"]
    usuario = request.form["usuario"]
    password = request.form["password"]
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    imagen = request.form["imagen"]
    estado = request.form["estado"]

    controlador_usuarios.actualizar_usuario(usuario,password,nombre,apellido,imagen,estado,idUsuario)
    return redirect("/usuarios")

@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():
    usuario = request.form["usuario"]
    password = request.form["password"]
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    imagen=request.form['imagen']
    estado = request.form["estado"]
    rol = request.form["rol"]
    controlador_usuarios.insertar_usuario(usuario,password,nombre,apellido,imagen,estado,rol)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/usuarios")


#------------Productos-------------#


@app.route("/agregar_producto")
def formulario_agregar_producto():
    categorias = controlador_categorias.obtener_categoria()
    return render_template("agregar_producto.html",categorias=categorias)



@app.route("/productos")
def productos():
    productos = controlador_productos.obtener_producto()
    return render_template("listado_productos.html", productos=productos)

@app.route("/eliminar_producto", methods=["POST"])
def eliminar_producto():
    controlador_productos.eliminar_producto(request.form["idproducto"])
    return redirect("/productos")


@app.route("/formulario_editar_producto/<int:idproducto>")
def editar_producto(idproducto):
    # Obtener el usuario por ID
    producto = controlador_productos.obtener_producto_por_id(idproducto)
    return render_template("editar_producto.html", producto=producto)


@app.route("/actualizar_producto", methods=["POST"])
def actualizar_producto():
    idproducto = request.form["idproducto"]
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    stock = request.form["stock"]
    descripcion = request.form["descripcion"]
    color = request.form["color"]
    medida = request.form["medida"]
    imagen = request.form["imagen"]
    costo_venta = request.form["costo_venta"]
    estado = request.form["estado"]
    

    controlador_productos.actualizar_producto(codigo,nombre,stock,descripcion,color,medida,imagen,costo_venta,estado,idproducto)
    return redirect("/productos")

@app.route("/guardar_producto", methods=["POST"])
def guardar_producto():
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    stock = request.form["stock"]
    descripcion = request.form["descripcion"]
    color = request.form["color"]
    medida = request.form["medida"]
    imagen = request.form["imagen"]
    costo_venta = request.form["costo_venta"]
    estado = request.form["estado"]
    categoria =request.form["categoria"]

    controlador_productos.insertar_producto(codigo,nombre,stock,descripcion,color,medida,imagen,costo_venta,estado,categoria)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/productos")


#------------Ventas-------------#


@app.route("/agregar_venta")
def formulario_agregar_venta():
    productos = controlador_productos.obtener_producto_categoria()
    clientes = controlador_clientes.obtener_cliente()
    return render_template("agregar_venta.html", productos=productos,clientes=clientes)



@app.route("/ventas")
def ventas():
    ventas = controlador_ventas.obtener_venta()
    return render_template("listado_ventas.html", ventas=ventas)

@app.route("/eliminar_venta", methods=["POST"])
def eliminar_venta():
    controlador_ventas.eliminar_venta(request.form["idventa"])
    return redirect("/ventas")


@app.route("/formulario_editar_venta/<int:idventa>")
def editar_venta(idventa):
    # Obtener el usuario por ID
    venta = controlador_ventas.obtener_venta_por_id(idventa)
    return render_template("editar_venta.html", venta=venta)


@app.route("/actualizar_venta", methods=["POST"])
def actualizar_venta():
    idventa = request.form["idventa"]
    fecha_venta = request.form["fecha_venta"]
    fecha_entrega = request.form["fecha_entrega"]
    total_venta = request.form["total_venta"]
    hora = request.form["hora"]
    anticipo = request.form["anticipo"]
    adeudo = request.form["adeudo"]
    subtotal = request.form["subtotal"]

    controlador_ventas.actualizar_venta(fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,subtotal,idventa)
    return redirect("/ventas")

@app.route("/guardar_venta", methods=["POST"])
def guardar_venta():

    fecha_venta = request.form["fecha_venta"]
    fecha_entrega = request.form["fecha_entrega"]
    total_venta = request.form["total_venta"]
    hora = request.form["hora"]
    anticipo = request.form["anticipo"]
    adeudo = request.form["adeudo"]
    subtotal = request.form["subtotal"]

    controlador_ventas.insertar_venta(fecha_venta,fecha_entrega,total_venta,hora,anticipo,adeudo,subtotal)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/ventas")



#------------Cotizaciones-------------#


@app.route("/agregar_cotizacion")
def formulario_agregar_cotizacion():
    return render_template("agregar_cotizacion.html")



@app.route("/cotizaciones")
def cotizaciones():
    cotizaciones = controlador_cotizaciones.obtener_cotizacion()
    return render_template("listado_cotizaciones.html", cotizaciones=cotizaciones)

@app.route("/eliminar_cotizacion", methods=["POST"])
def eliminar_cotizacion():
    controlador_cotizaciones.eliminar_cotizacion(request.form["idcotizacion"])
    return redirect("/cotizaciones")


@app.route("/formulario_editar_cotizacion/<int:idcotizacion>")
def editar_cotizacion(idcotizacion):
    # Obtener el usuario por ID
    cotizacion = controlador_cotizaciones.obtener_cotizacion_por_id(idcotizacion)
    return render_template("editar_cotizacion.html", cotizacion=cotizacion)


@app.route("/actualizar_cotizacion", methods=["POST"])
def actualizar_cotizacion():

    idcotizacion = request.form["idcotizacion"]
    codigo = request.form["codigo"]
    fecha_cotizacion = request.form["fecha_cotizacion"]
    descripcion = request.form["descripcion"]
    total = request.form["total"]
    estado = request.form["estado"]
    

    controlador_cotizaciones.actualizar_cotizacion(codigo,fecha_cotizacion,descripcion,total,estado,idcotizacion)
    return redirect("/cotizaciones")

@app.route("/guardar_cotizacion", methods=["POST"])
def guardar_cotizacion():

    codigo = request.form["codigo"]
    fecha_cotizacion = request.form["fecha_cotizacion"]
    descripcion = request.form["descripcion"]
    total = request.form["total"]
    estado = request.form["estado"]
    

    controlador_cotizaciones.insertar_cotizacion(codigo,fecha_cotizacion,descripcion,total,estado)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/cotizaciones")


#------------Compras-------------#


@app.route("/agregar_compra")
def formulario_agregar_compra():
    return render_template("agregar_compra.html")



@app.route("/compras")
def compras():
    compras = controlador_compras.obtener_compras()
    return render_template("listado_compras.html", compras=compras)

@app.route("/eliminar_compra", methods=["POST"])
def eliminar_compra():
    controlador_compras.eliminar_compra(request.form["idcompras"])
    return redirect("/compras")


@app.route("/formulario_editar_compra/<int:idcompras>")
def editar_compras(idcompras):
    # Obtener el usuario por ID
    compra = controlador_cotizaciones.obtener_cotizacion_por_id(idcompras)
    return render_template("editar_compra.html", compra=compra)


@app.route("/actualizar_compra", methods=["POST"])
def actualizar_compra():

    idcompras = request.form["idcompra"]
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    hora = request.form["hora"]
    fecha_compra = request.form["feha_compra"]
    total = request.form["total"]
    
    

    controlador_compras.actualizar_compras(codigo,nombre,descripcion,hora,fecha_compra,total,idcompras)
    return redirect("/compras")

@app.route("/guardar_compra", methods=["POST"])
def guardar_compra():

    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    hora = request.form["hora"]
    fecha_compra = request.form["feha_compra"]
    total = request.form["total"]
    

    controlador_cotizaciones.insertar_cotizacion(codigo,nombre,descripcion,hora,fecha_compra,total)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/compras")



#------------Proveedores-------------#




if __name__=='__main__':

  app.run(debug=True, port=5000)