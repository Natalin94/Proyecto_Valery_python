
listaAdministradores=[]
listaEstudiantes=[]
listaDocentes=[]
listaCarreras=[{'nombre' : 'Ingeniería en Producción Industrial', 'codigo' : 'PI'}, {'nombre' : 'Ingeniería Electrónica', 'codigo' : 'EL'},  {'nombre': 'Ingeniería en Computación', 'codigo' : 'IC'}]
listaCursos=[]
listaRecintos=[{'nombre':'San Carlos', 'direccion': 'Santa Clara frente al chino'}]
listaAulas=[]
listaHorarios=[]


## MANTENIMIENTO ESTUDIANTES
def agregarEstudiantes():
    nuevoEstudiante= {}

    nombreEstudiante= input("Digite el nombre del nuevo estudiante: ")
    apellidosEstudiante= input("Digite los apellidos del nuevo estudiante: ")
    direccionEstudiante= input("Digite la direccion del nuevo estudiante: ")
    telefonoEstudiante= input("Digite el numero de telefono del nuevo estudiante: ")
    correoEstudiante= input("Digite el correo del TEC del nuevo estudiante: ")

    nuevoEstudiante["nombre"]=nombreEstudiante
    nuevoEstudiante["apellido"]=apellidosEstudiante
    nuevoEstudiante["direccion"]= direccionEstudiante
    nuevoEstudiante["telefono"]=telefonoEstudiante
    nuevoEstudiante["correo"]=correoEstudiante
    if correoEstudiante.find("@itcr.ac.cr") == -1:
        print("El formato del correo no es correcto")
        nuevoEstudiante["correo"]= "Formato no valido"
    else:
        nuevoEstudiante["correo"]=correoEstudiante

    listaEstudiantes.append(nuevoEstudiante)
    print("Estudiante guardado con exito")

def modificarEstudiante():
    nombreEstudianteModificar= input("Digite el nombre del estudiante que desea modificar: ")

def eliminarEstudiante():
    nombreEstudianteEliminar= input("Digite el nombre del estudiante que desea eliminar: ")
    apellidosEstudianteEliminar= input("Digite los apellidos del estudiante que desea eliminar: ")

    for element in listaEstudiantes:
        if element["nombre"] == nombreEstudianteEliminar and element["apellido"] == apellidosEstudianteEliminar:
            listaEstudiantes.remove(element)
            print("El estudiante fue eliminado con exito")
        else:
            print("El estudiante no fue encontado en el sistema")




## MANTENIMIENTO DE DOCENTES
def agregarDocentes():
    nuevoDocente={}

    nombreDocente=input("Digite el nombre del nuevo docente: ")
    apellidosDocente=input("Digite los apellidos del nuevo docente: ")
    direccionDocente=input("Digite la direccion del nuevo docente: ")
    telefonoDocente=input("Digite el numero de telefono del nuevo docente: ")
    correoDocente= input("Digite el correo del TEC del nuevo docente: ")

    nuevoDocente["nombre"]=nombreDocente
    nuevoDocente["apellido"]=apellidosDocente
    nuevoDocente["direccion"]=direccionDocente
    nuevoDocente["telefono"]=telefonoDocente
    if correoDocente.find("@itcr.ac.cr") == -1:
        print("El formato del correo no es correcto")
        nuevoDocente["correo"]= "Formato no valido"
    else:
        nuevoDocente["correo"]=correoDocente


    listaDocentes.append(nuevoDocente)

def modificarDocentes():
    print("En mantenimiento")


def eliminarDocente():
    nombreDocenteEliminar= input("Digite el nombre del docente que desea eliminar: ")
    apellidosDocenteEliminar= input("Digite los apellidos del docente que desea eliminar: ")

    for element in listaDocentes:
        if element["nombre"] == nombreDocenteEliminar and element["apellido"] == apellidosDocenteEliminar:
            listaDocentes.remove(element)
            print("El docente fue eliminado con exito")
        else:
            print("El docente no fue encontado en el sistema")



## MANTENIMIENTO DE CARRERAS

def agregarCarreras():
    nuevaCarrera={}

    nombreCarrera=input("Digite el nombre de la nueva carrera: ")
    codigoCarrera=input("Digite el código de la nueva carrera: ")

    nuevaCarrera["nombre"]=nombreDocente
    nuevaCarrera["codigo"]=apellidosDocente

    listaCarreras.append(nuevaCarrera)

