# IMPORTAMOS LAS CLASES: PERSONA Y DEPARTAMENTO
from Persona import Persona
from Departamento import Departamento



# CREACION DE DOS LISTAS PARA ALMACENAR VARIOS EMPLEADOS Y DEPARTAMENTOS
pers = list()
depto=list()

# FUNCION QUE MUESTRA UN MENU PARA EMPLEADOS: REGISTRO, IMPRIMIR LISTA DE EMPLEADOS Y SALIR
def menuEmpleado():
    opcE=0
    # CICLO PARA MOSTRAR EL MENU CON LAS OPCIONES DE REGISTRAR, VISUALIZAR Y SALIR
    while opcE != 3:

        print("\n 1.Registrar empleado")
        print("2.Visualizar listado de empleados")
        print("3. Salir")
        opcE=int(input("Seleccione una opción"))
        if opcE==1:
            # CREA UN OBJETO/INSTANCIA DE LA CLASE PERSONA
            p = Persona()
            # SE SOLICITA LA INFORMACIÓN PARA ALMACENAR EN LA LISTA
            control=int(input("Ingrese el numero de control del empleado:"))
            nom=input("Ingrese el nombre del empleado")
            depart=int(input("Ingrese el numero de departamento: "))
            sueldo=float(input("Ingrese el costo por hora: "))
            numhrs=int(input("Ingrese el numero de horas trabajadas: "))
            # SE LLAMA A LOS MÉTODOS DE LA CLASE PERSONA
            # SE PASA INFORMACION A CADA METODO
            p.ingresarNoControl(control)
            p.ingresarNombre(nom)
            p.ingresarDepto(depart)
            p.ingresarSueldoHr(sueldo)
            p.ingresarNumHrs(numhrs)

            # SE AGREGA LOS DATOS DE UN EMPLEADO A LA LISTA CREADA
            pers.append(p)
        elif opcE==2:

            # IMPRIME LOS DATOS DE LOS EMPLEADOS ALMACENADOS
            for p in pers:
                print(p.imprimir())
            # REGRESE AL MENU PRINCIPAL
        elif opcE==3:
            menuGeneral()

# FUNCION PARA MOSTRAR UN MENU CON LAS OPCIONES PARA DEPARTAMENTO: REGISTRAR, VISUALIZAR Y SALIR
def menuDepartamento():
    opcD = 0
    # CICLO QUE SE REPETIRA HASTA QUE SE TECLEE UN NUMERO DIFERENTE DE 3
    while opcD != 3:

        print("\n 1.Registrar departamento")
        print("2.Visualizar departametos")
        print("3. Salir")
        opcD = int(input("Seleccione una opción"))
        if opcD == 1:

            # CREA UN OBJETO/INSTANCIA DE LA CLASE DEPARTAMENTO
            d=Departamento()

            # SOLICITA LOS DATOS PARA DEPARTAMENTO
            clave=int(input("Ingrese el numero de departamento: "))
            nombreD=input("Ingrese el nombre del departamento: ")
            jefe=input("Ingrese el nombre del jefe:  ")
            tel=int(input("Ingrese el numero de telefono: "))

            # SE MANDA A LLAMAR LOS MÉTODOS DE LA CLASE DEPARTAMENTO
            d.ingresarClave(clave)
            d.ingresarNombreDepto(nombreD)
            d.ingresarJefe(jefe)
            d.ingresarTelefono(tel)

            # SE AGREGA LA INFORMACIÓN DE UN DEPARTAMENTO A LA LISTA
            depto.append(d)
        elif opcD==2:

            # SE IMPRIME LA INFORMACION DE LA LISTA
            for d in depto:
                print(d.imprimirD())
        elif opcD==3:

            # MUESTRA EL MENU PRINCIPAL
            menuGeneral()


def menuGeneral():
    opc=0
    while opc!=3:
        print ("\n 1. Empleado")
        print("2. Departamento")
        print("3. Salir")
        opc=int(input("Seleccione una opción"))
        if opc==1:
            menuEmpleado()
        elif opc==2:
            menuDepartamento()
        elif opc==3:
            print("FIN")

# SE LLAMA A LA FUNCION MENU PRINCIPAL
menuGeneral( )