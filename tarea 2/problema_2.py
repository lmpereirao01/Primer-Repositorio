"""
Escribe un programa que pida al usuario ingresar una frase o párrafo. 
Luego, el programa debe contar cuántas veces aparece cada palabra en el texto y 
mostrar las palabras junto con su frecuencia.

Requisitos:
Eliminar los signos de puntuación y convertir todas las palabras a minúsculas para evitar diferencias.
Usar un diccionario donde la clave sea la palabra y el valor sea su frecuencia.
Mostrar las palabras y sus frecuencias de forma ordenada por la palabra.
"""
import string

text = input("Introduce una frase o párrafo:")

text = text.lower()
for punct in string.punctuation:
    text = text.replace(punct, "")

words = text.split()
dictionary = {}

for n in words:
    if n in dictionary:
        dictionary[n]+=1
    else:
        dictionary[n]=1
    
for word in sorted(dictionary):
    print(f"{word}: {dictionary[word]}")