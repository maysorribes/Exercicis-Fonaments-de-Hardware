[← Volver al índice](README.md)

# Sistemas Numéricos — Solución

Solución de la práctica sobre representación de números en distintas bases (binario, octal, decimal, hexadecimal), complemento a 2, codificación de caracteres, imágenes, audio y punto flotante IEEE 754.

## Índice

1. [Binario a decimal](#ejercicio-1--binario-a-decimal)
2. [Decimal a binario](#ejercicio-2--decimal-a-binario)
3. [Octal ↔ decimal](#ejercicio-3--octal--decimal)
4. [Hexadecimal ↔ decimal](#ejercicio-4--hexadecimal--decimal)
5. [Binario → octal y hexadecimal directos](#ejercicio-5--binario--octal-y-hexadecimal-directos)
6. [Sumas en binario](#ejercicio-6--sumas-en-binario)
7. [Colores hexadecimales en diseño web](#ejercicio-7--colores-hexadecimales-en-diseño-web)
8. [Tabla de conversión 16-20](#ejercicio-8--tabla-de-conversión-16-a-20)
9. [Complemento a 2](#ejercicio-9---18-en-complemento-a-2-8-bits)
10. [Signo y magnitud vs. complemento a 2](#ejercicio-10--problema-del-doble-cero)
11. [ASCII vs Unicode](#ejercicio-11--ascii-vs-unicode)
12. [Colores con 16 bits/píxel](#ejercicio-12--colores-con-16-bitspíxel)
13. [Frecuencia de muestreo](#ejercicio-13--frecuencia-de-muestreo)
14. [IEEE 754 (32 bits)](#ejercicio-14--5,25-en-ieee-754-32-bits)

---

## Ejercicio 1 — Binario a decimal

| Binario | Cálculo | Decimal |
|---|---|---|
| 1101₂ | 1·8 + 1·4 + 0·2 + 1·1 | **13** |
| 100110₂ | 1·32 + 0·16 + 0·8 + 1·4 + 1·2 + 0·1 | **38** |
| 11111₂ | 16+8+4+2+1 | **31** |

## Ejercicio 2 — Decimal a binario

| Decimal | Binario |
|---|---|
| 25 = 16+8+1 | **11001₂** |
| 100 = 64+32+4 | **1100100₂** |
| 17 = 16+1 | **10001₂** |

## Ejercicio 3 — Octal ↔ decimal

**345₈ → decimal:** 3·64 + 4·8 + 5·1 = 192+32+5 = **229**

**200₁₀ → octal:** divisiones sucesivas entre 8

```
200 ÷ 8 = 25  resto 0
 25 ÷ 8 =  3  resto 1
  3 ÷ 8 =  0  resto 3
```

Leyendo restos de abajo a arriba: **310₈** (comprobación: 3·64+1·8+0 = 200 ✓)

## Ejercicio 4 — Hexadecimal ↔ decimal

**1A3₁₆ → decimal:** 1·256 + 10·16 + 3 = 256+160+3 = **419**

**500₁₀ → hexadecimal:**

```
500 ÷ 16 = 31  resto 4
 31 ÷ 16 =  1  resto 15 (F)
  1 ÷ 16 =  0  resto 1
```

**1F4₁₆** (comprobación: 256+240+4 = 500 ✓)

## Ejercicio 5 — Binario → octal y hexadecimal directos

`111010110₂`

**A octal** (agrupando de 3 en 3 desde la derecha):

`111 / 010 / 110` → `7 2 6` → **726₈**

**A hexadecimal** (agrupando de 4 en 4 desde la derecha, rellenando con ceros):

`0001 / 1101 / 0110` → `1 D 6` → **1D6₁₆**

*(Comprobación en decimal: 470 en los tres casos)*

## Ejercicio 6 — Sumas en binario

**1101₂ + 1011₂**

```
  1101
+ 1011
-------
 11000
```
13 + 11 = 24 → 11000₂ = 16+8 = 24 ✓

**10010₂ + 00111₂**

```
  10010
+ 00111
--------
  11001
```
18 + 7 = 25 → 11001₂ = 16+8+1 = 25 ✓

## Ejercicio 7 — Colores hexadecimales en diseño web

Color: `#A3C1E8`

Cada componente (R, G, B) se escribe con **2 dígitos hexadecimales**, y como cada dígito hex equivale a 4 bits, cada componente ocupa **8 bits** (rango 00–FF, 0–255). En total el color usa 24 bits (3×8).

Se usa hexadecimal porque hay correspondencia exacta entre 1 dígito hex y 4 bits (un "nibble"), de modo que un byte completo se representa con solo 2 caracteres: más compacto que el binario (24 dígitos) y más fácil de convertir a/desde binario que el decimal.

## Ejercicio 8 — Tabla de conversión 16 a 20

| Decimal | Binario | Octal | Hexadecimal |
|---|---|---|---|
| 16 | 10000 | 20 | 10 |
| 17 | 10001 | 21 | 11 |
| 18 | 10010 | 22 | 12 |
| 19 | 10011 | 23 | 13 |
| 20 | 10100 | 24 | 14 |

## Ejercicio 9 — −18 en complemento a 2 (8 bits)

1. 18 en binario (8 bits): `00010010`
2. Invertir bits: `11101101`
3. Sumar 1: **`11101110`**

Comprobación: invirtiendo `11101110` → `00010001`, +1 → `00010010` = 18 ✓

## Ejercicio 10 — Problema del doble cero

En **signo y magnitud**, el bit más significativo indica solo el signo, y el resto la magnitud. Esto permite dos representaciones de cero: **+0** (`00000000`) y **−0** (`10000000`), bit a bit distintas pero con el mismo valor. Complica los circuitos aritméticos y las comparaciones.

El **complemento a 2** lo resuelve: el cero solo tiene una representación (`00000000`). Al negar un número se invierten los bits y se suma 1; aplicado a 0 se obtiene de nuevo `00000000` (el acarreo extra se descarta). Además simplifica la suma/resta, ya que se puede usar el mismo circuito sumador para positivos y negativos.

## Ejercicio 11 — ASCII vs Unicode

**ASCII**: usa 7 bits (128 combinaciones), cubre solo el alfabeto inglés, dígitos, puntuación básica y caracteres de control. No representa acentos, alfabetos no latinos (cirílico, árabe, chino...) ni emojis.

**Unicode**: creado para representar todos los sistemas de escritura del mundo en un único estándar, asignando un punto de código a cada carácter (más de 149.000). Se implementa con codificaciones de longitud variable como UTF-8, UTF-16 o UTF-32; UTF-8 mantiene compatibilidad con los primeros 128 caracteres ASCII.

## Ejercicio 12 — Colores con 16 bits/píxel

2¹⁶ = **65 536 colores distintos** como máximo.

## Ejercicio 13 — Frecuencia de muestreo

La **frecuencia de muestreo** es el número de veces por segundo que se mide una señal analógica continua para convertirla en valores digitales (se mide en Hz).

El CD de audio usa **44 100 Hz** por el **teorema de Nyquist-Shannon**: hay que muestrear al menos al doble de la frecuencia máxima contenida. El oído humano llega a ~20 kHz, por lo que se necesitan al menos 40 000 Hz; se eligieron 44 100 Hz para dejar margen de filtrado (evitar *aliasing*) y por compatibilidad histórica con los equipos de vídeo usados para grabar audio digital.

## Ejercicio 14 — 5,25 en IEEE 754 (32 bits)

**Paso 1 — Parte entera y decimal a binario**
- 5 = `101₂`
- 0,25 = `0,01₂`
- 5,25 = `101,01₂`

**Paso 2 — Normalizar** (forma 1,xxxx × 2ⁿ)

`101,01₂` = `1,0101 × 2²`

**Paso 3 — Signo**: número positivo → bit de signo = **0**

**Paso 4 — Exponente con sesgo (bias = 127)**

Exponente real = 2 → 2 + 127 = 129 = `10000001₂`

**Paso 5 — Mantisa (23 bits)**

De `1,0101` → `01010000000000000000000`

**Resultado final (32 bits):**

```
0 10000001 01010000000000000000000
signo  exponente(8)      mantisa(23)
```

---

[← Volver al índice](README.md)
