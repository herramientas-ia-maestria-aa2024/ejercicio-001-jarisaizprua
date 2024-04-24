# Nombre de archivo
nombre_archivo = 'informacion.txt'

# Abrir el archivo en modo lectura (r -> read)
with open(nombre_archivo, 'r') as archivo:
    # Leer cada línea del archivo
    for linea in archivo:
        # Imprimir cada línea
        print(linea)
        #print(linea.strip()) # eliminar los saltos de línea al final de cada línea
