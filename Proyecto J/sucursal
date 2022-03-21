global listSucursal
listSucursal=list()


class Sucursal:

    def listaSucursal(self ):

        s=Sucursal()
        opListSu = int (input("ingrese la cantidad de sucursales"))
        for i in range (opListSu):
            s.codigo=str(input("ingrese codigo"))
            s.direccion=str(input("ingrese direccion"))
            s.telefono=str(input("ingrese telefono"))
            listSucursal.append(s)
            print("-------------")
        s.mainSucursal()
        
    def visualizarSucursal(self):
        for s in listSucursal:
           print("esto es codigo de sucursal\n",s.codigo,"esta es la direccion\n", s.direccion,
            "este es el telefono\n", s.telefono)
        ViSu =Sucursal()
        ViSu.mainSucursal()
                exit("adios")
                
    def mainSucursal(self):
            from main import main
            from turista import  Turista
            print("Menu Sucursal")
            print("1.Añadir sucursal\n2.-Visualizar sucursal\n3.-Menu hotel\n4.-Menu principal\n5.-Salir ")
            print("")
            opMainSu = int(input("Ingrese la opcion a elijir\n>"))
            if opMainSu == 1:
                mainsuc = Sucursal()
                mainsuc.listaSucursal()
            elif opMainSu == 2:
                mainSu = Sucursal()
                mainSu.visualizarSucursal()
            elif opMainSu == 3:
                mainSuHo = Hotel()
                mainSuHo = mainHotel()
            elif opMainSu == 4:
                main()
            else:
                exit("adios")
