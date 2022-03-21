global listRe
listRe = list()
class Reservacion:

    def listaReservacion(self):
        r = Reservacion()
        opListRe = int(input("ingrese la cantidad de  reservaciones"))
        for i in range(opListRe):
            r.llegada = str(input("ingrese Fecha de llegada"))
            r.salida = str(input("ingrese fecha de salida"))
            listRe.append(r)
            print("-------------")
        r.mainReservacion()
        
    
    def visualizarReservacion(self):
        ViRe = Reservacion()
        for r in listRe:
           print("Fecha de llegada ",r.llegada,"\n fecha de salida", r.salida)
        ViRe.mainReservacion() 


    def mainReservacion(self):
            from main import main
            from sucursal import Sucursal
            from VUELO import Vuelo
            from turista import Turista
            print("Menu Reservacion")
            print("1.Añadir Reservacion\n2.-Visualizar Reservacion\n3.-Menu Sucursal \n4.-Menu Vuelo\n5.-Menu Turista\n. 6.-Regresar menu principal")
            print("")
            opMainRe = int(input("Ingrese la opcion a elijir\n>"))
            if opMainRe == 1:
                mainRe = Reservacion()
                mainRe.listaReservacion()
            elif opMainRe == 2:
                mainReser = Reservacion()
                mainReser.visualizarReservacion()
            elif opMainRe == 3:
                mainRe = Sucursal()
                mainRe.mainSucursal()
            elif opMainRe == 4:
                mainSuVu = Vuelo()
                mainSuVu.mainVuelo()
            elif opMainRe == 5:
                mainSuTu = Turista()
                mainSuTu.mainTurista()
            elif opMainRe == 6:
                main()
            else:
                exit("adios")
