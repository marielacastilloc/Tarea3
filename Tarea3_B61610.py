#!/usr/bin/env python
# coding: utf-8

# In[15]:


# IE-0405: Modelos Probabilísticos de Señales y Sistemas
# Tarea 3: Variables aleatorias múltiples
# Estudiante: Mariela Castillo Cabezas
# Carné: B61610
# Profesor: Fabian Abarca Calderón
# I Ciclo 2020

# Importamos algunos paquetes útiles
import numpy as np 
import scipy
from scipy import stats
import matplotlib.mlab as mlab 
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from pylab import plot, show, hist, title
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D


# Se realiza la lectura de los archivos proporcionados
datos_xy = pd.read_csv('xy.csv')
datos_xyp = pd.read_csv('xyp.csv')
xy = datos_xy.drop(['Unnamed: 0'], axis = 1)
xy_n = xy.to_numpy()


# 1. A partir de los datos, encontrar la mejor curva de ajuste (modelo probabilístico)
# para las funciones de densidad marginales de X y Y.
fX = np.sum(xy_n, axis = 1)
fY = np.sum(xy_n, axis = 0)


# Para X

# Se define mi eje x como: 
eje_x = np.linspace(5,15,len(fX))


# Se define la función de distribución gaussiana 
def normal(x,mu,sigma):
  return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(x-mu)**2/(2*sigma**2))


paramX, _ = curve_fit(normal,eje_x,fX) # obtengo los parámetros de mi función
print(paramX)
curva_x = norm.pdf(eje_x, paramX[0], paramX[1]) # param [0] corresponde a mu y param[1] corresponde a sigma
plt.xlabel('x')
plt.ylabel('fX')
plt.title('Función de densidad marginal de X')
plt.plot(eje_x,fX)
#plt.plot(eje_x,curva_x)
plt.show()

# Para Y

eje_y = np.linspace(5,25, len(fY))

paramY, _ = curve_fit(normal,eje_y,fY)
print(paramY)
curva_y = norm.pdf(eje_y, paramY[0], paramY[1])
plt.xlabel('y')
plt.ylabel('fY')
plt.title('Función de densidad marginal de Y')
plt.plot(eje_y, fY)
#plt.plot(eje_y,curva_y)
plt.show()
#plt.close()

# 2. Ver en archivo READ ME en GitHub

#3. Hallar los valores de correlación, covarianza y coeficiente de correlación (Pearson) 
 # para los datos y explicar su significado

xyp = pd.read_csv("xyp.csv",header = 0)

x_1 = xyp["x"] 
y_1 = xyp["y"] 
p_1 = xyp["p"]

#Correlación
correlacion = 0 
for i in range(len(xyp)):
    correlacion = correlacion + x_1[i]*y_1[i]*p_1[i]; 
print( "La correlacion es :" ,correlacion)

# Varianza 
covarianza = correlacion - (paramX[0]*paramY[0])
print( "La varianza es :" ,covarianza)


# Coeficiente de varianza

cv = covarianza/ (paramX[1]*paramY[1]*4)
print( "El coeficiente de varianza es :" ,cv)

#  4 Graficar las funciones de densidad marginales (2D), la función de densidad conjunta (3D).
#Curva fX
plt.xlabel('x')
plt.ylabel('fX')
plt.title('Curva obtenida de datos en x')
plt.plot(eje_x,fX)

#Curva de mejor ajuste para los valores de x
plt.xlabel('x')
plt.ylabel('fX')
plt.title('Curva de mejor ajuste para los datos en X')
plt.plot(eje_x,curva_x)
plt.show()

#Curva fY
plt.xlabel('y')
plt.ylabel('fY')
plt.title('Curva obtenida de datos en y')
plt.plot(eje_y,fY)

#Curva de mejor ajuste para los valores y 
plt.xlabel('y')
plt.ylabel('fY')
plt.title('Curva de mejor ajuste para datos en Y')
plt.plot(eje_y,curva_y)
plt.show()

a = plt.axes(projection = '3d')
X_1 = x_1
Y_1 = y_1 
Z_1 = p_1

a.plot_trisurf(X_1, Y_1, Z_1, cmap = 'twilight_shifted')


# In[ ]:




