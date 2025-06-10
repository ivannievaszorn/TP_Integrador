# Este script compara el rendimiento de distintos algoritmos de ordenamiento
# sobre una lista grande y otra reducida de poblaciones argentinas.

import random
import timeit

print("="*60)
print("Comparación de Algoritmos de Ordenamiento en Python".center(60))
print("="*60)

# Lista mezclada de poblaciones de las 331 ciudades mas pobladas de Argentina
poblaciones_arg = [
    21624, 730266, 24307, 15741, 39601, 37745, 58315, 82227, 296826, 7983, 121451, 6351, 
    22924, 43251, 47839, 85060, 49132, 3812, 63284, 79476, 352646, 115353, 64556, 48140, 
    180995, 28537, 26651, 405683, 99066, 43287, 34421, 11428, 17491, 46421, 8946, 7902, 
    19142, 4570, 30903, 27000, 57244, 106899, 231198, 42276, 109461, 81465, 244168, 25757, 
    33607, 291720, 11785, 31901, 64867, 160954, 247863, 13689, 47622, 5465, 12029, 157532, 
    52529, 85189, 43009, 58430, 26221, 50426, 9294, 12537, 163240, 2106734, 65859, 106441, 
    8260, 18349, 169947, 15394, 32097, 57669, 32116, 16710000, 41705, 903, 40259, 400, 
    29205, 15126, 301572, 55728, 10873, 32646, 54698, 91322, 26497, 46239, 12801, 50183, 
    120346, 38000, 5547, 12621, 30680, 44796, 41109, 160000, 11562, 10067, 12799, 92945, 
    57323, 7591, 47348, 159139, 62315, 45848, 31602, 75315, 9012, 7772, 25705, 14692, 54081, 
    73058, 32027, 215020, 56419, 90000, 223898, 98859, 41403, 56956, 48158, 7110, 23408, 
    275988, 104985, 43595, 3317, 107786, 95785, 160219, 80769, 72304, 87258, 200000, 29854, 
    190696, 35307, 47374, 27004, 10885, 147965, 98017, 24747, 10902, 321789, 35465, 46642, 
    100324, 31553, 481, 66112, 262379, 191299, 59031, 29593, 471389, 47626, 75616, 11101, 
    31892, 76070, 107778, 6084, 21997, 89882, 60867, 38470, 11589, 459263, 216637, 28051, 
    41463, 54678, 112580, 35301, 44529, 6916, 54463, 65881, 50057, 19877, 63226, 106662, 
    6320, 149450, 23150, 16874, 88470, 23171, 9244, 52837, 22953, 47569, 25520, 25940, 136604, 
    82582, 10470, 85315, 58152, 24616, 29218, 112887, 42082, 27956, 605767, 535303, 238067, 
    100728, 57458, 41390, 85420, 62001, 30100, 11316, 23299, 12733, 41155, 31758, 4569, 
    7652, 65684, 9763, 32083, 18089, 88600, 36994, 21333, 89721, 49782, 2064, 180523, 682605, 
    32097, 72000, 92957, 26448, 22046, 60000, 21125, 57878, 10889, 95796, 39507, 73293, 
    30028, 21592, 86860, 37775, 25140, 18115, 15347, 102880, 33724, 17634, 35058, 115041, 
    46019, 28750, 2139, 28814, 63196, 135275, 64640, 6249, 82582, 28339, 234000, 10743, 3973, 
    73155, 43168, 33222, 13462, 35844, 36494, 25404, 13245, 911506, 109914, 109644, 4429, 
    13516, 31190, 10319, 51448, 58811, 23470, 71479, 21088, 78699, 94403, 5534, 193144, 41176, 
    39151, 23274, 97915, 59335, 22824, 38418, 1276000, 49445, 16658, 79557, 23027, 111391, 
    146704, 98522, 32390, 62000, 33835, 28265, 8351, 11672, 40858, 30666, 189067, 32227, 971, 
    60752
]

total_ciudades = len(poblaciones_arg)
print(f"La lista sin ordenar tiene las poblaciones de un total de {total_ciudades} ciudades")

# Ordenamos inversamente la lista poblaciones_arg para tomar las 10 poblaciones mas altas.
poblaciones_arg_top10 = sorted(poblaciones_arg, reverse=True)[:10]

# Algoritmos
# Funcion Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Funcion selection sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Funcion Quicksort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
# Funciones sort()
def usar_sort(lista):
    lista.sort()
    return lista

# Funcion sorted()
def usar_sorted(lista):
    return sorted(lista)

# Función para medir tiempo de ejecución
def medir_tiempo(func, lista):
    inicio = timeit.default_timer()
    func(lista.copy())
    fin = timeit.default_timer()
    return fin - inicio

def mostrar_resultado(nombre_lista, mejor, peor, tiempos):
    print(f"\nEn {nombre_lista}:")
    print(f"✅ El más rápido fue: {mejor} con {tiempos[mejor]:.6f} segundos")
    print(f"❌ El más lento fue: {peor} con {tiempos[peor]:.6f} segundos")

# Crear un diccionario vacío para guardar los tiempos
tiempos_lista_completa = {}
tiempos_lista_top10 = {}

# Diccionario unificado de algoritmos con nombres consistentes
algoritmos = {
    "Insertion Sort": insertion_sort,
    "Selection Sort": selection_sort,
    "Quick Sort": quicksort,
    "sort()": usar_sort,
    "sorted()": usar_sorted
}

for metodo, funcion in algoritmos.items():
    tiempos_lista_completa[f"{metodo}"] = medir_tiempo(funcion, poblaciones_arg)
    tiempos_lista_top10[f"{metodo}"] = medir_tiempo(funcion, poblaciones_arg_top10)

