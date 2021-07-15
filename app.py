############################################ L I B R E R I A S #################################################################
# || NOMBRE DE LA LIBRERIA -> COMANDO PARA INSTALARLA ||
#    Flask -> pip install flask 
#    flask_mysqldb -> pip install flask_mysqldb
#
################################################################################################################################


#Importamos lo necesario para que nuestra aplicacion de flask funciones
from flask import (Flask, render_template, request, url_for, Blueprint, g, Response, redirect, flash)
from flask_mysqldb import MySQL
from flask import send_from_directory
from datetime import datetime

import os

app = Flask(__name__)

#Configuramos la conexión con la base de datos a utilizar
app.config['MYSQL_HOST'] = 'localhost' #Asignamos el host que tiene nuestra base de datos, en este caso es localhost
app.config['MYSQL_USER'] = 'root' #Asignamos el usuario de ese host, en este caso el usuario es root
app.config['MYSQL_PASSWORD'] = '' #En caso de que tenga una contraseña la ingresamos aqui
app.config['MYSQL_DB'] = 'agenda-iainteractive' #Indicamos el nombre de la base de datos a utilizar
mysql = MySQL(app)

app.secret_key='mysecretkey' # En ocasiones manda un error si no se pone una llave secreta.

#Configuramos la carptea uploads para poder almacenar las fotos de los contactos que se suban
carpetaFotos = os.path.join('uploads') 
app.config['CARPETA'] = carpetaFotos


def phoneValidateDB(telefono): ##Funcion para validar que el telefono no exista en la base de datos al registar un contacto
    cursorTelefono = mysql.connection.cursor() #Inicializamos el cursor
    validate_phone = 'SELECT telefono FROM contactos WHERE telefono = %s' #Query para validar si hay otro telefono igual registrado
    cursorTelefono.execute(validate_phone, (telefono,)) #ejecutamos el query con los datos
    dataTelefono = cursorTelefono.fetchall() #El resultado lo asignamos a una tupla.
    if dataTelefono: #si la tupla no esta vacia
        return True #retornamos un True, indicando que hay un telefono registrado igual al que se intenta registrar
    
    return False #retornamos False, si la tupla esta vacia, esto quiere decir que no hay un telefono  registrado igual al que se intenta registrar

def mailValidateDB(correo): #Funcion para validar que el telefono no exista en la base de datos al registar un contacto
    cursorMail = mysql.connection.cursor()  #Inicializamos el cursor
    validate_correo = 'SELECT correo FROM contactos WHERE correo = %s'  #Query para validar si hay otro correo igual registrado
    cursorMail.execute(validate_correo, (correo,)) #ejecutamos el query con los datos
    dataCorreo = cursorMail.fetchall() #El resultado lo asignamos a una tupla.
    if dataCorreo: #si la tupla no esta vacia
        return True #retornamos un True, indicando que hay un correo registrado igual al que se intenta registrar
    
    return False #retornamos False, si la tupla esta vacia, esto quiere decir que no hay un correo  registrado igual al que se intenta registrar

def phoneValidateUpdate(telefono): #Funcion para validar que el telefono a actualizar no se repita dos veces.
    #La diferencia con el anterior de validar si existe el telefono registrado, es que en esta se verifica que el telefono no este dos veces.
    #Esto pues, habrá ocaciones en las que el usuario no quiera editar el telefono, entonces al intentar hacer update y utilizar la funcion anterior
    #Esta retornara un True, indicando que ese telefono ya esta registrado.
    cursorTelefono = mysql.connection.cursor() #Inicializamos el cursor
    validate_phone = 'SELECT telefono FROM contactos WHERE telefono = %s' #Query para verificar el telefono
    cursorTelefono.execute(validate_phone, (telefono,)) #ejecutamos el query con los datos
    dataTelefono = cursorTelefono.fetchall() #El resultado lo asignamos a una tupla.
    if len(dataTelefono) > 1: #si el tamaño de la tupla es mayor a 1 (cosa que no debe pasar puesto que los telefono son unicos) retornamos un True
        #Indicando que hay mas telefono iguales 
        return True
    
    return False #Retornamos False, si el tamaño de la tupla no es mayor a 1

def mailValidateUpdate(correo): #El funcionamiento de esta funcion es exactamente igual a la anterior, con la diferencia que aqui es el correo en lugar del telefono
    cursorMail = mysql.connection.cursor()
    validate_correo = 'SELECT correo FROM contactos WHERE correo = %s'
    cursorMail.execute(validate_correo, (correo,))
    dataCorreo = cursorMail.fetchall()
    if len(dataCorreo) > 1:
        return True
    
    return False



