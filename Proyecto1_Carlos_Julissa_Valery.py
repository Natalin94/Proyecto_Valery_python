import time
# List of dictionaries to save the data, with default data
listaAdministradores=[{'usuario':'valery','contraseña':'valery123'}, {'usuario':'carlos','contraseña':'carlos123'}, {'usuario':'julissa','contraseña':'julissa123'}]
listaEstudiantes=[{'cedula':'201230123','nombre':'Andres','apellido':'Martinez Gonzales','direccion': 'Ciudad Quesada', 'telefono': '86543223', 'correo':'amartinez@itcr.ac.cr'}]
listaDocentes=[{'cedula':'201230198','nombre':'Margarita','apellido':'Campos Zamora','direccion': 'Ciudad Quesada', 'telefono': '89767654', 'correo':'mcampos@itcr.ac.cr'}]
listaCarreras=[{'nombre' : 'Ingeniería en Producción Industrial', 'codigo' : 'PI', 'cursos':['Intro', 'Mate'],'docentes':['201230198'],'estudiantes':['201230123']}, {'nombre' : 'Ingeniería Electrónica', 'codigo' : 'EL', 'cursos':['Calculo'],'docentes':[],'estudiantes':['Andres']},  {'nombre': 'Ingeniería en Computación', 'codigo' : 'IC', 'cursos':[],'docentes':[],'estudiantes':[]}]
listaCursos=[{'nombre' : 'Intro', 'codigo' : '01', 'recintos':['San Carlos'], 'aulas':['01'], 'horarios':[], 'docentes':['201230198'], 'estudiantes':['201230123']},{'nombre' : 'Mate', 'codigo' : '01', 'recintos':[], 'aulas':[], 'horarios':[], 'docentes':[], 'estudiantes':[]}, {'nombre' : 'Calculo', 'codigo' : '01', 'recintos':[], 'aulas':[], 'horarios':[], 'docentes':[], 'estudiantes':['Andres', 'Maria', 'Juan']}]
listaRecintos=[{'nombre':'San Carlos', 'direccion': 'Santa Clara frente al chino'}]
listaAulas=[{'codigo': '01', 'recinto': 'San Carlos'}]
listaHorarios=[{'nombre':'matutino','inicio':'8:00','fin':'11:00'}]

#Function to validate that the user is registered as administrator, to have access to system functions
def validarUsuario():
    print()
    print("            *** Login ***")
    print("Bienvenido al Sistema de Gestión Universitaria")
    print()
    usuario= input("Digite su nombre de usuario: ")
    contraseña= input("Digite su contraseña: ")

    validar= False
    for element in listaAdministradores:
        if element['usuario']== usuario:
            if element['contraseña']== contraseña:
                validar= True
                menu_principal()

    if validar == False:
        print("El usuario no se encuentra registrado.")
        validarUsuario()

def editarConstraseña():
    usuario= input("Digite su nombre de usuario: ")
    contraseña= input("Digite su contraseña actual: ")

    validar= False
    for element in listaAdministradores:
        if element['usuario']== usuario:
            if element['contraseña']== contraseña:
                nuevacontraseña=input("Digite su nueva contraseña: ")
                element['contraseña']= nuevacontraseña
                print("Contraseña editada con éxito")
                validar= True
                menu_principal()

    if validar == False:
        print("El usuario no se encuentra registrado.")
        validarUsuario()

## STUDENT MAINTENANCE
# Function to add new students
def agregarEstudiantes():
    nuevoEstudiante= {}

    cedulaEstudiante= input("Digite la cedula del nuevo estudiante: ")
    nombreEstudiante= input("Digite el nombre del nuevo estudiante: ")
    apellidosEstudiante= input("Digite los apellidos del nuevo estudiante: ")
    direccionEstudiante= input("Digite la direccion del nuevo estudiante: ")
    telefonoEstudiante= input("Digite el numero de telefono del nuevo estudiante: ")
    correoEstudiante= input("Digite el correo del TEC del nuevo estudiante: ")

    nuevoEstudiante["cedula"]=cedulaEstudiante
    boolean= False
    for element in listaEstudiantes:
        if element["cedula"]== cedulaEstudiante:
            boolean= True;

    if boolean == False:
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
        print(" ")
    else:
        print("El estudiante ya se encuentra registrado")
        print(" ")