# Mostrar resultados ordenados. # Ordenamos las claves del diccionario "tiempos", utilizando el valor asociado a cada clave (tiempo) key=tiempos.get, de menor a mayor.
print("\n" + "-"*60)
print(f"Tiempos para Lista Completa ({total_ciudades} ciudades)".center(60))
print("-"*60)
for metodo in sorted(tiempos_lista_completa, key=tiempos_lista_completa.get):
    print(f"{metodo:15}: {tiempos_lista_completa[metodo]:.6f} segundos") #":15" deja 25 espacios reservados para alinear los nombres a la izquierda. ".6f" muestra resultado con 6 decimales.

print("\n" + "-"*60)
print("Tiempos para Lista Top 10 Ciudades".center(60))
print("-"*60)
for metodo in sorted(tiempos_lista_top10, key=tiempos_lista_top10.get):
    print(f"{metodo:15}: {tiempos_lista_top10[metodo]:.6f} segundos") #":15" deja 25 espacios reservados para alinear los nombres a la izquierda. ".6f" muestra resultado con 6 decimales.

# Buscar el algoritmo más rápido y más lento para la lista completa de ciudades. 
# # key=tiempos.get le dice a min() o max() que, en lugar de comparar los nombres, compare los valores del diccionario.
mejor_lista_completa = min(tiempos_lista_completa, key=tiempos_lista_completa.get)
peor_lista_completa = max(tiempos_lista_completa, key=tiempos_lista_completa.get)
# Buscar el algoritmo más rápido y más lento para la lista reducida (10 ciudades más pobladas)
mejor_lista_top10 = min(tiempos_lista_top10, key=tiempos_lista_top10.get)
peor_lista_top10 = max(tiempos_lista_top10, key=tiempos_lista_top10.get)

print("\n" + "="*60)
print("Conclusiones".center(60))
print("="*60)
mostrar_resultado(f"Lista Completa ({total_ciudades} ciudades)", mejor_lista_completa, peor_lista_completa, tiempos_lista_completa)
mostrar_resultado("Lista Top 10 Ciudades", mejor_lista_top10, peor_lista_top10, tiempos_lista_top10)

# Preparamos la lista ordenada con el mejor algoritmo para que sea utilizada en la funcion de busqueda
lista_ordenada_para_busqueda = algoritmos[mejor_lista_completa](poblaciones_arg)
print(f"\nTarea de ordenamiento finalizada")
print(f"\nLa lista ordenada fue creada correctamente utilizando {mejor_lista_completa} para su posterior utilización en funciones de busqueda")

# Función búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Función búsqueda binaria 
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return -1

def medir_tiempo_busqueda(func, lista, objetivo):
    inicio = timeit.default_timer()
    resultado = func(lista, objetivo)
    fin = timeit.default_timer()
    return resultado, fin - inicio

print("\n")
print("="*60)
print("Comparación de Algoritmos de Búsqueda en Python".center(60))
print("="*60)

objetivo = 275988
print(f"\nEl objetivo es: {objetivo}")

busquedas = {
    "Búsqueda Lineal": busqueda_lineal,
    "Búsqueda Binaria": busqueda_binaria
}

# Diccionarios para guardar tiempos e índices
indices_busqueda_desordenada = {}
tiempos_busqueda_desordenada = {}
indices_busqueda_ordenada = {}
tiempos_busqueda_ordenada = {}

for nombre, funcion in busquedas.items():
    indice, tiempo = medir_tiempo_busqueda(funcion, poblaciones_arg, objetivo)
    tiempos_busqueda_desordenada[nombre] = tiempo
    indices_busqueda_desordenada[nombre] = indice

for nombre, funcion in busquedas.items():
    indice, tiempo = medir_tiempo_busqueda(funcion, lista_ordenada_para_busqueda, objetivo)
    tiempos_busqueda_ordenada[nombre] = tiempo
    indices_busqueda_ordenada[nombre] = indice

print("\n" + "-"*60)
print("Tiempos de Búsqueda en Lista Desordenada".center(60))
print("-"*60)
for metodo in sorted(tiempos_busqueda_desordenada, key=tiempos_busqueda_desordenada.get):
    tiempo = tiempos_busqueda_desordenada[metodo]
    indice = indices_busqueda_desordenada[metodo]
    print(f"{metodo:20}: índice = {indice:5}, tiempo = {tiempo:.6f} segundos")

print("\n" + "-"*60)
print("Tiempos de Búsqueda en Lista Ordenada".center(60))
print("-"*60)
for metodo in sorted(tiempos_busqueda_ordenada, key=tiempos_busqueda_ordenada.get):
    tiempo = tiempos_busqueda_ordenada[metodo]
    indice = indices_busqueda_ordenada[metodo]
    print(f"{metodo:20}: índice = {indice:5}, tiempo = {tiempo:.6f} segundos")

mejor_des = min(tiempos_busqueda_desordenada, key=tiempos_busqueda_desordenada.get)
peor_des = max(tiempos_busqueda_desordenada, key=tiempos_busqueda_desordenada.get)
mejor_ord = min(tiempos_busqueda_ordenada, key=tiempos_busqueda_ordenada.get)
peor_ord = max(tiempos_busqueda_ordenada, key=tiempos_busqueda_ordenada.get)

print("\n" + "="*60)
print("Conclusiones de Búsqueda".center(60))
print("="*60)
mostrar_resultado("Lista Desordenada", mejor_des, peor_des, tiempos_busqueda_desordenada)
mostrar_resultado("Lista Ordenada", mejor_ord, peor_ord, tiempos_busqueda_ordenada)