from flask import Flask, render_template,request,redirect
import controlador_clientes, controlador_productos,controlador_usuarios
from bd import*

app=Flask(__name__, template_folder='Templates')

@app.route('/')
def main():
    return render_template('listado_clientes.html')

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
    return render_template("agregar_usuario.html")


@app.route("/guardar_usuario", methods=["POST"])
def guardar_usuario():

    usuario = request.form["usuario"]
    password = request.form["password"]
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    estado = request.form["estado"]
    
    controlador_clientes.insertar_cliente(usuario,password,nombre,apellido,estado)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/usuarios")


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
    estado = request.form["estado"]

    controlador_usuarios.actualizar_usuario(usuario,password,nombre,apellido,estado,idUsuario)
    return redirect("/usuarios")




if __name__=='__main__':

  app.run(debug=True, port=5000)