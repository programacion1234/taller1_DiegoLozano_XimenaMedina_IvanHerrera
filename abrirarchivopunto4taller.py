## Realizado por Ivan Herrera, Ximena Molano, Diego Lozano'
## importamos las librerias necesarias
import wave
import struct
import math

## creamos clase archivo
class Archivo:
    ## se crea el arreglo que se llenara con el archivo de audio
    wavearray = []

    def __init__(self, nombre):
            self.nombre = nombre
            print self.nombre
    ## funcion que nos permite abrir el archivo de audio
    def Abrir(self):
        w = wave.open(self.nombre, 'rb')
        tamano =  w.getnframes()
        for i in range(0, tamano):
            waveData= w.readframes(1)
            data = struct.unpack("<h", waveData)
            Archivo.wavearray.append(int(data[0]))



def Main():

    print("Taller 1 ")


    nombre = raw_input("Ingrese la ruta y nombre del archivo que desea abrir: ")
    onda = Archivo(nombre)
    onda.Abrir()


    print ("Ingrese su opcion: ")
    opcion=input("1.valor pico 2.valor RMS 3.Leq: ")



## Se tomara siempre el valor pico dBFS en 8 bits
    if(opcion==1):
        valorpicodbfs=max(Archivo.wavearray)
        print("el valor pico en dBFS es ")
        print(valorpicodbfs)
## Esta opcion nos da el valor RMS
    if(opcion==2):

        tamano=len(Archivo.wavearray)
        suma=0
        for i in range (0, tamano):
            suma=suma+int(Archivo.wavearray[i])**2
        a=(suma/tamano)
        valorrmsdbfs=math.sqrt(a)

        print("el valor rms en dBFS es")
        print(valorrmsdbfs)

## esta opcion nos da el valor Leq donde la profundidad de bits sera 8
    if(opcion==3):

        tttt=0.000226757

        tamano=len(Archivo.wavearray)
        suma = 0
        for i in range (0, tamano):
            suma = suma+(int(Archivo.wavearray[i])**2)*tttt
        tiempo=tttt*tamano

        valorleqdbfs=20 * math.log10((1/tiempo)*(suma)/2**8)
        print("el valor leq en dBFS es ")
        print(valorleqdbfs)



if __name__ == "__main__":
    Main()