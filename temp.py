import socket
import datetime
from dateutil.relativedelta import relativedelta
import sys
#//*Autor: Raul Ernesto Perez Barcenas*//
#//*Matricula: 148661*//
#//*Version: 1.0*//
#//*Asignatura: Programacion Integrativa (UACJ)*//

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
opcion = input("Ingresa una opcion: ")
if opcion=='U' or opcion=='u':
    opcion='U'
    mascara="XXXXXXXX"
    print("----Update----")
    nombresensor=input("Ingresa el nombre del sensor: ")
    if len(nombresensor) == len(mascara):
        print("Nombre correcto!")            
    else:
        print("Nombre incorrecto!")
        sys.exit()
    datomedicion=float(input("Ingresa el dato de medicion: "))
    if (datomedicion>=-99999.9 and datomedicion<=999999.9):    
        s_datomedicion=str(datomedicion) #conversion de float a string para mensaje
        if len(s_datomedicion) == 3:
            s_datomedicion=s_datomedicion+"00000"
        elif len(s_datomedicion) == 4:
            s_datomedicion=s_datomedicion+"0000"
        elif len(s_datomedicion) == 5:
            s_datomedicion=s_datomedicion+"000"
        elif len(s_datomedicion) == 6:
            s_datomedicion=s_datomedicion+"00"
        elif len(s_datomedicion) == 7:
            s_datomedicion=s_datomedicion+"0"
        if (s_datomedicion[0]=="-"):
            #print(s_datomedicion)
            print("Dato negativo indicado!")
        if len(s_datomedicion) == 3:
            s_datomedicion=s_datomedicion+"00000"
        if len(s_datomedicion) == 4:
            s_datomedicion=s_datomedicion+"0000"
        if len(s_datomedicion) == 5:
            s_datomedicion=s_datomedicion+"000"
        if len(s_datomedicion) == 6:
            s_datomedicion=s_datomedicion+"00"
        if len(s_datomedicion) == 7:
            s_datomedicion=s_datomedicion+"0"
        if len(s_datomedicion) == 8:
            print("Medición tomada correctamente.")
    fecha = datetime.datetime.now() + relativedelta(years=0) #instancia de fecha
    fecha_f = fecha.strftime("%d%m%Y") #parse fecha
    tiempo= fecha.strftime("%H%M%S") #parse tiempo
    mensaje=str(opcion+nombresensor+s_datomedicion+fecha_f+tiempo) #generacion mensaje 31 bytes
    #print(len(mensaje)) #longitud mensaje
    ck31=ord(mensaje[1])
    ck30=ord(mensaje[2])
    ck29=ord(mensaje[3])
    ck28=ord(mensaje[4])
    ck27=ord(mensaje[5])
    ck26=ord(mensaje[6])
    ck25=ord(mensaje[7])
    ck24=ord(mensaje[8])
    ck23=ord(mensaje[9])
    ck22=ord(mensaje[10])
    ck21=ord(mensaje[11])
    ck20=ord(mensaje[12])
    ck19=ord(mensaje[13])
    ck18=ord(mensaje[14])
    ck17=ord(mensaje[15])
    ck16=ord(mensaje[16])
    ck15=ord(mensaje[17])
    ck14=ord(mensaje[18])
    ck13=ord(mensaje[19])
    ck12=ord(mensaje[20])
    ck11=ord(mensaje[21])
    ck10=ord(mensaje[22])
    ck9=ord(mensaje[23])
    ck8=ord(mensaje[24])
    ck7=ord(mensaje[25])
    ck6=ord(mensaje[26])
    ck5=ord(mensaje[27])
    ck4=ord(mensaje[28])
    ck3=ord(mensaje[29])
    ck2=ord(mensaje[30])
    ck1=ord(mensaje[0])
    cksum=ck1+ck2+ck3+ck4+ck5+ck6+ck7+ck8+ck9+ck10+ck11+ck12+ck13+ck14+ck15+ck16+ck17+ck18+ck19+ck20+ck21+ck22+ck23+ck24+ck25+ck26+ck27+ck28+ck29+ck30+ck31
    #print(cksum)
    mensaje=mensaje+str(cksum)
    mensajebytes=mensaje.encode()
    clientsocket.send(mensajebytes)
elif opcion=='R' or opcion=='r':
    opcion='R'
    print("----Request----")
    mascara2="XXXXXXXX"
    namesensor=input("Ingresa el nombre del sensor: ")
    if len(namesensor) == len(mascara2):
        print("Nombre de sensor correcto!")            
    else:
        print("Nombre de sensor incorrecto!")
        sys.exit()
    nameobserver=input("Ingresa el nombre del observante: ")
    if len(nameobserver) == len(mascara2):
        print("Nombre de observante correcto!")            
    else:
        print("Nombre de observante incorrecto!")
        sys.exit()
    requestmensaje=opcion+namesensor+nameobserver
    print(requestmensaje)
    requestbytes=requestmensaje.encode()
    clientsocket.send(requestbytes)
else:
    print("Error no se selecciono la opción correcta")