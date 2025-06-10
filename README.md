# Algoritmos de Búsqueda y Ordenamiento en Python

Trabajo integrador realizado para la materia **Programación I**.  
Se implementaron y analizaron distintos algoritmos de ordenamiento y búsqueda sobre datos reales, con foco en la eficiencia y aplicabilidad práctica.

## 📌 Objetivos

- Estudiar el funcionamiento y rendimiento de algoritmos de ordenamiento y búsqueda.
- Comparar su eficiencia tanto teórica como práctica mediante pruebas sobre datos reales.
- Preparar la información para realizar búsquedas eficientes.

## 🧠 Algoritmos utilizados

### Ordenamiento
- Insertion Sort
- Selection Sort
- Quick Sort
- `sort()` (método interno de listas en Python)
- `sorted()` (función integrada de Python)

### Búsqueda
- Búsqueda Lineal
- Búsqueda Binaria

## 🗂️ Datos utilizados

Se trabajó con una lista de poblaciones de **331 ciudades argentinas**, extraída de [Argentina Cities Database](https://simplemaps.com/data/ar-cities) (SimpleMaps).

## ⚙️ Metodología

1. **Investigación teórica**: Estudio de algoritmos en materiales de cátedra y documentación adicional (W3Schools, ChatGPT).
2. **Implementación**: Se programaron los algoritmos en Python y se estructuraron para medir sus tiempos de ejecución.
3. **Pruebas**: Se evaluó el rendimiento sobre:
   - Lista completa (331 ciudades)
   - Lista acotada (Top 10 ciudades más pobladas)
   - Lista ordenada vs. desordenada (para búsquedas)
4. **Análisis de resultados**: Comparación de eficiencia y precisión en contexto práctico.

## 🧪 Resultados destacados

### Ordenamiento
- **sorted()** fue el más eficiente en ambos escenarios.
- **Selection Sort** fue el más lento en la lista completa (hasta **8868.75% más lento**, o **89.69 veces**).
- **Quick Sort** fue más lento en listas acotadas debido a su recursividad.

### Búsqueda
- La **búsqueda binaria** fue más rápida, pero solo válida en listas ordenadas.
- La **búsqueda lineal** fue correcta en todos los casos, aunque más lenta.

## 🧰 Herramientas utilizadas

- Python 3.11.9
- Visual Studio Code 1.100.3
- Biblioteca `time` para medición de tiempos
- Datos: Argentina Cities Database (SimpleMaps)
- ChatGPT (OpenAI) para asistencia conceptual, organización y mejora del código

## 👥 Integrantes del equipo

- **Iván Nievas Zorn**: Desarrollo y análisis de algoritmos de ordenamiento
- **Alexis Javier Pajón Fenoglio**: Desarrollo y análisis de algoritmos de búsqueda
- Ambos colaboraron en la redacción del informe y las conclusiones

## 📚 Bibliografía

- W3Schools. (n.d.). *Python sort() method*. https://www.w3schools.com/python/ref_list_sort.asp  
- W3Schools. (n.d.). *Python sorted() function*. https://www.w3schools.com/python/ref_func_sorted.asp  
- SimpleMaps. (2024). *Argentina Cities Database*. https://simplemaps.com/data/ar-cities (Licencia: MIT)  
- OpenAI. (2025). *ChatGPT (versión GPT-4)*. https://openai.com/chatgpt  

> ChatGPT fue utilizado para organizar ideas, redactar contenidos técnicos, sugerir mejoras en la implementación y asistir en el análisis de resultados.
>
## 🔗 Enlace al video

> https://youtu.be/jUVyHmFiofc
