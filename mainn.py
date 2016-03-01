from ondaygrafica import Seno
from ondaygrafica import Triangle
from ondaygrafica import Square
from ondaygrafica import DienteSierra
from archivar import Archivo

def Main():

        print ("Menu: Seleccione el tipo de onda que desea generar y graficar:")

    ##Se muestra el menu con las opciones a realizar correspondientes
        opcion = input("A) Ingrese 1 para onda seno , B) Ingrese 2 para onda cuadrada , C) Ingrese 3 para onda triangular , D) Ingrese 4 para onda diente de sierra : ")
        print ("Ingrese los valores solicitados")
        tono = input("Ingrese la frecuencia:")
        frecmuestreo = input("Ingrese la frecuencia de muestreo: ")
        nbits = input("Ingrese el numero de bits: ")
        duracion = input("Ingrese la duracion en segundos: ")
        nombre = raw_input("Ingrese el nombre del archivo a generar: ")
        nombre = (nombre+".wav")
        dBfSin = input("Digite el valor en dBfsPico de la senal: ")

        profundidadbits = (((10**(dBfSin/20.0))*2**nbits)/2.0)

    ##Sentencia if que indica que se escogio la opcion 1 y que llamara la funcion generar y graficar para la onda seno.
        if (opcion ==  1):
            print ("A continuacion se mostrara grafica seno")
            ondaaa = Seno(tono, frecmuestreo, profundidadbits, duracion)
            ondas = ondaaa.Generarseno()
            ondaaa.Graficar(ondas[:500])
            archivos = Archivo(frecmuestreo, profundidadbits, nombre)
            archivos.archivarmuestra(ondas)
    ##Sentencia if que indica que se escogio la opcion 1 y que llamara la funcion generar y graficar para la onda cuadrada.
        if (opcion == 2):
            print ("A continuacion se mostrara grafica cuadrada")
            ondaaa = Square(tono, frecmuestreo, profundidadbits, duracion)
            ondacuadrada = ondaaa.Generarsquare()
            ondaaa.Graficar(ondacuadrada[:500])
            archivos = Archivo(frecmuestreo, profundidadbits, nombre)
            archivos.archivarmuestra(ondacuadrada)
    ##Sentencia if que indica que se escogio la opcion 1 y que llamara la funcion generar y graficar para la onda triangular.
        if (opcion == 3):
            print ("A continuacion se mostrara grafica triangular")
            ondaaa = Triangle(tono, frecmuestreo, profundidadbits, duracion)
            ondatriangular = ondaaa.Generartriangle()
            ondaaa.Graficar(ondatriangular[:500])
            archivos = Archivo(frecmuestreo, profundidadbits, nombre)
            archivos.archivarmuestra(ondatriangular)
    ##Sentencia if que indica que se escogio la opcion 1 y que llamara la funcion generar y graficar para la onda diente de sierra.
        if (opcion == 4):
            print ("A continuacion se mostrara grafica diente de sierra")
            ondaaa = DienteSierra(tono, frecmuestreo, profundidadbits, duracion)
            ondasierra= ondaaa.Generardiente()
            ondaaa.Graficar(ondasierra[:500])
            archivos = Archivo(frecmuestreo, profundidadbits, nombre)
            archivos.archivarmuestra(ondasierra)



if __name__ == "__main__":
        Main()
