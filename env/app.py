from flask import Flask, render_template,request,redirect
import controlador_clientes, controlador_productos

app=Flask(__name__, template_folder='Templates')

@app.route('/')
def main():
    return render_template('listado_clientes.html')

@app.route("/agregar_cliente")
def formulario_agregar_cliente():
    return render_template("agregar_cliente.html")


@app.route("/guardar_cliente", methods=["POST"])
def guardar_cliente():
    num_cliente = request.form["#"]
    aPaterno = request.form["Apellidos"]
    aMaterno = request.form["Apellidos"]
    nombre = request.form["Nombres"]
    telefono = request.form["Teléfono"]
    email = request.form["Email"]
    calle = request.form["Dirección"]
    numero_exterior = request.form["Dirección"]
    numero_interior = request.form["Dirección"]
    colonia = request.form["Dirección"]
    CP = request.form["CP"]
    RFC = request.form["RFC"]
    regimen = request.form["Regimen"]
    controlador_clientes.insertar_cliente(num_cliente,aPaterno,aMaterno,nombre,telefono,email,calle,
                                          numero_exterior,numero_interior,colonia,CP,RFC,regimen)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/listado_clientes")


@app.route("/clientes")
def clientes():
    clientes = controlador_clientes.obtener_cliente()
    return render_template("listado_clientes.html", clientes=clientes)

@app.route("/productos")
def productos():
    productos = controlador_productos.obtener_producto()
    return render_template("listado-productos.html", productos=productos)


if __name__=='__main__':

  app.run(debug=True, port=5000) 