#Function to edit students
def modificarEstudiante():
    cedulaEstudianteModificar= input("Digite la cedula del estudiante que desea modificar: ")
    valor=False
    for element in listaEstudiantes:
        if element["cedula"] == cedulaEstudianteModificar:
            valor= True
            print("Cual dato desea modificar?")
            print("1. Nombre")
            print("2. Apellidos")
            print("3. Direccion")
            print("4. Telefono")
            print("5. Correo")
            print("6. Salir")
            opcion= input("Seleccione la opción por modificar: ")
            if opcion == "1":
                nombre= input("Digite el nuevo nombre del estudiante")
                element["nombre"]= nombre
                print("Modificado con exito")
            if opcion == "2":
                apellido=input("Digite el nuevo apellido del estudiante")
                element["apellido"]= apellido
                print("Modificado con exito")

            if opcion == "3":
                direccion=input("Digite la nueva direccion del estudiante")
                element["direccion"]= direccion
                print("Modificado con exito")

            if opcion == "4":
                telefono=input("Digite el nuevo telefono del estudiante")
                element["telefono"]=telefono
                print("Modificado con exito")

            if opcion == "5":
                correo=input("Digite el nuevo correo del estudiante")
                if correo.find("@itcr.ac.cr") == -1:
                    print("El formato del correo no es correcto")
                    element["correo"]= "Formato no valido"
                else:
                    element["correo"]=correo
                    print("Modificado con exito")
            if opcion == "6":
                menu_administrativo()
    if valor== False:
        print("El estudiante no se encuentra registrado")
#Function to delete students
def eliminarEstudiante():
    cedulaEstudianteEliminar= input("Digite la cedula del estudiante que desea eliminar: ")

    for element in listaEstudiantes:
        if element["cedula"] == cedulaEstudianteEliminar:
            listaEstudiantes.remove(element)
            print("El estudiante fue eliminado con exito")
            print("")
        else:
            print("El estudiante no fue encontado en el sistema")
            "print"


def imprimirListaEstudiantes():
    print("Lista de estudiantes registrados")
    for e in listaEstudiantes:
        print("-", e["nombre"],e["apellido"])

def imprimirListaEstudiantesDocentes():
    print("Lista de docentes registrados")
    for e in listaDocentes:
        print("-", e["nombre"],e["apellido"])

def imprimirListaCarreras():
    print("Lista de carreras registrados")
    for e in listaCarreras:
        print("-", e["nombre"])

def imprimirListaCursos():
    print("Lista de cursos registrados")
    for e in listaCursos:
        print("-", e["nombre"])

def imprimirListaRecintos():
    print("Lista de recintos registrados")
    for e in listaRecintos:
        print("-", e["nombre"])

def imprimirListaAulas():
    print("Lista de aulas registradas")
    for e in listaAulas:
        print("-", e["codigo"])

def imprimirListaHorarios():
    print("Lista de horarios registrados")
    for e in listaHorarios:
        print("-", e["nombre"])
## TEACHER MAINTENANCE

# Function to add a new teacher
def agregarDocentes():
    nuevoDocente={}

    cedulaDocente= input("Digite la cedula del nuevo docente: ")
    nombreDocente=input("Digite el nombre del nuevo docente: ")
    apellidosDocente=input("Digite los apellidos del nuevo docente: ")
    direccionDocente=input("Digite la direccion del nuevo docente: ")
    telefonoDocente=input("Digite el numero de telefono del nuevo docente: ")
    correoDocente= input("Digite el correo del TEC del nuevo docente: ")

    nuevoDocente["cedula"]= cedulaDocente
    boolean=False
    for element in listaDocentes:
        if element["cedula"] == cedulaDocente:
            boolean=True;
    if boolean == False:
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
        print("Docente guardado con exito")
        print(" ")
    else:
        print("El docente ya se encuentra registrado")
        print(" ")


## Function to edit a teacher
def modificarDocentes():
    cedulaDocenteModificar=input("Digite la cedula del docentte que desea modificar: ")
    valor= False
    for element in listaDocentes:
        if element["cedula"] == cedulaDocenteModificar:
            valor= True
            print("Cual dato desea modificar?")
            print("1. Nombre")
            print("2. Apellidos")
            print("3. Direccion")
            print("4. Telefono")
            print("5. Correo")
            print("6. Salir")
            opcion=input("Seleccione la opción por modificar: ")
            if opcion == "1":
                nombre=input("Digite el nuevo nombre del docente")
                element["nombre"]=nombre
                print("Modificado con exito")
            if opcion == "2":
                apellido=input("Digite el nuevo apellido del docente")
                element["apellido"]=apellido
                print("Modificado con exito")

            if opcion == "3":
                direccion=input("Digite la nueva direccion del docente")
                element["direccion"]=direccion
                print("Modificado con exito")

            if opcion == "4":
                telefono=input("Digite el nuevo telefono del docente")
                element["telefono"]=telefono
                print("Modificado con exito")

            if opcion == "5":
                correo=input("Digite el nuevo correo del docente")
                if correo.find("@itcr.ac.cr") == -1:
                    print("El formato del correo no es correcto")
                    element["correo"]="Formato no valido"
                else:
                    element["correo"]=correo
                    print("Modificado con exito")
            if opcion == "6":
                menu_administrativo()
    if valor== False:
        print("El docente no se encuentra registrado")


#Function to delete a teacher
def eliminarDocente():
    cedulaDocenteEliminar= input("Digite la cedula del docente que desea eliminar: ")

    for element in listaDocentes:
        if element["cedula"] == cedulaDocenteEliminar:
            listaDocentes.remove(element)
            print("El docente fue eliminado con exito")
        else:
            print("El docente no fue encontado en el sistema")



