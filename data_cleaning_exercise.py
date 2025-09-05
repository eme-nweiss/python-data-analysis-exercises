import pandas as pd
import numpy as np

# Crear un DataFrame de ejemplo con datos sucios
data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Valor': [10, 20, np.nan, 40, 50, 60, 70, np.nan, 90, 100],
    'Categoria': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C'],
    'Fecha': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06', '2023-01-07', '2023-01-08', '2023-01-09', '2023-01-10']
}
df = pd.DataFrame(data)

print("DataFrame original:")
print(df)
print("\n---\n")

# Ejercicio 1: Manejar valores nulos (reemplazar NaN con la media de la columna 'Valor')
df['Valor'].fillna(df['Valor'].mean(), inplace=True)
print("DataFrame después de manejar valores nulos en 'Valor':")
print(df)
print("\n---\n")

# Ejercicio 2: Eliminar filas con valores nulos (si hubiera en otras columnas)
df_cleaned = df.dropna()
print("DataFrame después de eliminar filas con valores nulos (si los hubiera):")
print(df_cleaned)
print("\n---\n")

# Ejercicio 3: Convertir la columna 'Fecha' a tipo datetime
df['Fecha'] = pd.to_datetime(df['Fecha'])
print("DataFrame con 'Fecha' convertida a datetime:")
print(df.info())
print("\n---\n")

# Ejercicio 4: Eliminar duplicados (crear un duplicado para demostrar)
df_with_duplicates = pd.concat([df, df.iloc[[0]]], ignore_index=True)
print("DataFrame con duplicados (para demostración):")
print(df_with_duplicates)
print("\n---\n")

df_no_duplicates = df_with_duplicates.drop_duplicates()
print("DataFrame después de eliminar duplicados:")
print(df_no_duplicates)