def modificarCarrera():
    print("En mantenimiento")

def eliminarCarrera():
    codigoCarreraEliminar=input("Digite el código de la carrera que desea eliminar: ")

    for element in listaCarreras:
        if element["codigo"] == codigoCarreraEliminar:
            listaCarreras.remove(element)
            print("La carrera fue eliminada con exito")
        else:
            print("La carrera no fue encontrada en el sistema")

### MANTENIMIENTO DE CURSOS

def agregarCursos():
    nuevoCurso={}

    nombreCurso=input("Digite el nombre del nuevo curso: ")
    codigoCurso=input("Digite el código del nuevo curso: ")

    nuevoCurso["nombre"]=nombreCurso
    nuevoCurso["codigo"]=codigoCurso

    listaCursos.append(nuevoCurso)

def modificarCursos():
    print("En mantenimiento")

def eliminarCurso():
    codigoCursoEliminar=input("Digite el código del curso que desea eliminar: ")

    for element in listaCursos:
        if element["codigo"] == codigoCursoEliminar:
            listaCursos.remove(element)
            print("El curso fue eliminado con exito")
        else:
            print("El curso no fue encontrado en el sistema")


### MANTENIMIENTO DE RECINTOS:


def agregarRecinto():
    nuevoRecinto={}

    nombreRecinto=input("Digite el nombre del nuevo recinto: ")
    direccionRecinto=input("Digite la dirección física del nuevo recinto: ")

    nuevoRecinto["nombre"]=nombreRecinto
    nuevoRecinto["codigo"]=direccionRecinto

    listaRecintos.append(nuevoRecinto)

def modificarRecinto():
    print("En mantenimiento")

def eliminarRecinto():
    nombreRecintoEliminar=input("Digite el nombre del recinto que desea eliminar: ")

    for element in listaRecintos:
        if element["nombre"] == nombreRecintoEliminar:
            listaRecintos.remove(element)
            print("El recinto fue eliminado con exito")
        else:
            print("El recinto no fue encontrado en el sistema")


## MANTENIMIENTO DE AULAS

def agregarAula():
    nuevaAula={}

    codigoAula=input("Digite el código de la nueva aula: ")
    recintoAula=input("Digite el recinto al que pertenece la nueva aula: ")

    nuevaAula["codigo"]=codigoAula
    nuevaAula["recinto"]=recintoAula

    listaAulas.append(nuevaAula)

def modificarAula():
    print("En mantenimiento")

def eliminarAula():
    codigoAulaEliminar=input("Digite el codigo del aula que desea eliminar: ")

    for element in listaAulas:
        if element["codigo"] == codigoAulaEliminar:
            listaAulas.remove(element)
            print("El aula fue eliminado con exito")
        else:
            print("El aula no fue encontrado en el sistema")


## MANTENIMIENTO HORARIOS

def agregarHorario():
    nuevoHorario={}

    nombreHorario=input("Digite el nombre del nuevo horario: ")
    horaInicio=input("Digite la hora de inicio del nuevo horario: ")
    horaFinal=input("Digite la hora de fin del nuevo horario: ")

    nuevoHorario["nombre"]=nombreHorario
    nuevoHorario["inicio"]=horaInicio
    nuevoHorario["fin"]= horaFinal

    listaHorarios.append(nuevoHorario)

def modificarHorarios():
    print("En mantenimiento")

def eliminarHorario():
    nombreHorarioEliminar=input("Digite el nombre del horario que desea eliminar: ")

    for element in listaHorarios:
        if element["nombre"] == nombreHorarioEliminar:
            listaHorarios.remove(element)
            print("El horario fue eliminado con exito")
        else:
            print("El horario no fue encontrado en el sistema")

