import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Crear un DataFrame de ejemplo
data = {
    'Producto': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Ventas': [150, 200, 120, 300, 180, 250, 100, 220, 280, 170],
    'Region': ['Norte', 'Sur', 'Este', 'Oeste', 'Norte', 'Sur', 'Este', 'Oeste', 'Norte', 'Sur']
}
df = pd.DataFrame(data)

print("DataFrame original:")
print(df)
print("\n---\n")

# Ejercicio 1: Gráfico de barras de ventas por producto
plt.figure(figsize=(10, 6))
sns.barplot(x='Producto', y='Ventas', data=df)
plt.title('Ventas por Producto')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.grid(axis='y', linestyle='--')
plt.show()

# Ejercicio 2: Histograma de ventas
plt.figure(figsize=(8, 5))
sns.histplot(df['Ventas'], bins=5, kde=True)
plt.title('Distribución de Ventas')
plt.xlabel('Ventas')
plt.ylabel('Frecuencia')
plt.show()

# Ejercicio 3: Gráfico de pastel de ventas por región
ventas_por_region = df.groupby('Region')['Ventas'].sum()
plt.figure(figsize=(8, 8))
plt.pie(ventas_por_region, labels=ventas_por_region.index, autopct='%1.1f%%', startangle=140)
plt.title('Ventas por Región')
plt.axis('equal') # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Ejercicio 4: Diagrama de dispersión de Ventas vs. un índice ficticio
df['Indice_Satisfaccion'] = [7, 8, 6, 9, 7, 8, 6, 8, 9, 7] # Datos ficticios
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Indice_Satisfaccion', y='Ventas', data=df, hue='Region', s=100)
plt.title('Ventas vs. Índice de Satisfacción por Región')
plt.xlabel('Índice de Satisfacción')
plt.ylabel('Ventas')
plt.grid(True)
plt.show()


