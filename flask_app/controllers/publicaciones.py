from flask_app import app
from flask_bcrypt import Bcrypt
from flask import render_template, redirect, request, session, flash
from flask_app.models.usuario import Usuario
from flask_app.models.publicacion import Publicacion
import datetime


@app.route('/publicaciones/crear', methods=['POST'])
def crear():
    if 'usuario_id' not in session: #asegurar que el usuario es quien esta en sesion
        return redirect('/')
    
    if not Publicacion.validar_publicacion(request.form): # si esque la publicacion no es valido, 
        return redirect('/dashboard') #que redirigida a la misma pagina con los errores de registro
    
    datos = {
        'nombre': request.form['nombre'],
        'fecha': request.form['fecha'],
        'lugar': request.form['lugar'],
        'descripcion': request.form['descripcion'],
        'usuario_id': session['usuario_id'],
    }
    Publicacion.save(datos)
    return redirect('/dashboard')

@app.route('/publicaciones/ver/<int:id>')
def ver_publicacion(id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    publicacion = Publicacion.get_by_id({'id':id})
    #print(viaje_viajeros)
    if not publicacion:
        return redirect('/dashboard')
    return render_template('ver.html', publicacion=publicacion)

@app.route('/publicaciones/borrar/<int:id>')
def borrar_publicacion(id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    publicacion = Publicacion.get_by_id({'id':id})
    if publicacion and publicacion.usuario_id == session['usuario_id']:
        Publicacion.delete({'id':id})

    return redirect('/dashboard')

@app.route('/publicaciones/editar/<int:id>')
def editar_publicacion(id):
    if 'usuario_id' not in session:
        return redirect('/')
    
    publicacion = Publicacion.get_by_id({'id':id})

    if not publicacion:
        return redirect('/dashboard')
    
    if publicacion.usuario_id != session['usuario_id']:
        return redirect('/dashboard')
    
    return render_template('editar.html', publicacion=publicacion)    

@app.route('/publicaciones/actualizar/<int:id>', methods=['POST'])

def actualizar_publicacion(id):
    if 'usuario_id' not in session:
        return redirect('/')

    publicacion = Publicacion.get_by_id({'id': id})

    if not publicacion:
        return redirect('/dashboard')

    if publicacion.usuario_id != session['usuario_id']:
        return redirect('/dashboard')

    if not Publicacion.validar_publicacion(request.form):
        return redirect(f'/publicaciones/editar/{id}')

    datos = {
        'id': id, # está como parametro
        'nombre': request.form['nombre'],
        'fecha': request.form['fecha'],
        'lugar': request.form['lugar'],
        'descripcion': request.form['descripcion'],
        'usuario_id': session['usuario_id']
    }

    Publicacion.update(datos)

    return redirect('/dashboard')
