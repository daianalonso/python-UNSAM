import csv
#%% Ejercicio 6.6
def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo) as f:
        rows = csv.reader(f)
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
            
            for row in rows:
                if not row:    # Saltea filas sin datos
                    continue
                if indices:
                    row = [row[index] for index in indices]
                #Modifica los tipos de datos de los valores si se pasó por
                #parámetro los tipos
                if types:
                    row = [func(val) for func, val in zip(types, row)]
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