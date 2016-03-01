import wave
import struct


class Archivo:
    def __init__(self, frecuencia, bits, nombre):
        self.frecuencia = frecuencia
        self.profundidadbits = bits
        self.nombre = nombre


    def archivarmuestra(self,datos):
        out = wave.open(self.nombre, 'w')
        Set_Bits = self.profundidadbits/8
        out.setparams((1, Set_Bits, self.frecuencia, 0, 'NONE', 'not compressed'))


        values = []
        for i in range(0, len(datos)):
            packed_value = struct.pack('<h', datos[i])
            values.append(packed_value)


        value_str = ''.join(values)
        out.writeframes(value_str)
        out.close()