from email import message
import json
from pyexpat.errors import messages
from flask import Flask, render_template, request, redirect, flash, jsonify
import flask
# import controlador.controlador_juegos as controlador_juegos
# import clase.clase_juego as clase_juego
import controlador.controlador_procedimientos as controlador_procedimientos
import clase.clase_procedimiento as clase_procedimiento
import controlador.controlador_procedimientos_tipo as controlador_procedimientos_tipo
import clase.clase_procedimiento_tipo as clase_procedimiento_tipo

app = Flask(__name__)

# APIs - Inicio

    # ..................................PROCEDIMIENTO TIPO....................................

@app.route("/api_obtenerprocedimientos")
def api_obtenerprocedimientos():
    try:
        procedimientos = controlador_procedimientos.obtener_procedimientos()
        listaserializable = []
        for procedimiento in procedimientos:
            miobj = clase_procedimiento.Procedimiento(procedimiento[0], procedimiento[1], procedimiento[2], procedimiento[3],procedimiento[4],procedimiento[5],procedimiento[6],procedimiento[7],procedimiento[8])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas Grupo01"})

@app.route("/api_obtenerprocedimientotipos")
def api_obtenerprocedimientotipos():
    try:
        procedimientos_tipo = controlador_procedimientos_tipo.obtener_procedimientos_tipo()
        listaserializable = []
        for procedimiento_tipo in procedimientos_tipo:
            miobj = clase_procedimiento_tipo.Procedimiento_tipo(procedimiento_tipo[0],procedimiento_tipo[1], procedimiento_tipo[2], procedimiento_tipo[3],procedimiento_tipo[4])
            listaserializable.append(miobj.midic.copy())
        return jsonify(listaserializable)
    except:
        return jsonify({"Mensaje":"Error interno. Llame al Administrador de sistemas Grupo01"})
# ............

@app.route("/api_obtenerprocedimiento/{id}")#api obtener procedimientos por id
def api_obtenerprocedimiento(id):
    try:
        procedimiento = controlador_procedimientos.obtener_procedimiento_por_id(id)
        if(procedimiento is not None):
           return jsonify(procedimiento)
        return jsonify({"Mensaje": "Procedimiento no encontrado"})
    except:
        return jsonify({"Mensaje":"Error al obtener" })

@app.route("/api_obtenerprocedimientotipo/{id}")#api obtener procedimientos_tipo por id
def api_obtenerprocedimientotipo(id):
    try:
        procedimiento_tipo = controlador_procedimientos_tipo.obtener_procedimiento_tipo_por_id(id)
        if(procedimiento_tipo is not None):
           return jsonify(procedimiento_tipo)
        return jsonify({"Mensaje": "Procedimiento tipo no encontrado"})
    except:
        return jsonify({"Mensaje":"Error al obtener" })
# ............

@app.route("/api_guardarprocedimientotipo", methods=["POST"])
def api_guardarprocedimientotipo():
    name = request.json["name"]
    description = request.json["description"]
    controlador_procedimientos_tipo.insertar_procedimiento_tipo(name,description)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Tipo de Procedimiento registrado correctamente"})

@app.route("/api_guardarprocedimiento", methods=["POST"])
def api_guardarprocedimiento():
    date = request.json["date"]
    description = request.json["description"]
    procedure_type_id = request.json["procedure_type_id"]
    tree_id = request.json["tree_id"]
    responsible_id = request.json["responsible_id"]
    user_id = request.json["user_id"]
    controlador_procedimientos.insertar_procedimiento(date, description, procedure_type_id, tree_id,responsible_id, user_id)
    # De cualquier modo, y si todo fue bien, redireccionar
    return jsonify({"Mensaje":"Procedimiento registrado correctamente"})
# ............

@app.route("/api_actualizarprocedimientotipo", methods=["POST"])
def api_actualizarprocedimientotipo():
    id = request.json["id"]
    name = request.json["name"]
    description = request.json["description"]
    controlador_procedimientos_tipo.actualizar_procedimiento_tipo(name,description,id)
    return jsonify({"Mensaje":"Tipo de Procedimiento actualizado correctamente"})

@app.route("/api_actualizarprocedimiento", methods=["POST"])
def api_actualizarprocedimiento():
    id = request.json["id"]
    date = request.json["date"]
    description = request.json["description"]
    procedure_type_id = request.json["procedure_type_id"]
    tree_id = request.json["tree_id"]
    responsible_id = request.json["responsible_id"]
    user_id = request.json["user_id"]
    controlador_procedimientos_tipo.actualizar_procedimiento_tipo(date, description, procedure_type_id, tree_id,responsible_id, user_id,id)
    return jsonify({"Mensaje":"Procedimiento actualizado correctamente"})

# ............

