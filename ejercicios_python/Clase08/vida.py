#%% Ejercicio 8.1
from datetime import date, timedelta, datetime

def vida_en_segundos(fecha_nac):
    now = datetime.now()
    #Convierto el string 'dd/mm/AAAA' en datetime
    birth_date = datetime.strptime(fecha_nac, '%d/%m/%Y')
    #Hago la diferencia entre esas dos fechas y las muestro en segundos
    return (now - birth_date).total_seconds()

#%% Ejercicio 8.2
def dias_habiles(inicio, fin, feriados):
    primer_dia = datetime.strptime(inicio, '%d/%m/%Y')
    ultimo_dia = datetime.strptime(fin, '%d/%m/%Y')
    dias_entre_fechas = ultimo_dia - primer_dia

    fechas_feriados = [datetime.strptime(dia, '%d/%m/%Y') for dia in feriados]

    #Recorro todas los dias y cuento los sabados, domingos y feriados
    count_feriados = 0
    count_sat_sun = 0
    for d in range(dias_entre_fechas.days):
        date = primer_dia + timedelta(days=d)
        if date.weekday() > 4:
            count_sat_sun += 1
        if date in fechas_feriados:
            count_feriados += 1

    #Devuelvo la cantidad de días hábiles menos los feriados
    return dias_entre_fechas.days - count_sat_sun - count_feriados



if __name__ == '__main__':
    print(vida_en_segundos("01/10/2021"))
    feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']
    print(dias_habiles("20/09/2020", "10/10/2020", []))
    print(dias_habiles("20/09/2020", "24/11/2020", feriados))


# %%