## MENU MANTENIMIENTOS
def menu_administrativo():
    print("Menú Administrativo")
    print()
    print("En esta sección las opciones son: ")
    print("1.Estudiantes")
    print("2.Docentes")
    print("3.Carreras")
    print("4.Cursos")
    print("5.Recinto")
    print("6.Aula")
    print("7.Horario")
    print("8.Salir")
    print()
    opcion3=input("Digite la opcion que desea realizar: ")
    if opcion3=="1":
        print("1.Agregar nuevos estudiantes")
        print("2.Modificar estudiante")
        print("3.Eliminar estudiante")
        print("4.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            agregarEstudiantes()
            menu_administrativo()
        if opcion4 == "2":
            modificarEstudiante()
            menu_administrativo()
        if opcion4 == "3":
            eliminarEstudiante()
            menu_administrativo()
        if opcion4 == "4":
            menu_administrativo()
        else:
            print("La opción no es valida")
            menu_administrativo()
    if opcion3=="2":
        print("1.Agregar nuevos docentes")
        print("2.Modificar docente")
        print("3.Eliminar docente")
        print("4.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            agregarDocentes()
            menu_administrativo()
        if opcion4 == "2":
            modificarDocentes()
            menu_administrativo()
        if opcion4 == "3":
            eliminarDocente()
            menu_administrativo()
        if opcion4 == "4":
            menu_administrativo()
        else:
            print("La opción no es valida")
            menu_administrativo()
    if opcion3=="3":
        print("1.Agregar nueva carrera")
        print("2.Modificar carrera")
        print("3.Eliminar carrera")
        print("4.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            agregarCarreras()
            menu_administrativo()
        if opcion4 == "2":
            modificarCarrera()
            menu_administrativo()
        if opcion4 == "3":
            eliminarCarrera()
            menu_administrativo()
        if opcion4 == "4":
            menu_administrativo()
        else:
            print("La opción no es valida")
            menu_administrativo()
    if opcion3=="4":
        print("1.Agregar nuevo curso")
        print("2.Modificar curso")
        print("3.Eliminar curso")
        print("4.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            agregarCursos()
            menu_administrativo()
        if opcion4 == "2":
            modificarCursos()
            menu_administrativo()
        if opcion4 == "3":
            eliminarCurso()
            menu_administrativo()
        if opcion4 == "4":
            menu_administrativo()
        else:
            print("La opción no es valida")
            menu_administrativo()
    if opcion3=="5":
        print("1.Agregar nuevo recinto")
        print("2.Modificar recinto")
        print("3.Eliminar recinto")
        print("4.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            agregarRecinto()
            menu_administrativo()
        if opcion4 == "2":
            modificarRecinto()
            menu_administrativo()
        if opcion4 == "3":
            eliminarRecinto()
            menu_administrativo()
        if opcion4 == "4":
            menu_administrativo()
        else:
            print("La opción no es valida")
            menu_administrativo()
    if opcion3=="6":
        print("1.Agregar nueva aula")
        print("2.Modificar aula")
        print("3.Eliminar aula")
        print("4.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            agregarAula()
            menu_administrativo()
        if opcion4 == "2":
            modificarAula()
            menu_administrativo()
        if opcion4 == "3":
            eliminarAula()
            menu_administrativo()
        if opcion4 == "4":
            menu_administrativo()
        else:
            print("La opción no es valida")
            menu_administrativo()
    if opcion3 == "7":
        print("1.Agregar nuevo horario")
        print("2.Modificar horario")
        print("3.Eliminar horario")
        print("4.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            agregarHorario()
            menu_administrativo()
        if opcion4 == "2":
            modificarHorarios()
            menu_administrativo()
        if opcion4 == "3":
            eliminarHorario()
            menu_administrativo()
        if opcion4 == "4":
            menu_administrativo()
        else:
            print("La opción no es valida")
            menu_administrativo()
    if opcion3=="8":
        return menu_principal()
    else:
        print("Error, opción inválida. Vuelva a intentarlo.")
        print()
        return menu_administrativo()



## MENU PRINCIPAL
def menu_principal():
    print()
    print("            *** Menú Principal ***")
    print("Bienvenido al Sistema de Gestión Universitaria")
    print()
    print("Estas son las opciones que están a su disposición")
    print("1.Sección administrativa")
    print("2.Sección operativa")
    print("3.Reportes")
    print("4.Volver al menú")
    print("5.Salir del sistema")
    print()
    opcion=input("Digite opción que desea realizar: ")
    if opcion=="1":
        print()
        return menu_administrativo()

    if opcion=="2":
        return menu_administrativo()

    if opcion=="3":
        print()
        return menu_administrativo()

    if opcion=="4":
        print()
        return menu_principal()
    if opcion=="5":
        print()
        print ("Gracias por utilizar nuestro sistema.  ")
    else:
        print("Error, esa no es una de las opciones válidas...")
        print("Intenta una vez más")
        print("-----------------------------")
        return menu_principal()
        print()
menu_principal()