## CAREER MAINTENANCE

# Function to add a new career
def agregarCarreras():
    nuevaCarrera={}

    codigoCarrera=input("Digite el código de la nueva carrera: ")
    nombreCarrera=input("Digite el nombre de la nueva carrera: ")
    boolean= False
    for element in listaCarreras:
        if element["codigo"]== codigoCarrera:
            boolean= True
    if boolean== False:
        nuevaCarrera["codigo"]=codigoCarrera
        nuevaCarrera["nombre"]=nombreCarrera
        nuevaCarrera["cursos"]= []
        nuevaCarrera["docentes"]=[]
        nuevaCarrera["estudiantes"]=[]

        listaCarreras.append(nuevaCarrera)
        print("Carrera agregada con exito")
        print(" ")
    else:
        print("La carrera con ese codigo ya se encuentra registrado")

## Function to edit a career
def modificarCarrera():
    codigoModificar= input("Digite el código de la carrera que desea modificar")
    valor=False
    for element in listaCarreras:
        if element["codigo"] == codigoModificar:
            valor= True
            print("Cual dato desea modificar?")
            print("1. Nombre")
            print("2. Salir")
            opcion= input("Digite la opción que desea seleccionar: ")
            if opcion == "1":
                nombre=input("Digite el nuevo nombre de la carrera")
                element["nombre"]=nombre
                print("Modificado con exito")
            if opcion == "2":
                menu_administrativo()
    if valor== False:
        print("La carrera no se encuentra registrada")


## Function to delete a career
def eliminarCarrera():
    codigoCarreraEliminar=input("Digite el código de la carrera que desea eliminar: ")

    for element in listaCarreras:
        if element["codigo"] == codigoCarreraEliminar:
            listaCarreras.remove(element)
            print("La carrera fue eliminada con exito")
        else:
            print("La carrera no fue encontrada en el sistema")

### MAINTAINING COURSES

# Function to add a new course
def agregarCursos():
    nuevoCurso={}

    codigoCurso=input("Digite el código del nuevo curso: ")
    nombreCurso=input("Digite el nombre del nuevo curso: ")

    valor= False
    for element in listaCursos:
        if element["codigo"]== codigoCurso:
            valor= True
    if valor== False:
        nuevoCurso["nombre"]=nombreCurso
        nuevoCurso["codigo"]=codigoCurso
        nuevoCurso["recintos"]=[]
        nuevoCurso["aulas"]=[]
        nuevoCurso["horarios"]=[]
        nuevoCurso["docentes"]=[]
        nuevoCurso["estudiantes"]=[]

        listaCursos.append(nuevoCurso)
        print("El curso ha sido agregado con exito")
        print(listaCursos)
        print("")
    else:
        print("El curso ya está registrado")
        print("")

# Function to edit a course
def modificarCursos():
    codigoModificar=input("Digite el código del curso que desea modificar")
    valor= False
    for element in listaCursos:
        if element["codigo"] == codigoModificar:
            print("Cual dato desea modificar?")
            valor= True
            print("1. Nombre")
            print("2. Salir")
            opcion=input("Digite la opción que desea seleccionar: ")
            if opcion == "1":
                nombre=input("Digite el nuevo nombre del curso")
                element["nombre"]=nombre
                print("Modificado con exito")
            if opcion == "2":
                menu_administrativo()
    if valor== False:
        print("El curso no se encuentra registrado")

# Function to delete a course
def eliminarCurso():
    codigoCursoEliminar=input("Digite el código del curso que desea eliminar: ")

    for element in listaCursos:
        if element["codigo"] == codigoCursoEliminar:
            listaCursos.remove(element)
            print("El curso fue eliminado con exito")
        else:
            print("El curso no fue encontrado en el sistema")


### MAINTENANCE OF ENCLOSURES:

# Function to add a new enclosures
def agregarRecinto():
    nuevoRecinto={}

    nombreRecinto=input("Digite el nombre del nuevo recinto: ")
    direccionRecinto=input("Digite la dirección física del nuevo recinto: ")

    nuevoRecinto["nombre"]=nombreRecinto
    nuevoRecinto["direccion"]=direccionRecinto

    listaRecintos.append(nuevoRecinto)

# Function to edit a enclosure
def modificarRecinto():
    nombreModificar=input("Digite el nombre del recinto que desea modificar")
    valor= False
    for element in listaRecintos:
        if element["nombre"] == nombreModificar:
            valor= True
            print("Cual dato desea modificar?")
            print("1. Dirección")
            print("2. Salir")
            opcion=input("Digite la opción que desea seleccionar: ")
            if opcion == "1":
                nombre=input("Digite la nueva dirección del recinto")
                element["direccion"]=nombre
                print("Modificado con exito")
            if opcion == "2":
                menu_administrativo()
    if valor== False:
        print("El recinto no se encuentra registrado")


