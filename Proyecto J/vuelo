global listVu
listVu = list()
class Vuelo:

    def listaVuelo(self):
        v = Vuelo()
        opListVu = int(input("ingrese la cantidad de vuelos"))
        for i in range(opListVu):
            v.numeroVu = int(input("Ingrese numero de vuelo"))
            v.fechaVu = str (input("ingrese fecha de vuelo"))
            v.origenVu = str (input("ingrese el origen del vuelo"))
            v.destinoVu = str (input("ingrese el destino del vuelo"))
            v.plazatotalVu = int (input("ingrese la plazatotal"))
            v.plazaturista = int (input("ingrese la plaza turista"))
            listVu.append(v)
            print("-------------")
        v.mainVuelo()
        
    def visualizarVuelo(self):
        ViVu = Vuelo()
        for v in listVu:
           print("Numero de vuelo:",v.numeroVu,"\nFecha vuelo:", v.fechaVu,"\nOrigen vuelo:",v.origenVu,"\nDestino vuelo:",v.destinoVu,"\nPlaza total vuelo:",v.plazatotalVu,"\nPlaza tursta:",v.plazaturista)
        ViVu.mainVuelo()

    def mainVuelo(self):
            from main import main
            from sucursal import Sucursal
            from ww import Reservacion
            print("Menu Vuelo")
            print("1.Añadir Vuelo\n2.-Visualizar Vuelo\n3.-Menu Vuelo \n4.-Menu reservacion\n5.-Menu Turista\n. 6.-Regresar menu principal")
            print("")
            opMainVu = int(input("Ingrese la opcion a elijir\n>"))
            if opMainVu == 1:
                mainVu = Vuelo()
                mainVu.listaVuelo()
            elif opMainVu == 2:
                mainVu = Vuelo()
                mainVu.visualizarVuelo()
            elif opMainVu == 3:
                mainVuSu = Sucursal()
                mainVuSu.mainSucursal()
            elif opMainVu == 4:
                mainVuRe = Reservacion()
                mainVuRe.mainReservacion()
            elif opMainVu == 5:
                mainTu = Turista()
                mainTu.mainTurista()
            elif opMainVu == 6:
                main()
            else:
                exit("adios")
