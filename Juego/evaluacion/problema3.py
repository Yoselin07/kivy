def leer_y_numerar_lineas(archivo_entrada, archivo_salida):
    with open(archivo_entrada, 'r') as entrada:
        lineas = entrada.readlines()
    
    with open(archivo_salida, 'w') as salida:
        for i, linea in enumerate(lineas, start=1):
            salida.write(f"{i}. {linea.strip()}\n")
            return