# Function to delete a enclosure
def eliminarRecinto():
    nombreRecintoEliminar=input("Digite el nombre del recinto que desea eliminar: ")

    for element in listaRecintos:
        if element["nombre"] == nombreRecintoEliminar:
            listaRecintos.remove(element)
            print("El recinto fue eliminado con exito")
        else:
            print("El recinto no fue encontrado en el sistema")


## CLASSROOM MAINTENANCE

# Function to add a neww classroom
def agregarAula():
    nuevaAula={}

    codigoAula=input("Digite el código de la nueva aula: ")
    recintoAula=input("Digite el recinto al que pertenece la nueva aula: ")

    valor= False
    for element in listaAulas:
        if element["codigo"]== codigoAula:
            valor= True
    if valor== False:
        nuevaAula["codigo"]=codigoAula
        nuevaAula["recinto"]=recintoAula

        listaAulas.append(nuevaAula)
        print("El aula fue agregado con exito")
        print(" ")
    else:
        print("El aula ya se encuentra registrado")

# Function to edit a classroom
def modificarAula():
    codigoModificar=input("Digite el código del aula que desea modificar")
    valor= False
    for element in listaAulas:
        if element["codigo"] == codigoModificar:
            valor= True
            print("Cual dato desea modificar?")
            print("1. Recinto")
            print("2. Salir")
            opcion=input("Digite la opción que desea seleccionar: ")
            if opcion == "1":
                nombre=input("Digite el nuevo recinto del aula")
                element["recinto"]=nombre
                print("Modificado con exito")
            if opcion == "2":
                menu_administrativo()
    if valor== False:
        print("El recinto no se encuentra registrado")

# Function to delete a classroom
def eliminarAula():
    codigoAulaEliminar=input("Digite el codigo del aula que desea eliminar: ")

    for element in listaAulas:
        if element["codigo"] == codigoAulaEliminar:
            listaAulas.remove(element)
            print("El aula fue eliminado con exito")
        else:
            print("El aula no fue encontrado en el sistema")


## MAINTENANCE OF SCHEDULES

# Add a new schedules
def agregarHorario():
    nuevoHorario={}

    nombreHorario=input("Digite el nombre del nuevo horario: ")
    horaInicio=input("Digite la hora de inicio del nuevo horario: ")
    horaFinal=input("Digite la hora de fin del nuevo horario: ")

    valor= False
    for e in listaHorarios:
        if e["nombre"]== nombreHorario:
            valor= True
    if valor == False:
        nuevoHorario["nombre"]=nombreHorario
        nuevoHorario["inicio"]=horaInicio
        nuevoHorario["fin"]= horaFinal

        listaHorarios.append(nuevoHorario)
        print("El horario se agregó con exito")
        print("")
    else:
        print("El horario ya se encuentra registrado")
        print("")

# Edit a schedules
def modificarHorarios():
    nombreModificar=input("Digite el nombre del horario que desea modificar")
    valor = False
    for element in listaHorarios:
        if element["nombre"] == nombreModificar:
            valor= True
            print("Cual dato desea modificar?")
            print("1. Hora de Inicio")
            print("2. Hora Final")
            print("3. Salir")
            opcion= input("Digite la opción que desea seleccionar: ")
            if opcion == "1":
                inicio=input("Digite la nueva hora de inicio")
                element["inicio"]=inicio
                print("Modificado con exito")
            if opcion == "2":
                fin=input("Digite la nueva hora de fin")
                element["fin"]=fin
                print("Modificado con exito")
            if opcion == "3":
                menu_administrativo()
    if valor== False:
        print("El horario no se encuentra registrado")

# Delete a schedules
def eliminarHorario():
    nombreHorarioEliminar=input("Digite el nombre del horario que desea eliminar: ")

    for element in listaHorarios:
        if element["nombre"] == nombreHorarioEliminar:
            listaHorarios.remove(element)
            print("El horario fue eliminado con exito")
        else:
            print("El horario no fue encontrado en el sistema")


## SECCION OPERATIVA
## VINCULACIONES

# LINK COURSES WITH RACES

# ASSIGN COURSES TO RACES
def asignarCursosCarrera():
    carrera= input("Digite el código de la carrera a la que desea agregar un curso.")
    for element in listaCarreras:
        if element["codigo"] == carrera:
            curso= input("Digite el código del curso que desea vincular")
            for elemento in listaCursos:
                if elemento["codigo"] == curso:
                    element["cursos"].append(curso)
                    print("Vinculación exitosa")
                    print(listaCarreras)

                else:
                    print("El curso no se encuentra registrado")

# DISASSEMBLING COURSES TO RACES
def desasignarCursosCarrera():
    carrera=input("Digite el código de la carrera de la que desea desasignar un curso.")
    for element in listaCarreras:
        if element["codigo"] == carrera:
            curso= input("Digite el código del curso que desea desvincular")
            for elemento in element["cursos"]:
                if elemento == curso:
                    element["cursos"].remove(elemento)
                    print("Desvinculación exitosa")
                    print(listaCarreras)



## LINKED ENCLOSURES WITH COURSES

