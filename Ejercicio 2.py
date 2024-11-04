import numpy as np
import matplotlib.pyplot as plt

# Parámetro de la distribución exponencial (tasa de inactividad)
lambda_inactividad = 1 / 10  # Tiempo promedio de inactividad = 10 minutos

# Función para generar un tiempo de inactividad
def generar_tiempo_inactividad(lambda_inactividad):
    u = np.random.uniform(0, 1)  # Generar número aleatorio uniforme
    # Aplicar transformada inversa
    tiempo_inactividad = -1 / lambda_inactividad * np.log(1 - u)  
    return tiempo_inactividad

# Generar 100 tiempos de inactividad
tiempos_inactividad = [generar_tiempo_inactividad(lambda_inactividad) 
                       for _ in range(100)]

# Mostrar los tiempos de inactividad generados
print("Tiempos de inactividad generados:", tiempos_inactividad)

# Graficar los tiempos de inactividad simulados
plt.hist(tiempos_inactividad, bins=10, edgecolor='black', alpha=0.7)
plt.title('Distribución de Tiempos de Inactividad Simulados (Exponencial)')
plt.xlabel('Tiempo de inactividad (minutos)')
plt.ylabel('Frecuencia')
plt.show()