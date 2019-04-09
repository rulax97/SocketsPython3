#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import csv
import re
# //*Autor: Raul Ernesto Perez Barcenas*//
# //*Matricula: 148661*//
# //*Version: 1.0*//
# //*Asignatura: Programacion Integrativa (UACJ)*//

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5)  # become a server socket, maximum 5 connections
while True:
    (connection, address) = serversocket.accept()
    buf = connection.recv(64)
    if len(buf) > 0:
        #print (buf)
        b=str(buf, 'utf-8')
        print(b)
        option=ord(b[0])
        if b[0] == 'U':
            #Validacion Checksum (nivel programa)
            bCompare=b[31:35]
            bCompare1=ord(bCompare[0])
            bCompare2=ord(bCompare[1])
            bCompare3=ord(bCompare[2])
            bCompare4=ord(bCompare[3])
            bCompareSum=bCompare1+bCompare2+bCompare3+bCompare4
            #print(bCompareSum)
            bOriginal=ord(b[31])+ord(b[32])+ord(b[33])+ord(b[34])
            #Validacion Checksum (nivel mensaje)
            if bOriginal == bCompareSum:
                print("CSV Data, guardado correctamente.")
            with open ("data.csv","a") as csvfile:
                bTipo=b[0:1]
                bSensor=b[1:9]
                bMedicion=b[9:17]
                bFecha=b[17:25]
                bTiempo=b[25:31]
                bCksum=b[31:35]
                writer = csv.writer(csvfile)
                writer.writerow([bTipo]+[bSensor]+[bMedicion]+[bFecha]+[bTiempo]+[bCksum]) 
                #b.send(b'Gracias por tu conexion') PENDIENTE EL RETORNO DE MENSAJE
                #connection.send(b'CORRECTO SERVER!')
        if b[0] == 'R':
            test_string =b[1:9]
            # printing original string 
            print("The original string is : " +  test_string)  
            # using regex( findall() ) 
            # to extract words from string 
            res = re.findall(r'\w+', test_string) 
            # printing result 
            print ("The list of words is : " +  str(res)) 
            print("CSV TransactionLog, guardado correctamente.")
            with open('data.csv', 'r') as f:
                reader = csv.reader(f)
                your_list = list(reader)
                print(your_list)
            with open ("transactionlog.csv","a") as csvfile:
                bNTipo=b[0:1]
                bNSensor=b[1:9]
                bNObservante=b[9:17]
                writer = csv.writer(csvfile)
                writer.writerow([bNTipo]+[bNSensor]+[bNObservante])