#ASSIGN COURSES TO COURSES
def asignarRecintosCursos():
    curso= input("Digite el código del curso al que desea agregar un recinto.")
    for element in listaCursos:
        if element["codigo"] == curso:
            recinto= input("Digite el nombre del recinto que desea vincular")
            for elemento in listaRecintos:
                if elemento["nombre"] == recinto:
                    element["recintos"].append(recinto)
                    print("Vinculación exitosa")
                    print(listaCursos)

                else:
                    print("El recinto no se encuentra registrado")

#DISASSEMBLING COURSES TO COURSES
def desasignarRecintosCursos():
    curso=input("Digite el código del curso del que desea desasignar un recinto.")
    for element in listaCursos:
        if element["codigo"] == curso:
            recinto= input("Digite el nombre del recinto que desea desvincular")
            for elemento in element["recintos"]:
                if elemento == recinto:
                    element["recintos"].remove(elemento)
                    print("Desvinculación exitosa")
                    print(listaCursos)

## LINK CLASSROOMS TO COURSES

# ASSIGN CLASSROOMS TO COURSES
def asignarAulasCursos():
    curso= input("Digite el código del curso al que desea agregar un aula.")
    for element in listaCursos:
        if element["codigo"] == curso:
            aula= input("Digite el codigo del aula que desea vincular")
            for elemento in listaAulas:
                if elemento["codigo"] == aula:
                    element["aulas"].append(aula)
                    print("Vinculación exitosa")
                    print(listaCursos)

                else:
                    print("El aula no se encuentra registrado")

#DISASSEMBLE CLASSROOMS TO COURSES
def desasignarAulasCursos():
    curso=input("Digite el código del curso del que desea desasignar un recinto.")
    for element in listaCursos:
        if element["codigo"] == curso:
            aula= input("Digite el codigo del aula que desea desvincular")
            for elemento in element["aulas"]:
                if elemento == aula:
                    element["aulas"].remove(elemento)
                    print("Desvinculación exitosa")
                    print(listaCursos)

## LINK SCHEDULES TO COURSES

# ASSIGN SCHEDULES TO COURSES
def asignarHorariosCursos():
    curso= input("Digite el código del curso al que desea agregar un horario.")
    for element in listaCursos:
        if element["codigo"] == curso:
            horario= input("Digite el nombre del horario que desea vincular")
            for elemento in listaHorarios:
                if elemento["nombre"] == horario:
                    element["horarios"].append(horario)
                    print("Vinculación exitosa")
                    print(listaCursos)

                else:
                    print("El horario no se encuentra registrado")

# DISASSEMBLE SCHEDULES TO COURSES
def desasignarHorariosCursos():
    curso=input("Digite el código del curso del que desea desasignar un horario.")
    for element in listaCursos:
        if element["codigo"] == curso:
            horario= input("Digite el nombre del horario que desea desvincular")
            for elemento in element["horarios"]:
                if elemento == horario:
                    element["horarios"].remove(elemento)
                    print("Desvinculación exitosa")
                    print(listaCursos)


## LINK STUDENTS TO COURSES

#ASSIGN STUDENTS TO COURSES
def asignarEstudiantesCursos():
    curso= input("Digite el código del curso al que desea agregar un estudiante.")
    for element in listaCursos:
        if element["codigo"] == curso:
            estudiante= input("Digite la cedula del estudiante que desea vincular")
            for elemento in listaEstudiantes:
                if elemento["cedula"] == estudiante:
                    element["estudiantes"].append(estudiante)
                    print("Vinculación exitosa")
                    print(listaCursos)

                else:
                    print("El estudiante no se encuentra registrado")
#DISASSEMBLING STUDENTS TO COURSES
def desasignarEstudiantesCursos():
    curso=input("Digite el código del curso del que desea desasignar un estudiante.")
    for element in listaCursos:
        if element["codigo"] == curso:
            estudiante= input("Digite la cedula del estudiante que desea desvincular")
            for elemento in element["estudiantes"]:
                if elemento == estudiante:
                    element["estudiantes"].remove(elemento)
                    print("Desvinculación exitosa")
                    print(listaCursos)

## LINKING COURSES TO COURSES

# ASSIGN TEACHERS TO COURSES
def asignarDocentesCursos():
    curso= input("Digite el código del curso al que desea agregar un docente.")
    for element in listaCursos:
        if element["codigo"] == curso:
            docente= input("Digite la cedula del docente que desea vincular")
            for elemento in listaDocentes:
                if elemento["cedula"] == docente:
                    element["docentes"].append(docente)
                    print("Vinculación exitosa")
                    print(listaCursos)

                else:
                    print("El docente no se encuentra registrado")

# UNLOCK TEACHERS TO COURSES
def desasignarDocentesCursos():
    curso=input("Digite el código del curso del que desea desasignar un docente.")
    for element in listaCursos:
        if element["codigo"] == curso:
            docente= input("Digite la cedula del docente que desea desvincular")
            for elemento in element["docentes"]:
                if elemento == docente:
                    element["docentes"].remove(elemento)
                    print("Desvinculación exitosa")
                    print(listaCursos)


