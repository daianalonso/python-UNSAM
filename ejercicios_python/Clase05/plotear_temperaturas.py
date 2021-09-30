#%%
import matplotlib.pyplot as plt
import numpy as np

#Ejercicio 5.9
def plotear_temperaturas():
    temperaturas = np.load('../Data/temperaturas.npy')
    plt.hist(temperaturas,bins=25)
    plt.show()

if __name__ == '__main__':
    plotear_temperaturas()


# %%
