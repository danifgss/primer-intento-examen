from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime

class Publicacion:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.fecha = data['fecha']
        self.lugar = data['lugar']
        self.descripcion = data['descripcion']
        self.usuario_id = data['usuario_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        # Nombre del usuario que creó la publicación
        self.usuario_nombre = data.get('usuario_nombre', '')

    # ----- GUARDAR PUBLICACION -----
    @classmethod
    def save(cls,data):
        query = """INSERT INTO publicaciones (nombre, fecha, lugar, descripcion, usuario_id)
                VALUES (%(nombre)s,%(fecha)s,%(lugar)s, %(descripcion)s,%(usuario_id)s);"""

        return connectToMySQL('esquema_publicaciones').query_db(query,data)

    # ---- MOSTRAR TODAS LAS PUBLICACIONES ----
    @classmethod
    def get_all(cls):
        query = """SELECT publicaciones.*, 
                   CONCAT(usuarios.nombre,' ',usuarios.apellido) AS usuario_nombre
                   FROM publicaciones 
                   JOIN usuarios ON publicaciones.usuario_id = usuarios.id
                   ORDER BY publicaciones.fecha ASC;
                """
        results = connectToMySQL('esquema_publicaciones').query_db(query)

        publicaciones = []

        if results:
            for r in results:
                publicaciones.append(cls(r))
        return publicaciones

    # ---- BUSCAR PUBLICACION POR ID ----
    @classmethod
    def get_by_id(cls, data):
        query = """SELECT publicaciones.*, CONCAT(u.nombre, ' ', u.apellido) AS usuario_nombre
                   FROM publicaciones
                   JOIN usuarios AS u ON publicaciones.usuario_id = u.id
                   WHERE publicaciones.id = %(id)s;
                """
        results = connectToMySQL('esquema_publicaciones').query_db(query, data)
        if not results:
            return None
        
        publicacion = cls(results[0])

        return publicacion

    # ---- BUSCAR PUBLICACION POR NOMBRE ----
    @classmethod
    def get_by_nombre(cls, data):
        query = """SELECT * FROM publicaciones WHERE nombre = %(nombre)s;
                """

        result = connectToMySQL('esquema_publicaciones').query_db(query, data)
        if not result:
            return None

        return cls(result[0])

    # ---- ACTUALIZAR PUBLICACION ----
    @classmethod
    def update(cls, data):
        query = """UPDATE publicaciones 
                   SET nombre = %(nombre)s, 
                   fecha = %(fecha)s,
                   lugar = %(lugar)s,
                   descripcion = %(descripcion)s, 
                   updated_at = NOW()
                   WHERE id = %(id)s; 
                """
        return connectToMySQL('esquema_publicaciones').query_db(query, data)


    # ---- BORRAR PUBLICACION ----
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM publicaciones WHERE id = %(id)s;
                """
        return connectToMySQL('esquema_publicaciones').query_db(query, data)

    @staticmethod
    def validar_publicacion(formulario):
        es_valido = True

        nombre = formulario.get('nombre', '').strip()
        fecha = formulario.get('fecha', '')
        lugar = formulario.get('lugar', '').strip()
        descripcion = formulario.get('descripcion', '').strip()

        if not nombre:
            flash("El campo nombre es obligatorio", "publicacion")
            es_valido = False

        #validar que nombre sea unico
        if nombre and Publicacion.get_by_nombre({'nombre': nombre}):
            flash("Ya existe una publicación con ese nombre","publicacion")
            es_valido = False

        if not fecha:
            flash("Los campos de fecha inicio y fecha fin son obligatorios", "publicacion")
            es_valido = False

        if fecha:
             try:
                datetime.strptime(fecha, '%Y-%m-%d').date()

             except ValueError:
                flash("Formato de fecha invalido", "publicacion")
                es_valido = False
        
        if not lugar:
            flash("El lugar es obligatorio", "publicacion")
            es_valido = False

        if not descripcion:
           flash("La descripción es obligatoria", "publicacion")
           es_valido = False

        return es_valido

   