## LINKED TEACHER WITH CAREER

# ASSIGN TEACHER TO CAREER
def asignarDocenteCarrera():
    carrera=input("Digite el código de la carrera a la que desea agregar un docente.")
    for element in listaCarreras:
        if element["codigo"] == carrera:
            docente=input("Digite la cedula del docente que desea vincular")
            for elemento in listaDocentes:
                if elemento["cedula"] == docente:
                    element["docentes"].append(docente)
                    print("Vinculación exitosa")
                    print(listaCarreras)

                else:
                    print("El docente no se encuentra registrado")

# ELIMINATE CAREER TEACHER
def desasignarDocentesCarrera():
    carrera=input("Digite el código de la carrera del que desea desasignar un docente.")
    for element in listaCarreras:
        if element["codigo"] == carrera:
            docente=input("Digite la cedula del docente que desea desvincular")
            for elemento in element["docentes"]:
                if elemento == docente:
                    element["docentes"].remove(elemento)
                    print("Desvinculación exitosa")
                    print(listaCarreras)


## CAREER TRAINING LINKAGE

# ASSIGN TEACHER TO CAREER
def asignarEstudiantesCarrera():
    carrera= input("Digite el código de la carrera al que desea agregar un estudiante.")
    for element in listaCarreras:
        if element["codigo"] == carrera:
            estudiante= input("Digite la cedula del estudiante que desea vincular")
            for elemento in listaEstudiantes:
                if elemento["cedula"] == estudiante:
                    element["estudiantes"].append(estudiante)
                    print("Vinculación exitosa")
                    print(listaCarreras)

                else:
                    print("El estudiante no se encuentra registrado")

def desasignarEstudiantesCarrera():
    carrera=input("Digite el código de la carrera del que desea desasignar un estudiante.")
    for element in listaCarreras:
        if element["codigo"] == carrera:
            estudiante= input("Digite la cedula del estudiante que desea desvincular")
            for elemento in element["estudiantes"]:
                if elemento == estudiante:
                    element["estudiantes"].remove(elemento)
                    print("Desvinculación exitosa")
                    print(listaCarreras)

## REPORTS
def reporteUno():
    estudiante= input("Digite el nombre del estudiante que desea ver: ")
    lista=[]
    localtime=time.asctime(time.localtime(time.time()))
    print("Hora Actual:", localtime)
    for element in listaCarreras:
        if estudiante in element["estudiantes"]:
            lista.append(element["nombre"])

    if len(lista)== 0:
        print("El estudiante no se encuentra en ninguna carrera")
    else:
        for e in lista:
            print(e)

def reporteDos():
    estudiante=input("Digite la cedula del estudiante que desea ver: ")
    localtime=time.asctime(time.localtime(time.time()))
    print("Hora Actual:", localtime)
    for element in listaCarreras:
        print(element["nombre"])
        for x in element["cursos"]:
            for curso in listaCursos:
                if curso["nombre"]== x:
                    if estudiante in curso["estudiantes"]:
                        print(" -", curso["nombre"])
    print(" ")

def reporteTres():
    docente=input("Digite la cedula del docente que desea ver: ")
    localtime=time.asctime(time.localtime(time.time()))
    print("Hora Actual:", localtime)
    for element in listaCarreras:
        print(element["nombre"])
        for x in element["cursos"]:
            for curso in listaCursos:
                if curso["nombre"] == x:
                    if docente in curso["docentes"]:
                        print(" -", curso["nombre"])
    print(" ")


def reporteCuatro():
    cursoMayor=0
    nomCursoMayor= ""
    localtime=time.asctime(time.localtime(time.time()))
    print("Hora Actual:", localtime)
    for element in listaCarreras:
        print(element["nombre"])
        for x in element["cursos"]:
            for curso in listaCursos:
                if x== curso["nombre"]:
                    if len(curso["estudiantes"]) >= cursoMayor:
                        cursoMayor= len(curso["estudiantes"])
                        nomCursoMayor= curso["nombre"]
        print(nomCursoMayor, "Cantidad: ", cursoMayor)

    print(" ")


def reporteCinco():
    cursoMayor=0
    nomCursoMayor=""
    localtime=time.asctime(time.localtime(time.time()))
    print("Hora Actual:", localtime)
    for element in listaCarreras:
        print(element["nombre"])
        for x in element["cursos"]:
            for curso in listaCursos:
                if x == curso["nombre"]:
                    if len(curso["estudiantes"]) <= cursoMayor:
                        cursoMayor=len(curso["estudiantes"])
                        nomCursoMayor=curso["nombre"]
        print(nomCursoMayor, "Cantidad: ", cursoMayor)

    print(" ")


