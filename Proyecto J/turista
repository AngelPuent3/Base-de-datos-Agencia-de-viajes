global listTu
listTu = list()
class Turista:

    def listaTurista(self):
        t2 = Turista()
        opMainTu = int(input("ingrese cantidad de turistas"))
        for i in range(opMainTu):
            t2.codigoTu = int(input("ingrese codigo"))
            t2.nombreTu = str(input("ingrese su nombre"))
            t2.apellidoTu = str(input("ingrese su apellido"))
            t2.direccionTu = str(input("ingrese su direccion"))
            t2.telefonoTu = str(input("ingrese su telefono"))
            listTu.append(t2)
            print("-------------")
        t2.mainTurista()

    def mainTurista(self):
            from main import main
            from sucursal import Sucursal
            from ww import  Reservacion
            from VUELO import Vuelo
            print("Menu Turista")
            print("1.Añadir Turista\n2.-Visualizar Turista\n3.-Menu Turista \n4.-Menu Vuelo\n5.-Menu principal\n6.-salir")
            print("")
            opMainTu = int(input("Ingrese la opcion a elijir\n>"))
            if opMainTu == 1:
                mainTu = Turista()
                mainTu.listaTurista()
            elif opMainTu == 2:
                opMainTu = Turista()
                opMainTu.visualizarTurista()
            elif opMainTu == 3:
                mainTu = Turista()
                mainTu.mainTurista()
            elif opMainTu == 4:
                mainTuVu = Vuelo()
                mainTuVu.mainVuelo()
            elif opMainTu == 5:
                main()
            else:
                exit("adios")




    def visualizarTurista(self):
        ViTu = Turista()
        for t2 in listTu:
           print("Esto es codigo ",t2.codigoTu,"\n esto es tu nombre", t2.nombreTu,
                 "este es tu apellido \n",t2.apellidoTu,"esta es tu direccion",t2.direccionTu,"este es tu telefono",t2.telefonoTu)
        ViTu.mainTurista()
