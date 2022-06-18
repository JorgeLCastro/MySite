from bd import obtener_conexion

def insertar_procedimiento(date,description,procedure_type_id,tree_id,responsible_id,user_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO procedures(date,description,procedure_type_id,tree_id,responsible_id,user_id,created_at) VALUES (%s, %s, %s, %s, %s, %s,NOW())",
                       (date,description,procedure_type_id,tree_id,responsible_id,user_id))
    conexion.commit()
    conexion.close()

def obtener_procedimientos():
    conexion = obtener_conexion()
    procedimientos = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id,date,description,procedure_type_id,tree_id,responsible_id,user_id,created_at,updated_at FROM procedures")
        procedimientos = cursor.fetchall()
    conexion.close()
    return procedimientos
    
def eliminar_procedimiento(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM procedures WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()   

def obtener_procedimiento_por_id(id):
     conexion = obtener_conexion()
     procedimiento = None
     with conexion.cursor() as cursor:
         cursor.execute(
             "SELECT id,date,description,procedure_type_id,tree_id,responsible_id,user_id,created_at,updated_at FROM procedures WHERE id = %s", (id,))
         procedimiento = cursor.fetchone()
     conexion.close()
     return procedimiento 

def actualizar_procedimiento(date,description,procedure_type_id,tree_id,responsible_id,user_id,id):
     conexion = obtener_conexion()
     with conexion.cursor() as cursor:
         cursor.execute("UPDATE procedures SET date = %s,description = %s,procedure_type_id = %s,tree_id = %s,updated_at = NOW(),responsible_id = %s,user_id = %s WHERE id = %s",
                        (date,description,procedure_type_id,tree_id,responsible_id,user_id,id))
     conexion.commit()
     conexion.close()
