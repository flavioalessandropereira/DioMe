import ctypes

atributos_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('flavio.txt', atributos_ocultar)

if retorno:
    print('Arquivo ocultado')

else:
    print('Arquivo não ocultado')