from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.contrasena = data['contrasena']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls,data):
        query = """INSERT INTO usuarios (nombre, apellido, email, contrasena) 
                    VALUES (%(nombre)s, %(apellido)s, %(email)s, %(contrasena)s);"""

        return connectToMySQL('esquema_publicaciones').query_db(query, data)

    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        resultados = connectToMySQL('esquema_publicaciones').query_db(query)

        usuarios = []

        for usuario in resultados:
            usuarios.append(cls(usuario))

        return usuarios

    @staticmethod
    def validar_registro(usuario):
        es_valido = True

        #Validar que el nombre tenga al menos 2 caracteres
        if (len(usuario['nombre'].strip())) < 2:
             flash("El nombre debe tener almenos 2 caracteres para registrarse","registro")
             es_valido = False

        # Validar que el apellido tenga al menos 2 caracteres
        if (len(usuario['apellido'].strip())) < 2:
            flash("El apellido debe tener almenos 2 caracteres para registrarse","registro")
            es_valido = False

        # Validar que las contraseñas sean iguales
        if usuario['contrasena'] != usuario['contrasena2']:
            flash("Las contrasenas ingresadas no coinciden", "registro")
            es_valido = False

        # Validar que el email no este en la BD
        if Usuario.get_by_email({'email': usuario['email']}):
            flash("El correo que quieres registrar, ya tine un usuario vinculado. Intente otro email", "registro")
            es_valido = False

        # Validar formato del email
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

        if not EMAIL_REGEX.match(usuario['email'].strip()):
            flash("Debes ingresar un correo electrónico válido","registro")
            es_valido = False

        return es_valido

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        result = connectToMySQL('esquema_publicaciones').query_db(query, data)
        if len(result) < 1:
            return False
        
        return cls(result[0])


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        result = connectToMySQL('esquema_publicaciones').query_db(query,data)

        return cls(result[0])

            