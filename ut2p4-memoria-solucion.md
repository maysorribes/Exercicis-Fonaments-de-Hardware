# Soluciones · UT2P4 Memoria

## Actividad 1 · Busca información

### 1. Uso de las diferentes memorias de la jerarquía de memorias en el PC

Las memorias se ordenan de más rápida, pequeña y cara a más lenta, grande y barata:

* **Registros:** dentro del procesador. Guardan los datos de la instrucción que se ejecuta en ese momento.
* **Caché (L1, L2, L3):** dentro del procesador. Guarda copias de los datos e instrucciones de la RAM que más se usan.
* **RAM:** memoria principal. Guarda el sistema operativo y los programas que se están ejecutando.
* **Almacenamiento (SSD/HDD):** guarda los datos de forma permanente.

### 2. Definición de RAM

La RAM (*Random Access Memory*) es la memoria principal del ordenador, donde se cargan los programas y los datos en uso. Es de **lectura y escritura**, de **acceso aleatorio** (se accede a cualquier posición directamente por su dirección) y **volátil** (pierde los datos al apagar el equipo).

### 3. Arquitectura y características de las RAM DDR5. Compáralas con DDR4

| | DDR4 | DDR5 |
|---|---|---|
| Velocidad | 1600–3200 MT/s | 4800–8800 MT/s |
| Tensión | 1,2 V | 1,1 V |
| Canales por módulo | 1 de 64 bits | 2 subcanales de 32 bits |
| Regulación de tensión | En la placa base | PMIC en el propio módulo |
| ECC en el chip | No | Sí (on-die) |
| Capacidad máx. por módulo | 32 GB | 128 GB |

* **Dos subcanales de 32 bits:** el controlador puede hacer dos accesos independientes a la vez, y así aprovecha mejor el bus.
* **PMIC:** el módulo convierte en el propio módulo la tensión que le llega de la placa. La tensión es más estable.
* **Latencias:** en ciclos son más altas, pero la latencia real en ns es parecida a la de DDR4. La ventaja de DDR5 está en el ancho de banda.

### 4. Diferencia entre RAM ECC y RAM no ECC

La **RAM ECC** tiene bits extra (8 por cada 64 de datos) que permiten **detectar y corregir errores** en los datos. La **no ECC** no detecta los errores. La ECC es más cara, necesita un procesador y una placa compatibles y se usa en servidores. La no ECC se usa en los PC domésticos.

### 5. Funcionamiento de la RAM ECC. ¿La ECC on-die de DDR5 equivale a una RAM ECC?

**Funcionamiento:** al escribir, el controlador calcula unos bits de control a partir de los datos y los guarda junto a ellos. Al leer, los vuelve a calcular y los compara con los guardados:

* Si coinciden, no hay error.
* Si falla 1 bit, sabe cuál es y lo corrige.
* Si fallan 2 bits, lo detecta, pero no lo puede corregir.

**No equivale.** La ECC on-die solo corrige errores **dentro del chip**. No protege los datos mientras viajan del módulo al procesador, y no avisa al sistema de los errores. La ECC real comprueba los datos en el controlador, de extremo a extremo.

### 6. Describe el procedimiento para obtener una palabra de memoria (8 bits)

La memoria está formada por **8 matrices de celdas** (una por cada bit de la palabra), organizadas en filas y columnas.

1. El procesador envía la **dirección** por el bus de direcciones.
2. La dirección se divide en **fila** y **columna**.
3. Se activa la **fila** (señal RAS) en las 8 matrices.
4. Se selecciona la **columna** (señal CAS) en las 8 matrices.
5. Cada matriz entrega 1 bit, y los 8 bits forman la palabra, que sale por el **bus de datos**.

### 7. Dibuja un ejemplo en digital de la matriz 3D y cómo obtener la palabra de memoria

Ejemplo: 8 planos de 4 × 4 celdas (16 palabras de 8 bits). La dirección tiene 4 bits: 2 para la fila y 2 para la columna.

Dirección `1001` → fila `10` (2), columna `01` (1):

```
         col:  0   1   2   3
             ┌───┬───┬───┬───┐
     fila 0  │   │   │   │   │
             ├───┼───┼───┼───┤
     fila 1  │   │   │   │   │       x 8 planos
             ├───┼───┼───┼───┤       (bit 0 ... bit 7)
  ►  fila 2  │   │ ■ │   │   │
             ├───┼───┼───┼───┤
     fila 3  │   │   │   │   │
             └───┴───┴───┴───┘

  Cada plano da el bit de la celda ■:

  Plano:   7  6  5  4  3  2  1  0
  Bit:     0  1  1  0  1  0  0  1   →  palabra 01101001
```

### 8. Si queremos que nuestras memorias sean las más rápidas, aparte de la frecuencia, ¿qué otros aspectos nos deben importar al elegirlas?

* **Latencia (CL):** son los ciclos que tarda la memoria en responder. Con la misma frecuencia, cuanto más baja sea la latencia, más rápido responde.
* **Dual channel:** con dos módulos en canales distintos se duplica el ancho de banda. Por eso 2 × 8 GB es mejor que 1 × 16 GB.
* **Capacidad:** si la RAM no llega, el sistema usa el disco como memoria virtual y el equipo va mucho más lento.
* **Compatibilidad:** la memoria tiene que ser compatible con la placa y el procesador. Si no lo es, funcionará a la velocidad más baja que soporten.
* **Perfil XMP/EXPO:** hay que activarlo en la BIOS para que la memoria funcione a la velocidad anunciada.

### 9. ¿Cuál es la relación entre el bus de datos y el bus de direcciones?

* El **bus de direcciones** indica **dónde** leer o escribir. Con *n* líneas hay 2ⁿ posiciones.
* El **bus de datos** lleva el **dato**. Su ancho es el tamaño de la palabra.