def reporteSeis():
    cursoMayor=0
    nomCursoMayor=""
    horario=[]
    localtime=time.asctime(time.localtime(time.time()))
    print("Hora Actual:", localtime)
    for element in listaCarreras:
        print(element["nombre"])
        for x in element["cursos"]:
            for curso in listaCursos:
                if x == curso["nombre"]:
                    if len(curso["estudiantes"]) >= cursoMayor:
                        cursoMayor=len(curso["estudiantes"])
                        nomCursoMayor=curso["nombre"]
                        horario= curso["horarios"]
        print(nomCursoMayor, " Horario: ", horario)

    print(" ")


def reporteSiete():
    estudiante= input("Digite la cedula del estudiante que desea consultar")
    localtime=time.asctime( time.localtime(time.time()) )
    print("Hora Actual:", localtime)
    for element in listaCarreras:
        if estudiante in element["estudiantes"]:
            print(element["nombre"])
            for e in element["cursos"]:
                for c in listaCursos:
                    if e == c["nombre"]:
                        print("- ",c["nombre"])
                        if estudiante in c["estudiantes"]:
                            print("     Recintos:",c["recintos"])
                            print("     Aulas", c["aulas"])
                            print("     Horarios", c["horarios"])







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
        print("4.Ver lista de estudiante")
        print("5.Salir")
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
            imprimirListaEstudiantes()
            menu_administrativo()
        if opcion4 == "5":
            menu_administrativo()
        else:
            print("La opción no es valida")
            menu_administrativo()
    if opcion3=="2":
        print("1.Agregar nuevos docentes")
        print("2.Modificar docente")
        print("3.Eliminar docente")
        print("4.Ver lista de docentes")
        print("5.Salir")
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
            imprimirListaEstudiantesDocentes()
            menu_administrativo()
        if opcion4 == "5":
            menu_administrativo()
        else:
            print("La opción no es valida")
            menu_administrativo()
    if opcion3=="3":
        print("1.Agregar nueva carrera")
        print("2.Modificar carrera")
        print("3.Eliminar carrera")
        print("4.Ver lista de carreras")
        print("5.Salir")
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
            imprimirListaCarreras()
            menu_administrativo()
        if opcion4 == "5":
            menu_administrativo()
        else:
            print("La opción no es valida")
            menu_administrativo()
    if opcion3=="4":
        print("1.Agregar nuevo curso")
        print("2.Modificar curso")
        print("3.Eliminar curso")
        print("4.Ver lista de cursos")
        print("5.Salir")
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
            imprimirListaCursos()
            menu_administrativo()
        if opcion4 == "5":
            menu_administrativo()
        else:
            print("La opción no es valida")
            menu_administrativo()
    if opcion3=="5":
        print("1.Agregar nuevo recinto")
        print("2.Modificar recinto")
        print("3.Eliminar recinto")
        print("4.Ver lista de recintos")
        print("5.Salir")
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
            imprimirListaRecintos()
            menu_administrativo()
        if opcion4 == "5":
            menu_administrativo()
        else:
            print("La opción no es valida")
            menu_administrativo()
    if opcion3=="6":
        print("1.Agregar nueva aula")
        print("2.Modificar aula")
        print("3.Eliminar aula")
        print("4.Ver lista de aulas")
        print("5.Salir")
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
            imprimirListaAulas()
            menu_administrativo()
        if opcion4 == "5":
            menu_administrativo()
        else:
            print("La opción no es valida")
            menu_administrativo()
    if opcion3 == "7":
        print("1.Agregar nuevo horario")
        print("2.Modificar horario")
        print("3.Eliminar horario")
        print("4.Ver lista de horarios")
        print("5.Salir")
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
            imprimirListaHorarios()
            menu_administrativo()
        if opcion4 == "5":
            menu_administrativo()
        else:
            print("La opción no es valida")
            menu_administrativo()
    if opcion3=="8":
        return menu_principal()
    else:
        print("Error, opción inválida. Vuelva a intentarlo.")
        print()
        return menu_operativo()


def menu_reportes():
    print("Menú Reportes")
    print()
    print("En esta sección las opciones son: ")
    print("1.Reporte 1: Lista de carreras a la que un estudiante pertenece")
    print("2.Reporte 2: Lista de cursos por carrera que un estudiante pertenece")
    print("3.Reporte 3: Lista de cursos por carrera que un docente pertenece.")
    print("4.Reporte 4: Curso por cada carrera con más estudiantes matriculados.")
    print("5.Reporte 5: Curso por cada carrera con menos estudiantes matriculados.")
    print("6.Reporte 6: Horario de un curso de una carrera, con más estudiantes están matriculados.")
    print("7.Reporte 7: Carrera, cursos, recinto de cada curso, aula de cada recinto, horario de cada curso de un estudiante en específico.")
    print("8.Salir")
    print()
    opcion3=input("Digite la opcion que desea realizar: ")
    if opcion3=="1":
        reporteUno()
        menu_reportes()
    if opcion3=="2":
        reporteDos()
        menu_reportes()
    if opcion3=="3":
        reporteTres()
        menu_reportes()
    if opcion3=="4":
        reporteCuatro()
        menu_reportes()
    if opcion3=="5":
        reporteCinco()
        menu_reportes()
    if opcion3=="6":
        reporteSeis()
        menu_reportes()
    if opcion3 == "7":
        reporteSiete()
        menu_reportes()
    if opcion3 == "8":
        return menu_principal()
    else:
        print("Error, opción inválida. Vuelva a intentarlo.")
        print()
        return menu_reportes()


