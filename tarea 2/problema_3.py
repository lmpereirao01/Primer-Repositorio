# Escribe un programa que permita al usuario crear dos conjuntos de números
# enteros. Luego, el programa debe calcular y mostrar:
# 1. La intersección de ambos conjuntos (elementos comunes).
# 2. La unión de ambos conjuntos (todos los elementos sin duplicados).
# 3. La diferencia simétrica (elementos que están en uno u otro conjunto,
# pero no en ambos).

conjunto1=input("Introduce un conjunto de números separados por comas: ")
conjunto2=input("Introduce otro conjunto de números separados por comas: ")

set1 = set(map(int, conjunto1.replace(" ", "").split(",")))
set2 = set(map(int, conjunto2.replace(" ", "").split(",")))

intersection = set1.intersection(set2)       # set1 & set2
union = set1.union(set2)                     # set1 | set2
difference = set1.symmetric_difference(set2) # set1 ^ set2

print("\nResultados:")
print("Intersección:", sorted(intersection))
print("Unión:", sorted(union))
print("Diferencia simétrica:", sorted(difference))