@app.route("/api_eliminarprocedimientotipo", methods=["POST"])
def api_eliminarprocedimientotipo():
    controlador_procedimientos_tipo.eliminar_procedimiento_tipo(request.json["id"])
    return jsonify({"Mensaje":"Tipo de Procedimiento eliminado correctamente"})

@app.route("/api_eliminarprocedimiento", methods=["POST"])
def api_eliminarprocedimiento():
    controlador_procedimientos.eliminar_procedimiento(request.json["id"])
    return jsonify({"Mensaje":"Procedimiento eliminado correctamente"})
# ............

# APIs - Fin

@app.route("/agregar_procedimiento_tipo")
def formulario_agregar_procedimiento_tipo():
    return render_template("agregar_procedimiento_tipo.html")

@app.route("/agregar_procedimiento")
def formulario_agregar_procedimiento():
    procedimientos_tipo = controlador_procedimientos_tipo.obtener_procedimientos_tipo()
    return render_template("agregar_procedimiento.html", procedimientos_tipo=procedimientos_tipo)
# ............

@app.route("/guardar_procedimiento_tipo", methods=["POST"])
def guardar_procedimiento_tipo():
    name = request.form["name"]
    description = request.form["description"]
    controlador_procedimientos_tipo.insertar_procedimiento_tipo(name, description)
    # De cualquier modo, y si todo fue bien, redireccionar
    flash('Tipo de procedimiento guardado correctamente')
    return redirect("/procedimientos_tipo")

@app.route("/guardar_procedimiento", methods=["POST"])
def guardar_procedimiento():
    date = request.form["date"]
    description = request.form["description"]
    procedure_type_id = request.form["procedure_type_id"]
    tree_id = request.form["tree_id"]
    responsible_id = request.form["responsible_id"]
    user_id = request.form["user_id"]
    controlador_procedimientos.insertar_procedimiento(date, description,procedure_type_id,tree_id,responsible_id,user_id)
    # De cualquier modo, y si todo fue bien, redireccionar
    flash("Procedimiento guardado correctamente")
    return redirect("/procedimientos")
# ............

@app.route("/")
@app.route("/procedimientos_tipo")
def procedimientos_tipo():
    procedimientos_tipo = controlador_procedimientos_tipo.obtener_procedimientos_tipo()
    return render_template("procedimientos_tipo.html", procedimientos_tipo=procedimientos_tipo)

@app.route("/")
@app.route("/procedimientos")
def procedimientos():
    procedimientos = controlador_procedimientos.obtener_procedimientos()
    return render_template("procedimientos.html", procedimientos=procedimientos)
# ............

@app.route("/eliminar_procedimiento_tipo", methods=["POST"])
def eliminar_procedimiento_tipo():
    controlador_procedimientos_tipo.eliminar_procedimiento_tipo(request.form["id"])
    return redirect("/procedimientos_tipo")

@app.route("/eliminar_procedimiento", methods=["POST"])
def eliminar_procedimiento():
    controlador_procedimientos.eliminar_procedimiento(request.form["id"])
    return redirect("/procedimientos")

# ............

@app.route("/formulario_editar_procedimiento_tipo/<int:id>")
def editar_procedimiento_tipo(id):
    # Obtener el procedimiento_tipo por ID
    procedimiento_tipo = controlador_procedimientos_tipo.obtener_procedimiento_tipo_por_id(id)
    return render_template("editar_procedimiento_tipo.html", procedimiento_tipo=procedimiento_tipo)

@app.route("/formulario_editar_procedimiento/<int:id>")
def editar_procedimiento(id):
    # Obtener el procedimiento por ID
    procedimiento = controlador_procedimientos.obtener_procedimiento_por_id(id)
    procedimientos_tipo = controlador_procedimientos_tipo.obtener_procedimientos_tipo()
   
    return render_template("editar_procedimiento.html", procedimiento=procedimiento,procedimientos_tipo=procedimientos_tipo)
# ............

@app.route("/actualizar_procedimiento_tipo", methods=["POST"])
def actualizar_procedimiento_tipo():
    id = request.form["id"]
    name= request.form["name"]
    description = request.form["description"]
    controlador_procedimientos_tipo.actualizar_procedimiento_tipo(name,description,id)
    flash("Tipo de procedimiento actualizado correctamente")
    return redirect("/procedimientos_tipo")

@app.route("/actualizar_procedimiento", methods=["POST"])
def actualizar_procedimiento():
    id = request.form["id"]
    date= request.form["date"]
    description = request.form["description"]
    procedure_type_id = request.form["procedure_type_id"]
    tree_id = request.form["tree_id"]
    responsible_id = request.form["responsible_id"]
    user_id = request.form["user_id"]
    controlador_procedimientos.actualizar_procedimiento(date,description,procedure_type_id,tree_id,responsible_id,user_id,id)
    flash("Procedimiento actualizado correctamente")
    return redirect("/procedimientos")
# ............

# Iniciar el servidor
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0', port=8000, debug=True)
    


