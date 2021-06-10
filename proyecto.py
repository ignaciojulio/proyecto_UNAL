import os 
from datetime import datetime

def clearConsole():
	command = 'clear'
	if os.name in ('nt', 'dos'): 
			command = 'cls'
	os.system(command)

parking=[]
for i in range(3):
	parking.append([])
	for __ in range(3):
		parking[i].append(0)

opciones = [1,2,3,4,5,6,7,8,9]

ventaDelDia = []

def menu():
    print("# # # # # # # # # # # #")
    print("#        Menu         #")
    print("#                     #")
    print("#      Opcion  1      #")
    print("# Entrada de Vehículo #")
    print("#                     #")
    print("#      Opcion  2      #")
    print("#  Salida de Vehículo #")
    print("#                     #")
    print("#      Opcion  3      #")
    print("#  Producido del Día  #")
    print("#                     #")
    print("#      Opcion  4      #")
    print("#   Cerrar Programa   #")
    print("# # # # # # # # # # # #")
    print("")
    option=int(input("Opcion: "))
    if option==1:
        clearConsole()
        parkingEntryPosition(vehicleType())
        return 1
    elif option==2: 
        clearConsole()
        recibo()
        return 2
    elif option==3:
        clearConsole()
        Producido()
        return 3
    elif option==4:
        clearConsole()
        exit()
        return 4
    else: 
        clearConsole()
        print("\nOpcion Incorrecta")
        menu()

def vehicleType():
    priceDictionary={'carro':5,'moto':3.30,'bicicleta':10}
    keyType=input("\nTipo de vehiculos: ")
    keyType=keyType.lower()
    while keyType != "carro" and keyType != "moto" and keyType !="bicicleta":
        print("\nError Vehiculo no permitido o mal escrito")
        keyType=input("\nTipo de vehiculos: ")
        keyType=keyType.lower()
    return priceDictionary[keyType],keyType

def timeVehicles(entradaOsalida): 
	time=-1
	cont=0
	while time<0 or time>240000:
		if cont>0:
			print("\n Error")
		print("\nFormato de Fecha (00:00:00 - 24:00:00)")
		time=input("\nTiempo " + entradaOsalida + " : ")
		for x in range(len(":")):
		  time=time.replace(":"[x],"")
		  time=int(time)
		cont=cont+1
	return time

def parkingEntryPosition(keyType):
    
    entry_time=timeVehicles("Entrada")

    parkinglocation=int(input("\nPosicion de estacionamiento: "))
    while parkinglocation not in opciones:
        print("\nEstacionamento no existente")
        parkinglocation=int(input("\nPosicion de estacionamiento: "))

    if parkinglocation==1 and parking[0][0]==0:
        parking[0][0]=keyType,entry_time
        return parking
    elif parkinglocation==2 and parking[0][1]==0:
        parking[0][1]=keyType,entry_time
        return parking
    elif parkinglocation==3 and parking[0][2]==0:
        parking[0][2]=keyType,entry_time
        return parking
    elif parkinglocation==4 and parking[1][0]==0:
        parking[1][0]=keyType,entry_time
        return parking
    elif parkinglocation==5 and parking[1][1]==0:
        parking[1][1]=keyType,entry_time
        return parking
    elif parkinglocation==6 and parking[1][2]==0:
        parking[1][2]=keyType,entry_time
        return parking
    elif parkinglocation==7 and parking[2][0]==0:
        parking[2][0]=keyType,entry_time
        return parking
    elif parkinglocation==8 and parking[2][1]==0:
        parking[2][1]==keyType,entry_time
        return parking
    elif parkinglocation==9 and parking[2][2]==0:
        parking[2][2]=keyType,entry_time
        return parking
    else:
        clearConsole()
        print("\nEstacionamento Ocupado")
        parkingEntryPosition(vehicleType())


