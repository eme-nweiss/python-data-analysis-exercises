import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Ana', 'Luis', 'Marta', 'Pedro', 'Sofía'],
    'Edad': [24, 30, 28, 35, 22],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Madrid', 'Sevilla'],
    'Salario': [30000, 45000, 38000, 50000, 32000]
}
df = pd.DataFrame(data)

print("DataFrame original:")
print(df)
print("\n---\n")

# Ejercicio 1: Calcular el salario promedio
salario_promedio = df['Salario'].mean()
print(f"Salario promedio: {salario_promedio:.2f}\n")

# Ejercicio 2: Filtrar personas mayores de 25 años
personas_mayores_25 = df[df['Edad'] > 25]
print("Personas mayores de 25 años:")
print(personas_mayores_25)
print("\n---\n")

# Ejercicio 3: Contar ocurrencias por ciudad
conteo_ciudades = df['Ciudad'].value_counts()
print("Conteo de personas por ciudad:")
print(conteo_ciudades)
print("\n---\n")

# Ejercicio 4: Añadir una nueva columna 'Bonus'
df['Bonus'] = df['Salario'] * 0.10
print("DataFrame con columna 'Bonus':")
print(df)
print("\n---\n")

# Ejercicio 5: Ordenar el DataFrame por salario descendente
df_ordenado = df.sort_values(by='Salario', ascending=False)
print("DataFrame ordenado por salario (descendente):")
print(df_ordenado)


