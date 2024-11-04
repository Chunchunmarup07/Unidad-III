import numpy as np
import matplotlib.pyplot as plt

# Parámetro de la distribución exponencial (tasa de servicio)
lambda_servicio = 1 / 2  # Tiempo promedio de servicio = 2 minutos

# Función para generar un tiempo de servicio
def generar_tiempo_servicio(lambda_servicio):
    u = np.random.uniform(0, 1)  # Generar número aleatorio uniforme
    tiempo_servicio = -1 / lambda_servicio * np.log(1 - u)  # Aplicar transformada inversa
    return tiempo_servicio

# Generar 100 tiempos de servicio
tiempos_servicio = [generar_tiempo_servicio(lambda_servicio) for _ in range(100)]

# Mostrar los tiempos de servicio
print("Tiempos de servicio generados:", tiempos_servicio)

# Graficar los tiempos de servicio simulados
plt.hist(tiempos_servicio, bins=10, edgecolor='black', alpha=0.7)
plt.title('Distribución de Tiempos de Servicio Simulados (Exponencial)')
plt.xlabel('Tiempo de servicio (minutos)')
plt.ylabel('Frecuencia')
plt.show()