def parkingExitPosition():
    parkingExitlocation=int(input("\nPosicion de estacionamiento: "))
    while parkingExitlocation not in opciones:
        print("\nEstacionamento no existente")
        parkingExitlocation=int(input("\nPosicion de estacionamiento: "))

    if parkingExitlocation==1 and parking[0][0]!=0:
        exit_time=timeVehicles("Salida")
        result=exit_time-parking[0][0][1]
        result=((result/10000)*60)/1
        receipt=parking[0][0][0][0]*int(result)
        a=0
        b=0
        return parking[0][0][0][1],parking[0][0][1],exit_time,result,receipt,a,b
    
    elif parkingExitlocation==2 and parking[0][1]!=0:
        exit_time=timeVehicles("Salida")
        result=exit_time-parking[0][1][1]
        result=((result/10000)*60)/1
        receipt=parking[0][1][0][0]*int(result)
        a=0
        b=1
        return parking[0][1][0][1],parking[0][1][1],exit_time,result,receipt,a,b
    
    elif parkingExitlocation==3 and parking[0][2]!=0:
        exit_time=timeVehicles("Salida")
        result=exit_time-parking[0][2][1]
        result=((result/10000)*60)/1
        receipt=parking[0][2][0][0]*int(result)
        a=0
        b=2        
        return parking[0][2][0][1],parking[0][2][1],exit_time,result,receipt,a,b
    
    elif parkingExitlocation==4 and parking[1][0]!=0:
        exit_time=timeVehicles("Salida")
        result=exit_time-parking[1][0][1]
        result=((result/10000)*60)/1
        receipt=parking[1][0][0][0]*int(result)
        a=1
        b=0
        return parking[1][0][0][1],parking[1][0][1],exit_time,result,receipt,a,b
    
    elif parkingExitlocation==5 and parking[1][1]!=0:
        exit_time=timeVehicles("Salida")
        result=exit_time-parking[1][1][1]
        result=((result/10000)*60)/1
        receipt=parking[1][1][0][0]*int(result)
        a=1
        b=1
        return parking[1][1][0][1],parking[1][1][1],exit_time,result,receipt,a,b
    
    elif parkingExitlocation==6 and parking[1][2]!=0:
        exit_time=timeVehicles("Salida")
        result=exit_time-parking[1][2][1]
        result=((result/10000)*60)/1
        receipt=parking[1][2][0][0]*int(result)
        a=1
        b=2
        return parking[1][2][0][1],parking[1][2][1],exit_time,result,receipt,a,b
    
    elif parkingExitlocation==7 and parking[2][0]!=0:
        exit_time=timeVehicles("Salida")
        result=exit_time-parking[2][0][1]
        result=((result/10000)*60)/1
        receipt=parking[2][0][0][0]*int(result)
        a=2
        b=0
        return   parking[2][0][0][1],parking[2][0][1],exit_time,result,receipt,a,b
    
    elif parkingExitlocation==8 and parking[2][1]!=0:
        exit_time=timeVehicles("Salida")
        result=exit_time-parking[2][1][1]
        result=((result/10000)*60)/1
        receipt=parking[2][1][0][0]*int(result)
        a=2
        b=1
        return  parking[2][1][0][1],parking[2][1][1],exit_time,result,receipt,a,b
    
    elif parkingExitlocation==9 and parking[2][2]!=0:
        exit_time=timeVehicles("Salida")
        result=exit_time-parking[2][2][1]
        result=((result/10000)*60)/1
        receipt=parking[2][2][0][0]*int(result)
        a=2
        b=2
        return parking[2][2][0][1],parking[2][2][1],exit_time,result,receipt,a,b
    else:
        clearConsole()
        print("\n Estacionamento vacio")
        parkingExitPosition()
        

def recibo():
    now = datetime.now()
    Fecha = now.strftime("%A, %d %B %Y")
    Tipodevehiculo ,Tiempodeentrada, Tiempodesalida , Tiempotranscurrido, Total , a,b= parkingExitPosition()
    Tabla = f"""\
    +-------------------------------------------+
    |                   RESIBO                  |
    +-------------------------------------------+
      Fecha: {Fecha}                            
      Tipo de vehiculo: {Tipodevehiculo}        
      Tiempo de entrada: {Tiempodeentrada}      
      Tiempo de salida: {Tiempodesalida}        
      Tiempo transcurrido: {Tiempotranscurrido} Minutos
    +-------------------------------------------+
      TOTAL ${Total}                             
    +-------------------------------------------+\
    """
    Tabla = (Tabla.format('\n'.join("| {:<8} |".format(*fila) 
    for fila in Fecha)))
    clearConsole()
    print (Tabla)
    ventaDelDia.append(int(Total))
    x=input("\nEnter para Seguir ")
    parking[a][b]=0
    return parking
    
def Producido():
    total=0
    for numero in range(len(ventaDelDia)):
        total+=ventaDelDia[numero]
    now = datetime.now()
    Fecha = now.strftime("%A, %d %B %Y")
    Tabla = f"""\
    +-------------------------------------------+
    |                   Total Dia               |
    +-------------------------------------------+
      Fecha: {Fecha}                            
    +-------------------------------------------+
      TOTAL ${total} del dia                    
    +-------------------------------------------+\
    """
    Tabla = (Tabla.format('\n'.join("| {:<8} |".format(*fila) 
    for fila in Fecha)))
    clearConsole()
    print (Tabla)
    x=input("\nEnter para Seguir ")
    
def main():
    clearConsole()
    while menu() != 4:
        clearConsole()
        menu()
        clearConsole()

if __name__ == '__main__':
    main()