## MENU REPORTES

def menu_operativo():
    print("Menú Operativo")
    print()
    print("En esta sección las opciones de vinculación son: ")
    print("1.Cursos a carrera")
    print("2.Recinto a curso")
    print("3.Aula a un curso")
    print("4.Horario a un curso")
    print("5.Docente a una carrera")
    print("6.Docente a un curso")
    print("7.Estudiante a una carrera")
    print("8.Estudiante a un curso")
    print("9.Salir")
    print()
    opcion3=input("Digite la opcion que desea realizar: ")
    if opcion3 == "1":
        print("1.Agregar curso a una carrera")
        print("2.Eliminar curso de una carrera")
        print("3.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            asignarCursosCarrera()
            menu_operativo()
        if opcion4 == "2":
            desasignarCursosCarrera()
            menu_operativo()
        if opcion4 == "3":
            menu_operativo()
        else:
            print("La opción no es valida")
            menu_operativo()
    if opcion3 == "2":
        print("1.Agregar recinto a un curso")
        print("2.Eliminar recinto de un curso")
        print("3.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            asignarRecintosCursos()
            menu_operativo()
        if opcion4 == "2":
            desasignarRecintosCursos()
            menu_operativo()
        if opcion4 == "3":
            menu_operativo()
        else:
            print("La opción no es valida")
            menu_operativo()
    if opcion3 == "3":
        print("1.Agregar aula a un curso")
        print("2.Eliminar aula de un curso")
        print("3.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            asignarAulasCursos()
            menu_operativo()
        if opcion4 == "2":
            desasignarAulasCursos()
            menu_operativo()
        if opcion4 == "3":
            menu_operativo()
        else:
            print("La opción no es valida")
            menu_operativo()
    if opcion3 == "4":
        print("1.Agregar horario a un curso")
        print("2.Eliminar horario de un curso")
        print("3.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            asignarHorariosCursos()
            menu_operativo()
        if opcion4 == "2":
            desasignarHorariosCursos()
            menu_operativo()
        if opcion4 == "3":
            menu_operativo()
        else:
            print("La opción no es valida")
            menu_operativo()
    if opcion3 == "5":
        print("1.Agregar docente a una carrera")
        print("2.Eliminar docente de una carrera")
        print("3.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            asignarDocenteCarrera()
            menu_operativo()
        if opcion4 == "2":
            desasignarDocentesCarrera()
            menu_operativo()
        if opcion4 == "3":
            menu_operativo()
        else:
            print("La opción no es valida")
            menu_operativo()
    if opcion3 == "6":
        print("1.Agregar un docente a un curso")
        print("2.Eliminar docente de un curso")
        print("3.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            asignarDocentesCursos()
            menu_operativo()
        if opcion4 == "2":
            desasignarDocentesCursos()
            menu_operativo()
        if opcion4 == "3":
            menu_operativo()
        else:
            print("La opción no es valida")
            menu_operativo()
    if opcion3 == "7":
        print("1.Agregar estudiante a una carrera")
        print("2.Eliminar estudiante de una carrera")
        print("3.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            asignarEstudiantesCarrera()
            menu_operativo()
        if opcion4 == "2":
            desasignarEstudiantesCarrera()
            menu_operativo()
        if opcion4 == "3":
            menu_operativo()
        else:
            print("La opción no es valida")
            menu_operativo()

    if opcion3 == "8":
        print("1.Agregar estudiante a un curso")
        print("2.Eliminar estudiante de un curso")
        print("3.Salir")
        opcion4=input("Digite la opcion que desea realizar: ")
        if opcion4 == "1":
            asignarEstudiantesCursos()
            menu_operativo()
        if opcion4 == "2":
            desasignarEstudiantesCursos()
            menu_operativo()
        if opcion4 == "3":
            menu_operativo()
        else:
            print("La opción no es valida")
            menu_operativo()

    if opcion3 == "9":
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
    print("4.Editar contraseña")
    print("5.Volver al menú")
    print("6.Salir del sistema")
    print()
    opcion=input("Digite opción que desea realizar: ")
    if opcion=="1":
        print()
        return menu_administrativo()

    if opcion=="2":
        return menu_operativo()

    if opcion=="3":
        print()
        return menu_reportes()
    if opcion=="4":
        editarConstraseña()
        return menu_principal()

    if opcion=="5":
        print()
        return menu_principal()
    if opcion=="6":
        print()
        print ("Gracias por utilizar nuestro sistema.  ")
    else:
        print("Error, esa no es una de las opciones válidas...")
        print("Intenta una vez más")
        print("-----------------------------")
        return menu_principal()
        print()

validarUsuario()

