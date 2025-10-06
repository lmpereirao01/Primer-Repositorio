"""
Escribe un programa que pida al usuario ingresar una frase o párrafo. 
Luego, el programa debe contar cuántas veces aparece cada palabra en el texto y 
mostrar las palabras junto con su frecuencia.

Requisitos:
Eliminar los signos de puntuación y convertir todas las palabras a minúsculas para evitar diferencias.
Usar un diccionario donde la clave sea la palabra y el valor sea su frecuencia.
Mostrar las palabras y sus frecuencias de forma ordenada por la palabra.
"""

text = input("Introduce una frase o párrafo:")

normalized_text = text.lower().replace(".","") # Delete all dots
words = normalized_text.split() 

print(words)