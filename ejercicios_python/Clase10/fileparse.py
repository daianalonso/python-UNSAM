import csv
#%% Ejercicio 7.1
def parse_csv(lines, select = None, types = None, has_headers = True, silence_errors = False):
    #Si la lista no está vacía y no tiene encabezados, lanzar excepción.
    if (not silence_errors and select and has_headers == False):
        raise RuntimeError("Para seleccionar, necesito encabezados.")

    rows = csv.reader(lines)
    registros = []
    if has_headers:
        # Lee los encabezados
        headers = next(rows)
        #Si se indicó un selector de columas,
        #buscar los indices de las columnas especificas
        #Y en ese caso achicar el conjunto de encabezados
        if select:
            indices = [headers.index(nombre_columna) for nombre_columna in select]
            headers = select
        else:
            indices = []
        
        for i, row in enumerate(rows):
            if not row:    # Saltea filas sin datos
                continue
            if indices:
                row = [row[index] for index in indices]
            #Modifica los tipos de datos de los valores si se pasó por
            #parámetro los tipos
            if types:
                #Ejercicio 7.2
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as v:
                    if(silence_errors):
                        pass
                    else:
                        print("Fila", i, ": No pude convertir ", row)
                        print("Fila", i,": Motivo: ", v)
        #Armar el diccionario
            registro = dict(zip(headers, row))
            registros.append(registro)
    else:
        for row in rows:
            if not row:
                continue
            if types:
                row = [func(val) for func, val in zip(types, row)]
            registros.append(tuple(row))
    return registros


