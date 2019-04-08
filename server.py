#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import csv
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
        print (buf)
        b=str(buf, 'utf-8')
        print(b)
        option=ord(b[0])
        if b[0] == 'U':
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
        if b[0] == 'R':
            print("CSV TransactionLog, guardado correctamente.")
            with open ("transactionlog.csv","a") as csvfile:
                bNTipo=b[0:1]
                bNSensor=b[1:9]
                bNObservante=b[9:17]
                writer = csv.writer(csvfile)
                writer.writerow([bNTipo]+[bNSensor]+[bNObservante])