@app.route('/') #Definimos la ruta del index
def index(): #Definimos la funcion para el index
    return render_template('index.html') #Retornamos la plantilla del index


@app.route('/nuevo_contacto') #Definimos la ruta de agregar nuevo contacto
def nuevo_contacto(): #Definimos la funcion del agregar contactos
    return render_template('agregarContacto.html') #Retornamos la plantilla para agregar contactos

@app.route('/lista_contactos', methods=['GET']) #Definimos la ruta para la lista de contactos
def lista_contactos(): #Definimos la funcion para la lista de contactos
    cur = mysql.connection.cursor() #Inicializamos el cursor a la base de datos, y su conexión
    query_strin = 'SELECT id, nombres, telefono, foto FROM contactos' #Query que se hará a la base de datos
    cur.execute(query_strin) #Ejectuamos el query a la base de datos
    data = cur.fetchall() #Asignamos el resultado a una tupla

    return render_template('listaContactos.html', resultado = data) #Retornamos la plantilla listaContactos, junto con los datos que se
    #obtuvieron de la base de datos (Ver la plantilla listaContactos ubicada en templates/listaContactos.html, para ver el siguiente paso)



@app.route('/store', methods=['POST']) #Definimos la ruta al momento de registrar un contacto, junto con el metodo POST
def store(): #Definimos la funcion para registrar un contactos
    if request.method == 'POST': #Verificamos que el request sea de tipo POST
        #Asignamos los campos del formulario a una variable para posteriormente registrarlos
        nombre = request.form['nombre'] 
        apellidoP = request.form['apellidop']
        apellidoM = request.form['apellidom']
        telefono = request.form['telefono']
        correo = request.form['mail']
        fileImage = request.files['fotoContacto']

        #Esto nos servira para poder asignarle un nombre unico a la foto
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")

        #Verificamos que la imagen no este vacia (No debe de estar puesto que se valido previamente)
        if fileImage.filename!='':
            nuevoNombreFoto = tiempo+fileImage.filename #Asignamos una variable el el tiempo y el nombre de la foto
            fileImage.save("uploads/"+nuevoNombreFoto) #Guardamos la imagen con el nuevo nombre en la carpeta uploads

        cur = mysql.connection.cursor() #Inicializamos el cursor a la base de datos y la conexión
        phoneValidate = phoneValidateDB(telefono) #Mandamos llamar a la funcion que valida que no haya otro telefono igual registrado
        mailValidate = mailValidateDB(correo) #Mandamos llamar a la funcion que valida que no haya otro correo igual registrado


        if phoneValidate: #Si el resultado es True
            flash('El telefono ingresado ya se encuentra registrado.') #Mandamos un mensaje de error
            return redirect(url_for('nuevo_contacto')) #Redireccionamos nuevamente a la vista de agregarContacto

        if mailValidate:#Si el resultado es True
            flash('El correo ingresado ya se encuentra registrado.')  #Mandamos un mensaje de error
            return redirect(url_for('nuevo_contacto')) #Redireccionamos nuevamente a la vista de agregarContacto

        #Si ambos resultados son False, podemos contiguar con el registro a la base de datos

        query_strin = 'INSERT INTO contactos VALUES(NULL, %s, %s, %s, %s, %s, %s)' #Query para insertar en la base de datos los datos
        datos = (nombre, apellidoP, apellidoM, telefono, correo, nuevoNombreFoto) #Datos a insertar
        cur.execute(query_strin, datos) #Ejecutamos el query junto con los datos a insertar
        mysql.connection.commit() #Hacemos un commit para guardar los datos.

        flash('¡Su contacto se ha registrado con exito!') #Mandamos un mensaje de que los datos se registraron correctamente
        return redirect(url_for('index')) #Retornamos a la vista index


@app.route('/destroy/<int:id>') #Definimos la ruta para eliminar un contacto
def destroy(id): #Definimos la funcion para eliminar un contacto
    cur = mysql.connection.cursor() #Inicializamos el cursor a la base de datos junto con la conexión

    #Primero se eliminara la foto de la carpeta de uploads
    cur.execute("SELECT foto FROM contactos WHERE id = %s", (id,) ) #Ejecutamos el query a la base de datos para obtener el nombre de la foto
    fila = cur.fetchall() #Asignamos el resultado a una tupla
    os.remove(os.path.join(app.config['CARPETA'], fila[0][0])) #Removemos la foto de la carpeta

    cur.execute("DELETE FROM contactos WHERE id = %s",(id,)) #Ejecutamos el query junto con los datos, en este caso el id, para eliminr el contacto
    mysql.connection.commit() #Hcemos un commit para guardar los cambios
    return redirect(url_for('lista_contactos')) #Retornamos a la plantilla listaContactos.html


