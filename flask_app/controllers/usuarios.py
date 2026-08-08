from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.usuario import Usuario
from flask_app.models.publicacion import Publicacion
from flask_bcrypt import Bcrypt 
import datetime

bcrypt = Bcrypt(app)

@app.route ('/')
def index ():
    return render_template('index.html')


@app.route('/registrar', methods = ['POST'])
def registrar():
    if not Usuario.validar_registro(request.form):
        return redirect('/')

    contrasena_hash = bcrypt.generate_password_hash(request.form['contrasena']).decode('utf-8')

    datos = {
        'nombre': request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email'],
        'contrasena': contrasena_hash,
    }
    usuario_id = Usuario.save(datos)

    if not usuario_id:
        flash('No fue posible completar el registro. Inténtalo nuevamente.','registro')
        return redirect('/')

    flash( 'Registro exitoso. Ya puedes iniciar sesión.','registro_exitoso')

    return redirect('/')


@app.route('/dashboard')
def dashboard():
    print(session)

    if 'usuario_id' not in session:
        print("No hay usuario logeado, no se puede mostrar en el dashboard.")
        return redirect('/')

    usuario = Usuario.get_by_id({'id':session['usuario_id']})
    publicaciones = Publicacion.get_all()
    print(publicaciones)
    
    return render_template('dashboard.html', usuario=usuario, publicaciones=publicaciones)

#Validaciones de Inicio de sesion
@app.route('/login', methods=['POST'])
def login():
    usuario = Usuario.get_by_email({'email':request.form['email']})
    if not usuario or not bcrypt.check_password_hash(usuario.contrasena, request.form['contrasena']):
        flash("Credenciales no validas, intente denuevo", "login")
        return redirect('/')

    session['usuario_id'] = usuario.id
    session['usuario_nombre'] = usuario.nombre

    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')