# 🧠Backend Developer - Technical Test

Este proyecto contiene la solución a una prueba técnica para evaluar conocimientos de lógica, programación en Python y buenas prácticas de codificación, siguiendo la guía de estilo PEP8.

---

## 📁 Estructura del proyecto

.
├── sorting_filter/
│   └── sorting_filter.py            # Ejercicio 2: ordenar elementos por criterios sin usar sort()
├── word_counter/
│   └── word_counter.py              # Ejercicio 1: contar ocurrencias de una palabra sin usar funciones nativas
└── README.md              

## 📝   Ejercicio 1 - Contador de ocurrencias de una palabra

Objetivo: Contar cuántas veces aparece una palabra en un párrafo, sin utilizar funciones nativas como in, count, split, find, etc.

Cómo ejecutar:

```bash
python word_counter/word_counter.py
```
Resultado esperado:

```bash
La palabra 'logística' aparece 4 veces.
La palabra 'python' aparece 3 veces.
```

## 📝 Ejercicio 2 - Ordenar elementos por criterios

Objetivo: Ordenar un arreglo de diccionarios por el campo priority (descendente), solo para los elementos que cumplen ciertos criterios sobre campos como width, height, length, y weight. No se debe usar sort().

Cómo ejecutar:

```bash
python sorting_filter/sorting_filter.py
```

Resultado esperado:

Primero los elementos que cumplen los criterios (ordenados por priority)

Luego el resto de los elementos sin modificar su orden original

## ⚙️ Requisitos

Python 3.6 o superior

No se usan paquetes externos