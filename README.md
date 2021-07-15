# AGENDAPP 

_Aplicación web desarrollado en Flask. Permite a los usuarios el registro de contactos(nombre, apellidos, telefono, email y foto)._

### Pre-requisitos 📋

_El programa cuenta con una base de datos (agenda-iainteractive.sql), la cuál sirve para poder guardar y mostrar los contactos_

```
Insertar el archivo agenda-iainteractive.sql en phpmyadmin, así como activar los servicios de Apache y MySQL en WAMPP, XAMPP ó LAMPP, dependiendo de cual se tenga instalado
```

_Es recomendable instalar un ambiente virtual de python. En caso de que se quiera saltar este paso, puede ir directamente al apartado de **Instalación 🔧**_

_Primeramente clonaremos el repositorio con el comando:_
```
git clone https://github.com/chrisECH/AgendApp.git
```

_Una vez clonado, dentro de la carpeta que se nos creó copiaremos la ruta de acceso, abriremos la terminal y nos posicionaremos en esa ruta utilizando el comando_
```
cd _ruta/de/nuestro/directorio/donde/esta/nuestro/repositorio_
```

_Ya estando en la ruta crearemos nuestro ambiente virtual con el comando:_
_Para el caso de windows:_
```
py -3 -m venv venv
```

_Para el caso de Mac/Linux:_
```
python3 -m venv venv
```

_Una vez creado el ambiente virtual, procederemos a activarlo con el comando:_
_Para el caso de Windows:_
```
venv\Scripts\activate
```

_Para el caso de Mac/Linux:_
```
. venv/bin/activate
```
Con esto ya estarà activado nuestro ambiente virtual y podemos instalar las librerias necesarias para el correcto funcionamiento de la pagina web

### Instalación 🔧

_Para el correcto funcionamiento de esta pagina es necesario instalar algunas librerias:_

_Primeramente debemos clonar el proyecto con el comando:_

_En caso de que haya creado el ambiente virtual puede saltarse este comando_
```
git clone https://github.com/chrisECH/AgendApp.git
```

_Para instalar las librerias ejecutamos los siquientes comandos:_

_Para instalar el framework **Flask**:_

```
pip install flask
```

_Para la conexión de la base de datos con nuestra aplicación web utilizamos la libreria **flask_mysqldb**, ejecutamos el comando:_

```
pip install flask_mysqldb
```

_Son todas las librerias que se utilizaron_


## Funcionamiento ⚙️
**Añadir contacto**
_Un usuario puede registrar un contacto, ingresando el nombre del contacto (obligatorio), apellido paterno (obligatorio), apellido materno(opcional), telefono(obligatorio), correo(obligatorio) y una foto (obligatoria). Estos datos son validados para que sigan una serie de reglas antes de ser enviados para ser registrados._

**Ver contactos**
_El usuario podrá ver los contactos que ha creado, estos datos se muestran en forma de tabla, en ella se encuentran la foto, el nombre del contacto, el telefono y una serie de opciones a hacer con el contacto, ya sea editarlo o eliminarlo._

**Editar contacto**
_Si el usuario desea editar el contacto, se mostrará otra vista con los datos actuales del contacto a editar, el usuario puede cambiar estos datos, como el nombre, apellidos, telefono, correo o la foto. Estos datos son validados y verificados de que no se repitan en la base de datos (solo el telefono y el correo.). Además, como en la sección de **Añadir contacto** se validan de igual manera para que sigan una serie de reglas antes de ser actualizados._

**Eliminar contacto**
_El usuario puede eliminar un contacto, antes de ser eliminado definitivamente se mostrará un modal donde indica el nombre del contacto a eliminar, así como su telefono._


## Construido con 🛠️

* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - El framework web usado
* [XAMPP](https://www.apachefriends.org/es/index.html) 
* [Bootstrap V 4.6.x](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - Usado para generar las vistas