@app.route('/uploads/<nombreFoto>') #Definimos la ruta para mostrar las imagenes en la vista de listaContactos
def uploads(nombreFoto): #Definimos la funcion para mostrar las imagenes en la vista de listaContactos
    return send_from_directory(app.config['CARPETA'],nombreFoto) #Enviamos la fotos desde el directorio uploads para que se muestre la foto

@app.route('/edit/<int:id>') #Definimos la ruta para mostrar la vista de editar contacto
def edit(id): #Definimos la funcion para mostrar la vista de editar contacto
    cur = mysql.connection.cursor() #Inicializamos el cursor a la base de datos
    cur.execute("SELECT * FROM contactos WHERE id = %s", (id,) ) #Ejecutamos el query junto con los datos, en este caso el id
    contacto = cur.fetchall() #Asignamos el resultado a una tupla
    mysql.connection.commit()

    return render_template('editarContacto.html', resultado=contacto) #retornamos la vista junto con los datos obtenidos de la base de datos
    
@app.route('/update', methods=['POST']) #Definimos la ruta para editar el contacto, junto con el metodo POST
def update(): #Definimos la para funcion editar el contacto
    if request.method == 'POST':  #Verificamos que el request sea de tipo POST
        #Asignamos los campos del formulario a una variable para posteriormente actualizarlos
        id = request.form['id']
        nombre = request.form['nombre']
        apellidoP = request.form['apellidop']
        apellidoM = request.form['apellidom']
        telefono = request.form['telefono']
        correo = request.form['mail']
        fileImage = request.files['fotoContacto']

        cur = mysql.connection.cursor() #Inicializamos el cursor a la base de datos
        phoneValidate = phoneValidateUpdate(telefono) #Mandamos llamar a la funcion que valida que no haya dos telefonos iguales registrados
        mailValidate = mailValidateUpdate(correo) #Mandamos llamar a la funcion que valida que no haya dos correos iguales registrados

        if phoneValidate: #Si el resultado es True
            flash('El telefono ingresado ya se encuentra registrado.') #Mandamos un mensaje de error
            return redirect(url_for('lista_contactos')) #Reedirecionamos a la vista de listaContactos

        if mailValidate: #Si el resultado es True
            flash('El correo ingresado ya se encuentra registrado.') #Mandamos un mensaje de error
            return redirect(url_for('lista_contactos')) #Reedirecionamos a la vista de listaContactos

        #Query para actualizar los datos en la base de datos
        query_strin = 'UPDATE contactos SET nombres = %s, apellidop=%s, apellidom=%s, telefono = %s, correo = %s WHERE id = %s' 

        datos = (nombre, apellidoP, apellidoM, telefono, correo, id) #variables con los datos a actualizar

        #Nos servira para asignrale un nombre unico a la foto nueva
        now = datetime.now()
        tiempo = now.strftime("%Y%H%M%S")

        if fileImage.filename!='': #En caso de que haya un cambio en la foto del contacto
            nuevoNombreFoto = tiempo+fileImage.filename #Asignamos el tiempo y el nombre de la foto para un nuevo nombre unico
            fileImage.save("uploads/"+nuevoNombreFoto) #Guardamos la foto en la carpeta uploads

            cur.execute("SELECT foto FROM contactos WHERE id = %s", (id,)) #Obtenemos el nombre de la foto vieja guardada en la base de datos
            fila = cur.fetchall() #Asignamos el resultado a una tupla
            os.remove(os.path.join(app.config['CARPETA'], fila[0][0])) #Eliminamos la foto vieja de la carpeta uploads
            cur.execute("UPDATE contactos SET foto = %s WHERE id= %s", (nuevoNombreFoto, id)) #Actualizamos el nombre de la foto en la base de datos
            mysql.connection.commit() #Commit para guardar los cambios

        cur.execute(query_strin, datos) #Ejecutamos el query para actualizar los datos (sin la foto) en la base de datos 
        mysql.connection.commit() #Ejecutamos un commit para guardar los cambios

        flash('¡Su contacto se he modificado correctamente!') #Mandamos un mensaje de que se modifcaron correctamente
        return redirect(url_for('index')) #Reedirecionamos al index



if __name__ == '__main__': #Nos ayuda para poder inicializar nuestra aplicacion web de flask, sin esto no puede funcionar.
    app.run(port = 3000, debug = True)