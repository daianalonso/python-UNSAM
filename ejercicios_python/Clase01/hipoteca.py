#Ejercicio 1.11

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 0
pago_extra = 1000
pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108

while saldo > 0:
	if mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_fin:
		total_pagado = total_pagado + pago_extra
		saldo = saldo - pago_extra
	if(saldo * (1+tasa/12) - pago_mensual < 0):
		total_pagado = 	total_pagado + saldo
		saldo = 0
	else:
		saldo = saldo * (1+tasa/12) - pago_mensual
		total_pagado = total_pagado + pago_mensual
	mes = mes + 1

	print(mes, round(total_pagado,2), round(saldo,2))

print(f'Total pagado: {total_pagado:0.2f}')
print(f'Meses: {mes}')