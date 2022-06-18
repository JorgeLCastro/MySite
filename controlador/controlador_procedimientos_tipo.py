from bd import obtener_conexion

def insertar_procedimiento_tipo(name,description):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO procedure_types(name,description,created_at) VALUES (%s, %s, NOW())",
                       (name,description))
    conexion.commit()
    conexion.close()

# def obtener_juegos():
#     conexion = obtener_conexion()
#     juegos = []
#     with conexion.cursor() as cursor:
#         cursor.execute("SELECT id, nombre, descripcion, precio FROM juegos")
#         juegos = cursor.fetchall()
#     conexion.close()
#     return juegos

def obtener_procedimientos_tipo():
    conexion = obtener_conexion()
    procedimientos_tipo = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id,name,description,created_at,updated_at FROM procedure_types")
        procedimientos_tipo = cursor.fetchall()
    conexion.close()
    return procedimientos_tipo
    

# def eliminar_juego(id):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("DELETE FROM juegos WHERE id = %s", (id,))
#     conexion.commit()
#     conexion.close()

def eliminar_procedimiento_tipo(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM procedure_types WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()   

# def obtener_juego_por_id(id):
#     conexion = obtener_conexion()
#     juego = None
#     with conexion.cursor() as cursor:
#         cursor.execute(
#             "SELECT id, nombre, descripcion, precio FROM juegos WHERE id = %s", (id,))
#         juego = cursor.fetchone()
#     conexion.close()
#     return juego

def obtener_procedimiento_tipo_por_id(id):
     conexion = obtener_conexion()
     procedimiento_tipo = None
     with conexion.cursor() as cursor:
         cursor.execute(
             "SELECT id,name,description,created_at,updated_at FROM procedure_types WHERE id = %s", (id,))
         procedimiento_tipo = cursor.fetchone()
     conexion.close()
     return procedimiento_tipo 

# def actualizar_juego(nombre, descripcion, precio, id):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("UPDATE juegos SET nombre = %s, descripcion = %s, precio = %s WHERE id = %s",
#                        (nombre, descripcion, precio, id))
#     conexion.commit()
#     conexion.close()

def actualizar_procedimiento_tipo(name,description,id):
     conexion = obtener_conexion()
     with conexion.cursor() as cursor:
         cursor.execute("UPDATE procedure_types SET name = %s,description = %s,updated_at=NOW() WHERE id = %s",
                        (name,description,id))
     conexion.commit()
     conexion.close()
