function validar() {
    
    //Variables donde almacenamos el valor de los inputs.
    var nombre = document.getElementById('nombre').value;
    var apellidop = document.getElementById('apellidop').value;
    var apellidom = document.getElementById('apellidom').value;
    var mail = document.getElementById('mail').value;
    var telefono = document.getElementById('telefono').value;
    var imagen = document.getElementById('fotoContacto').value;
    
    //Variables con expresiones regulares que sirven para validar el formulario
    var regexNombre = /^[a-zA-ZÀ-ÿ\s]{1,40}$/;
    var regexApmaterno = /^[a-zA-ZÀ-ÿ\s]{0,40}$/;
    var regexTelefono = /^[0-9]{10}$/;
    var regexMail = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;


    //Variables con los id de los divs para mostrar errores
    var errorNombre = document.getElementById('errorNombre');
    var errorApellidop = document.getElementById('errorApellidop');
    var errorApellidom = document.getElementById('errorApellidom');
    var errorTelefono = document.getElementById('errorTelefono');
    var errorEmail = document.getElementById('errorEmail');
    var errorImagen = document.getElementById('errorImagen');

    //Variables con los ids de los small que sirven de ayuda al usuario
    var nombreHelper = document.getElementById('nombreHelpBlocker');
    var apellidopHelper = document.getElementById('apellidopHelpBlocker');
    var apellidomHelper = document.getElementById('apellidomHelpBlocker');
    var telefonoHelper = document.getElementById('telefonoHelpBlocker');
    var emailHelper = document.getElementById('emailHelpBlocker');
    var imagenHelper = document.getElementById('imagenHelpBlocker');


    if (!regexNombre.test(nombre)) { //Verificamos la primera validacion (nombre)
        //Si no la cumple: 
        errorNombre.style.display='block'; //Muestra el div con el mensaje de error
        errorNombre.innerHTML = 'No es un nombre valido.'; //El mensaje que se mostrara en el div de error
        nombreHelper.style.display='none'; //ocultamos el small de ayuda debajo del input

        setTimeout(function(){ //Agregamos un timer para que se quite el error pasado dos segundos
            errorNombre.style.display='none'; // quitamos el mensaje de error
            nombreHelper.style.display='block'; //mostramos el small de ayuda
        }, 2000);
        
        return false; //retornamos un false 

    } else if (!regexNombre.test(apellidop)) { //Los siguientes if es exactamente lo mismo que el anterior a excepción de la validacion de iamgen

        errorApellidop.style.display='block';
        errorApellidop.innerHTML = 'No es un apellido paterno valido.';
        apellidopHelper.style.display='none';

        setTimeout(function(){ 
            errorApellidop.style.display='none';
            apellidopHelper.style.display='block';
        }, 2000);

        return false;
    } else if (!regexApmaterno.test(apellidom)) {
        errorApellidom.style.display='block';
        errorApellidom.innerHTML = 'No es un apellido materno valido.';
        apellidomHelper.style.display='none';

        setTimeout(function(){ 
            errorApellidom.style.display='none';
            apellidomHelper.style.display='block';
        }, 2000);
        
        return false;
    }else if(!regexTelefono.test(telefono)){
        errorTelefono.style.display='block';
        errorTelefono.innerHTML = 'No es un telefono valido.';
        telefonoHelper.style.display='none';

        setTimeout(function(){ 
            errorTelefono.style.display='none';
            apellidomHelper.style.display='block';
        }, 2000);
        
        return false;

    }else if (!regexMail.test(mail)) {
        errorEmail.style.display='block';
        errorEmail.innerHTML = 'No es un correo valido.';
        emailHelper.style.display='none';

        setTimeout(function(){ 
            errorEmail.style.display='none';
            emailHelper.style.display='block';
        }, 2000);

        return false;
    } else if(imagen === '') { //Lo unico que cambia aqui, es que no utilizamos una regex, simplemente verificamos que el input no sea vacio.
        errorImagen.style.display='block';
        errorImagen.innerHTML = 'No ha seleccionado una imagen';
        imagenHelper.style.display='none';

        setTimeout(function(){ 
            errorImagen.style.display='none';
            imagenHelper.style.display='block';
        }, 2000);

        return false;
    }else { //Si todas las validaciones pasan, retornamos un true

        return true;
    }
}

