import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Parámetros de la distribución lognormal
mu = 1.0   # Media de la variable logarítmica
sigma = 0.5  # Desviación estándar de la variable logarítmica
n = 100  # Número de variables aleatorias a generar

# Generar n números aleatorios U ~ Uniform(0, 1)
U = np.random.uniform(0, 1, n)

# Transformada inversa para generar tiempos de inactividad lognormales
Z = mu + sigma * stats.norm.ppf(U)
T = np.exp(Z)  # Tiempos generados

# Mostrar los resultados
print("Tiempos de inactividad generados:", T)

# Graficar histograma de los tiempos de inactividad generados
plt.hist(T, bins=20, edgecolor='black', density=True)

# Graficar la función teórica de densidad de la distribución lognormal
x = np.linspace(min(T), max(T), 100)
pdf = stats.lognorm.pdf(x, sigma, scale=np.exp(mu))
plt.plot(x, pdf, 'r', label='Distribución lognormal teórica')

plt.title("Histograma de los tiempos de inactividad (Distribución Lognormal)")
plt.xlabel("Tiempo de inactividad")
plt.ylabel("Densidad de probabilidad")
plt.legend()
plt.show()