> Capacidad = 2ⁿ posiciones × tamaño de la palabra

**Ejemplo:** con un bus de direcciones de 4 bits y un bus de datos de 8 bits hay 2⁴ = 16 posiciones de 8 bits, es decir, 16 bytes.

### 10. Funcionamiento de la SRAM y la DRAM

* **SRAM:** cada bit se guarda en un **biestable** (6 transistores). **No necesita refresco**, es muy rápida y cara, y ocupa mucho espacio. Se usa en la **caché**.
* **DRAM:** cada bit se guarda como carga en un **condensador** (1 transistor + 1 condensador). El condensador pierde carga, así que **necesita refresco** periódico. Es más lenta, pero barata y densa. Se usa en la **memoria principal**.

### 11. Explica cómo se carga la memoria caché y qué operaciones se realizan entre la RAM y el procesador (acierto, fallo, escritura)

La caché se carga con **bloques (líneas)** de la RAM, no con datos sueltos. Así aprovecha que el procesador suele reutilizar los mismos datos y los que están cerca.

* **Acierto:** el dato está en la caché y se entrega al procesador rápidamente.
* **Fallo:** el dato no está. Se trae de la RAM el bloque que lo contiene, se guarda en la caché y se entrega al procesador.
* **Escritura:**
  * **Write-through:** se escribe a la vez en la caché y en la RAM.
  * **Write-back:** solo se escribe en la caché, y el bloque se copia a la RAM cuando se sustituye.

---

## Actividad 2 · Tabla de módulos

* **Frecuencia efectiva** = frecuencia del reloj × accesos por ciclo
* **Tasa de transferencia (MB/s)** = frecuencia efectiva × 8 bytes
* **Accesos por ciclo:** DDR = 2, DDR2 = 4, DDR3 y DDR4 = 8, DDR5 = 16

| Nombre del módulo | DDR - número | Frecuencia del reloj | Frecuencia efectiva | Accesos por ciclo | Tasa de transferencia | Tensión |
| --- | --- | --- | --- | --- | --- | --- |
| PC-1600 | DDR-200 | 100 MHz | 200 MHz | 2 | 1.600 MB/s | 2,5 V |
| PC-2700 | DDR-333 | 166 MHz | 333 MHz | 2 | 2.666 MB/s | 2,5 V |
| PC2-4800 | DDR2-600 | 150 MHz | 600 MHz | 4 | 4.800 MB/s | 1,8 V |
| PC4-21328 | DDR4-2666 | 333 MHz | 2.666 MHz | 8 | 21.328 MB/s | 1,2 V |
| PC3-12800 | DDR3-1600 | 200 MHz | 1.600 MHz | 8 | 12.800 MB/s | 1,5 V |
| PC4-17000 | DDR4-2133 | 266 MHz | 2.133 MHz | 8 | 17.064 MB/s | 1,2 V |
| PC2-6400 | DDR2-800 | 200 MHz | 800 MHz | 4 | 6.400 MB/s | 1,8 V |
| PC3-16000 | DDR3-2000 | 250 MHz | 2.000 MHz | 8 | 16.000 MB/s | 1,5 V |
| PC5-44800 | DDR5-5600 | 350 MHz | 5.600 MHz | 16 | 44.800 MB/s | 1,1 V |

---

## Actividad 3 · Clasificación de módulos

| Número | Tipo | Contactos | Tensión |
| --- | --- | --- | --- |
| 1 | DDR4 SO-DIMM (portátil) | 260 | 1,2 V |
| 2 | DDR2 SO-DIMM (portátil) | 200 | 1,8 V |
| 3 | DDR3 SO-DIMM (portátil) | 204 | 1,5 V |
| 4 | DDR2 DIMM (sobremesa) | 240 | 1,8 V |
| 5 | DDR3 DIMM con disipador (sobremesa) | 240 | 1,5 V |
| 6 | DDR4 RDIMM con ECC (servidor) | 288 | 1,2 V |

---

## Actividad 4 · Tecnologías de memoria

Cada alumno explica una. Esto es lo básico que debería aparecer:

* **HBM3E:** chips de DRAM apilados en vertical y colocados junto a la GPU. Da un ancho de banda enorme, pero es muy cara y no se puede ampliar. Se usa en GPU para IA y centros de datos.
* **GDDR7:** memoria de las tarjetas gráficas, sucesora de GDDR6. Transmite más datos por ciclo, así que da más ancho de banda. Es más cara. Se usa en las tarjetas gráficas actuales.
* **Intel Optane:** memoria no volátil (no pierde los datos al apagar) y mucho más rápida que un SSD normal. Era cara y tenía poca capacidad. Se dejó de fabricar en 2022 porque no era rentable.
* **Memorias 2D y 3D:** en las 2D las celdas están en un solo plano. En las 3D se apilan capas de celdas, y así cabe más capacidad en el mismo espacio y a menor precio. Toda la memoria de los SSD actuales es 3D.
* **CAMM2:** un módulo plano que se atornilla a la placa en vez de insertarse en una ranura. Es más fino y más rápido que un SO-DIMM y se puede cambiar. Se usa en portátiles.
* **LPCAMM2:** un CAMM2 con memoria de bajo consumo (LPDDR5X). Normalmente esa memoria va soldada a la placa; así se puede cambiar. Se usa en portátiles.
* **MRAM:** guarda el bit de forma magnética. Es no volátil, rápida y aguanta muchísimas escrituras, pero tiene poca capacidad y es cara. Se usa en sistemas industriales, coches y satélites.
* **UltraRAM:** memoria experimental de la Universidad de Lancaster. Pretende ser no volátil y tan rápida como la RAM, pero todavía está en investigación.
