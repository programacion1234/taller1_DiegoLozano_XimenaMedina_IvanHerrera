##Importamos librerias necesarias para que el programa genere la grafica y audio, y archivemos el mismo.
##Ivan Herrera,Ximena Medina,Diego Lozano

import math
import matplotlib.pylab as plt

##Se crea una clase y un arreglo vacio por cada tipo de onda.

##Creamos la clase para el tipo de onda seno
class Seno:

##Creamos un arreglo vacio para la clase seno, el cual se llenara con los datos correspondientes
	wavearray = []

##Definimos el metodo constructor de la clase con los argumentos de entrada correspondientes
	def __init__(self, frecuencia, muestreo, bits, duracion):
            self.frecmuestreo = muestreo
            self.profundidadbits = bits
            self.frecuencia = frecuencia
            self.numerosamples = muestreo * duracion
            self.amplitud = ((2**bits)/100)
            self.pi=math.pi
##metodo correspondiente para generar el audio
	def Generarseno(self):

            for i in range(0, self.numerosamples):
                sen = self.amplitud*math.sin((2*self.pi*self.frecuencia*i)/self.frecmuestreo)
                Seno.wavearray.append(sen)

            return Seno.wavearray
##metodo correspondiente para graficar el audio
	def Graficar(self,array):
            plt.plot(array,color="blue",linewidth=1.0, linestyle="-")
            plt.show()


##Creamos la clase para el tipo de onda cuadrada
class Square:

##Creamos un arreglo vacio para la clase cuadrada , el cual se llenara con los datos correspondientes
        wavearray=[]

##Definimos el metodo constructor de la clase con los argumentos de entrada correspondientes
	def __init__(self, frecuencia, muestreo, bits, duracion):
            self.frecmuestreo = muestreo
            self.profundidadbits = bits
            self.frecuencia = frecuencia
            self.numerosamples = muestreo * duracion
            self.amplitud = (2**bits)/2
            self.pi = math.pi
##metodo correspondiente para generar el audio
	def Generarsquare(self):
            for i in range(0, self.numerosamples):
                x=((4 / self.pi)*(2**self.profundidadbits))/100
                suma = 0
                for impar in range (1, 100 , 2):
                    muestra = math.sin((impar*self.pi*self.frecuencia*i)/self.frecmuestreo)
                    suma= suma + muestra
                s= suma * x
                Square.wavearray.append(s)

            return Square.wavearray
##metodo correspondiente para graficar el audio
	def Graficar(self,array):
            plt.plot(array,color="red",linewidth=1.0, linestyle="-")
            plt.show()

##Creamos la clase para el tipo de onda triangular
class Triangle:

##Creamos un arreglo vacio para la clase triangular, el cual se llenara con los datos correspondientes
        wavearray=[]

##Definimos el metodo constructor de la clase con los argumentos de entrada correspondientes
	def __init__(self, frecuencia, muestreo, bits, duracion):
            self.frecmuestreo = muestreo
            self.profundidadbits = bits
            self.frecuencia = frecuencia
            self.numerosamples = muestreo * duracion
            self.amplitud = (2**bits)/2
            self.pi = math.pi

##metodo correspondiente para generar el audio
	def Generartriangle(self):
            for i in range (0 , self.numerosamples):
                x = ((8 / self.pi**2)*(2**self.profundidadbits))/100
                suma = 0
                for impar in range(1, 100 , 2):
                    y = (-1**((impar -1)/2))/impar**2
                    muestra = y * math.sin((impar*self.pi*self.frecuencia*i)/self.frecmuestreo)
                    suma = suma + muestra
                t= suma * x
                Triangle.wavearray.append(t)


            return Triangle.wavearray

##metodo correspondiente para graficar el audio
	def Graficar(self,array):
            plt.plot(Triangle.wavearray,color="black",linewidth=1.0, linestyle="-")
            plt.show()

##Creamos la clase para el tipo de onda diente de sierra
class DienteSierra():

##Creamos un arreglo vacio para la clase diente de sierra, el cual se llenara con los datos correspondientes
        wavearray=[]

##Definimos el metodo constructor de la clase con los argumentos de entrada correspondientes
	def __init__(self, frecuencia, muestreo, bits, duracion):
            self.frecmuestreo = muestreo
            self.profundidadbits = bits
            self.frecuencia = frecuencia
            self.numerosamples = duracion * muestreo
            self.amplitud = (2**bits)/2
            self.pi = math.pi

##metodo correspondiente para generar el audio
	def Generardiente(self):
            for i in range (0 , self.numerosamples):
                x = ((0.5)-(1 / self.pi)*(2**self.profundidadbits))/100
                suma = 0

                for impar in range (1, 100):
                    muestra = (1/impar)*math.sin((impar*self.pi*self.frecuencia*i)/self.frecmuestreo)
                    suma = suma + muestra
                ds= suma * x
                DienteSierra.wavearray.append(ds)


            return DienteSierra.wavearray

##metodo correspondiente para graficar el audio
	def Graficar(self,array):
            plt.plot(DienteSierra.wavearray,color="green",linewidth=1.0, linestyle="-")
            plt.show()