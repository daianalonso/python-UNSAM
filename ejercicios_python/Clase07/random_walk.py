#%% Ejercicio 7.12
import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000
cant_caminatas = 12
caminatas  = [randomwalk(N) for caminata in range(cant_caminatas)]
#Busco cual fue la caminata que más se alejó
valores_mas_lejanos = []
for caminata in caminatas:
    xmax = np.abs(caminata).max()
    valores_mas_lejanos.append(xmax)
idx_caminata_lejana = valores_mas_lejanos.index(max(valores_mas_lejanos))

#Busco cual fue la caminata que más se acercó
valores_mas_cercanos = []
for caminata in caminatas:
    xmin = np.abs(caminata).min()
    valores_mas_cercanos.append(xmin)
idx_caminata_cercana = valores_mas_cercanos.index(min(valores_mas_cercanos))

fig = plt.figure(figsize=(8, 4)) 
plt.subplot(2, 1, 1) # define la figura de arriba
plt.title(f'12 Caminatas al azar', fontsize = 12)
for c in caminatas:
    plt.plot(c)
plt.xlabel("tiempo", fontsize = 10)
plt.ylabel("distancia al origen", fontsize = 10)
plt.xlim(0, 100000)
plt.ylim(-800, 800)

plt.subplot(2, 2, 3) 
plt.plot(caminatas[idx_caminata_lejana])
plt.title(f'La caminata que más se aleja', fontsize = 12)
plt.xlabel("tiempo", fontsize = 10)
plt.ylabel("distancia al origen", fontsize = 10)
plt.xlim(0, 100000)
plt.ylim(-800, 800)

plt.subplot(2, 2, 4) 
plt.plot(caminatas[idx_caminata_cercana])
plt.title(f'La caminata que menos se aleja', fontsize = 12)
plt.xlabel("tiempo", fontsize = 10)
plt.ylabel("distancia al origen", fontsize = 10)
plt.xlim(0, 100000)
plt.ylim(-800, 800)

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=1.2, 
                    wspace=0.4, 
                    hspace=0.4)

plt.show()
# %%

