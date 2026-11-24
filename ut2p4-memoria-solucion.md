# Soluciones · UT2P4 Memoria

Fundamentos de Hardware · CFGS ASIR (1.º curso)

> En la Actividad 4 cada alumno elige una tecnología. Para cada una se dan los puntos clave que debería contener la explicación.
>
> Criterio de la asignatura para la tabla de la Actividad 2: la **frecuencia del reloj** es la frecuencia interna de las celdas, y los **accesos por ciclo** coinciden con el *prefetch* (DDR = 2, DDR2 = 4, DDR3 y DDR4 = 8, DDR5 = 16).

---

## Actividad 1 · Busca información

### 1. Uso de las diferentes memorias de la jerarquía de memoria en el PC

Cuanto más arriba en la pirámide, más rápida, más cara y de menor capacidad es la memoria. Cuanto más abajo, más lenta, más barata y de mayor capacidad.

| Nivel | Dónde está | Tamaño típico | Tiempo de acceso | Para qué se usa |
| --- | --- | --- | --- | --- |
| Registros | Dentro de cada núcleo de la CPU | Bytes (decenas de registros) | < 1 ns (1 ciclo) | Operandos y resultados de la instrucción que se está ejecutando |
| Caché L1 | Dentro de cada núcleo (separada en instrucciones y datos) | 32–64 KB por núcleo | ≈ 1 ns | Datos e instrucciones que se van a usar inmediatamente |
| Caché L2 | Dentro de cada núcleo | 1–3 MB por núcleo | ≈ 3–5 ns | Lo que no cabe en L1 |
| Caché L3 | Compartida entre núcleos | Decenas de MB | ≈ 10–20 ns | Datos compartidos entre núcleos; último paso antes de la RAM |
| Memoria principal (DRAM) | Módulos en la placa | GB | ≈ 60–100 ns | Sistema operativo, programas en ejecución y sus datos |
| Almacenamiento secundario interno | SSD / HDD, ROM-BIOS | GB–TB | µs (SSD) – ms (HDD) | Guardar datos y programas de forma permanente |
| Almacenamiento secundario externo | USB, discos externos, ópticos | GB–TB | ms | Copias, transporte de datos |
| Almacenamiento en red | NAS, SAN, nube | TB–PB | ms o más | Datos compartidos, copias de seguridad |

Funciona gracias al **principio de localidad**: un programa suele volver a usar los mismos datos (localidad temporal) y los que están al lado (localidad espacial). Por eso basta con tener una copia pequeña de lo más usado en las memorias rápidas.

### 2. Definición de RAM

La **RAM** (*Random Access Memory*, memoria de acceso aleatorio) es la memoria principal del ordenador:

- De **lectura y escritura**.
- **Volátil**: pierde el contenido al quitar la alimentación.
- De **acceso aleatorio**: se puede leer cualquier posición directamente con su dirección y el tiempo de acceso no depende de dónde esté el dato (a diferencia de una cinta o un disco mecánico).

Guarda el sistema operativo, los programas en ejecución y sus datos, para que la CPU trabaje con ellos mucho más rápido que si los leyera del disco.

### 3. Arquitectura y características de la DDR5 (comparada con DDR4)

| Característica | DDR4 | DDR5 |
| --- | --- | --- |
| Tensión | 1,2 V | **1,1 V** |
| Contactos (DIMM / SO-DIMM) | 288 / 260 | 288 / 262 (muesca en otra posición: no son compatibles) |
| Regulación de tensión | En la placa base | **En el propio módulo (PMIC)** |
| Canales por módulo | 1 canal de 64 bits | **2 subcanales independientes de 32 bits** (40 bits con ECC) |
| *Burst length* | BL8 | **BL16** |
| *Prefetch* | 8n | **16n** |
| Bancos | 16 (4 grupos) | **32 (8 grupos)** |
| Velocidades JEDEC | 1600–3200 MT/s | **4800–8800 MT/s** |
| Capacidad por chip | Hasta 16 Gb | **Hasta 64 Gb** (módulos de hasta 128 GB) |
| ECC | Solo en módulos ECC | **ECC integrada en el chip (on-die)** en todos los módulos, además de los módulos ECC |

Ideas clave:

- **Dos subcanales de 32 bits por módulo**: el controlador puede hacer dos accesos independientes a la vez. Así se aprovecha mejor el bus cuando hay muchas peticiones pequeñas (varios núcleos trabajando).
- El **PMIC** convierte en el propio módulo los 5 V que llegan de la placa. Así la tensión es más estable y la placa se simplifica, pero el módulo es algo más caro.
- Las **latencias en ciclos** son más altas (por ejemplo, CL40 a 4800 MT/s), pero como el ciclo es más corto, la **latencia real en ns es parecida** a la de DDR4. La ventaja está en el **ancho de banda**.
- A partir de 6400 MT/s aparecen los módulos **CUDIMM**, con un chip que regenera la señal de reloj (CKD) para alcanzar más velocidad de forma estable.

### 4. Diferencia entre RAM ECC y RAM no ECC

| | RAM no ECC | RAM ECC |
| --- | --- | --- |
| Bits por acceso | 64 | **72** (64 datos + 8 de control) |
| Chips | Múltiplos de 8 (8 por cara/rango) | Un chip más por cada 8 (9, 18…) |
| Errores | No los detecta | **Corrige errores de 1 bit y detecta los de 2 bits** |
| Rendimiento | Algo más rápida | Ligeramente más lenta (≈ 1–2 %) por el cálculo |
| Precio | Más barata | Más cara |
| Soporte | Cualquier placa | Necesita **CPU y placa** compatibles (servidores, estaciones de trabajo, algunos Ryzen) |
| Uso | Equipos domésticos y de oficina | Servidores, estaciones de trabajo, equipos que no pueden fallar |

Los errores de memoria pueden venir de radiación cósmica, interferencias o celdas degradadas. En un servidor encendido 24/7 con cientos de GB son relativamente frecuentes. Por eso allí la ECC es obligatoria.

> No hay que confundir ECC con *registered* (RDIMM): la RDIMM añade un chip (*buffer*/registro) que reduce la carga eléctrica sobre el controlador para poder poner muchos módulos. Casi todas las RDIMM son ECC, pero también existen módulos ECC sin registro (ECC UDIMM).

### 5. Funcionamiento de la RAM ECC y ECC *on-die* de DDR5

**Funcionamiento** (código de Hamming SECDED):

1. **Al escribir**, el controlador de memoria calcula 8 bits de control a partir de los 64 bits de datos. Cada bit de control es la paridad de un grupo distinto de bits de datos. Se guardan los 72 bits.
2. **Al leer**, vuelve a calcular los bits de control con los datos leídos y los compara con los guardados. El resultado de la comparación se llama **síndrome**.
3. Si el síndrome es **0**, no hay error.
4. Si indica **una posición**, hay un error de 1 bit: el controlador sabe qué bit es, lo invierte y entrega el dato corregido. Además, lo anota en el registro de errores del sistema.
5. Si detecta **2 bits erróneos**, no puede corregirlos, pero lo avisa (*machine check*). Normalmente el sistema se detiene antes de trabajar con datos corruptos.

**¿La ECC *on-die* de DDR5 equivale a una RAM ECC? No.**

- La ECC *on-die* trabaja **dentro de cada chip**. Corrige errores de las propias celdas, que son cada vez más frecuentes por la densidad de los chips DDR5. Es una forma de que el fabricante consiga chips fiables.
- **No protege el camino entre el módulo y la CPU** (el bus) y **no informa** al sistema de los errores que corrige.
- Una **DDR5 ECC de verdad** tiene 80 bits por módulo (2 subcanales × 40 bits). El controlador de memoria de la CPU es el que comprueba los datos de extremo a extremo.

### 6. Procedimiento para obtener una palabra de memoria (palabra de 8 bits)

Las celdas de la DRAM están organizadas en **matrices de filas y columnas**. Para una palabra de 8 bits hay **8 matrices** (una por bit) que reciben la misma dirección.

1. La CPU pone la **dirección** en el bus de direcciones y la señal de **lectura** en el bus de control.
2. El controlador de memoria divide la dirección en **fila** y **columna**.
3. **Activación de fila (RAS)**: se envía la dirección de fila. Toda esa fila se copia a los **amplificadores de lectura** (*sense amplifiers*), que detectan la pequeña carga de cada condensador.
4. Tras el tiempo **tRCD**, se envía la **dirección de columna (CAS)**. De la fila abierta se selecciona la columna pedida, en las 8 matrices a la vez.
5. Tras la **latencia CAS (CL)**, los 8 bits (uno de cada matriz) salen juntos al **bus de datos**: esa es la palabra.
6. Como la lectura de una DRAM es destructiva, los amplificadores **reescriben** la fila. Después se **cierra la fila** (*precharge*, tRP) para poder abrir otra.

### 7. Ejemplo de la matriz 3D

Ejemplo: memoria de **16 palabras de 8 bits** → 8 planos de 4 × 4 celdas. La dirección tiene 4 bits: 2 para la fila y 2 para la columna.

```
Dirección pedida: 1011  →  fila 10 (2)  ·  columna 11 (3)

           col 0  col 1  col 2  col 3
fila 0   [  .      .      .      .  ]
fila 1   [  .      .      .      .  ]      plano bit 7
fila 2   [  .      .      .      X  ]  ─┐  plano bit 6
fila 3   [  .      .      .      .  ]   │  ...
                                        │  plano bit 0
   (los 8 planos están apilados:       │
    la misma celda (2,3) de cada plano  └─► bits b7 b6 b5 b4 b3 b2 b1 b0
    da un bit de la palabra)                = palabra de 8 bits → bus de datos
```

Lo que debe verse en el dibujo: los **8 planos apilados**, la **fila y la columna seleccionadas** en todos ellos, y los **8 bits saliendo a la vez** hacia el bus de datos.

### 8. Aspectos, además de la frecuencia, para que la memoria sea rápida

- **Latencias (timings)**: CL (latencia CAS), tRCD, tRP y tRAS, en ciclos de reloj. A igual frecuencia, cuanto más bajos, mejor. Lo que importa es la **latencia real en ns** = CL × 2.000 ÷ MT/s.
  - DDR4-3200 CL16 → 16 × 2.000 ÷ 3.200 = **10 ns**
  - DDR5-6000 CL30 → 30 × 2.000 ÷ 6.000 = **10 ns** (misma latencia, pero casi el doble de ancho de banda)
- **Canales**: usar **dual channel** (dos módulos iguales en las ranuras correctas) duplica el ancho de banda. En servidores hay 4, 8 o 12 canales.
- **Capacidad suficiente**: si la RAM se llena, el sistema usa el archivo de paginación del disco, que es miles de veces más lento. Esto pesa más que cualquier diferencia de frecuencia.
- **Rangos (*ranks*)** y número de módulos: dos rangos por canal mejoran algo el rendimiento, pero cuatro módulos pueden obligar a bajar la frecuencia.
- **Perfiles XMP (Intel) / EXPO (AMD)**: hay que activarlos en la BIOS. Si no, la memoria funciona a la velocidad JEDEC base, más lenta que la anunciada.
- **Compatibilidad con la plataforma**: la velocidad máxima que admite el controlador de memoria de la CPU y la relación con el reloj interno (en AMD, FCLK/UCLK; en Intel, modo Gear). Una memoria más rápida de lo que la CPU admite no aporta nada.

### 9. Relación entre bus de datos y bus de direcciones

- El **bus de direcciones** indica **qué posición** se quiere leer o escribir. Con **n** líneas se pueden direccionar **2ⁿ posiciones**.
- El **bus de datos** transporta **el contenido** de esa posición. Su anchura (**m** bits) es el tamaño de la palabra que se lee o escribe en cada acceso.
- Capacidad máxima = **2ⁿ × m bits**.

Ejemplo con palabra de 8 bits:

- Bus de direcciones de **16 bits** → 2¹⁶ = 65.536 posiciones.
- Bus de datos de **8 bits** → cada posición guarda 1 byte.
- Capacidad = 65.536 × 1 B = **64 KB**.
- Si quisiéramos 128 KB con la misma palabra, haría falta **1 línea de dirección más** (17 bits). Para leer 16 bits por acceso, el bus de datos tendría que ser de 16 líneas.

Otro ejemplo conocido: con 32 bits de dirección y palabras de 1 byte → 2³² B = **4 GB**, el límite de los sistemas de 32 bits.

### 10. Funcionamiento de la SRAM y la DRAM

| | SRAM (estática) | DRAM (dinámica) |
| --- | --- | --- |
| Celda | **Biestable (flip-flop) de 6 transistores** | **1 transistor + 1 condensador** |
| Cómo guarda el bit | Dos inversores realimentados mantienen el estado mientras haya alimentación | Con la **carga del condensador** (cargado = 1, descargado = 0) |
| Refresco | **No necesita** | El condensador se descarga: hay que **refrescar** cada fila periódicamente (cada 64 ms) |
| Lectura | No destructiva | **Destructiva**: al leer se descarga y hay que reescribir |
| Velocidad | Muy rápida | Más lenta |
| Densidad / precio | Poca densidad, cara | Mucha densidad, barata |
| Uso | **Memoria caché** (L1, L2, L3), registros | **Memoria principal** (módulos DDR), memoria de las gráficas (GDDR) |

### 11. Cómo se carga la caché y operaciones entre RAM y procesador

1. La CPU pide un dato por su dirección y primero lo busca en la **L1**. Compara la *etiqueta* (*tag*) de la dirección con las líneas guardadas.
2. **Acierto (*hit*)**: el dato está en la caché y se entrega en pocos ciclos.
3. **Fallo (*miss*)**: lo busca en **L2**, luego en **L3** y, si no está en ninguna, en la **RAM**.
4. De la RAM no se trae solo el dato, sino la **línea de caché completa (64 bytes)** que lo contiene. Por la localidad espacial, es probable que se usen los datos vecinos. La línea se copia en L3, L2 y L1.
5. Si la caché está llena, hay que **reemplazar** una línea. Normalmente es la que lleva más tiempo sin usarse (**LRU**).
6. **Escrituras**:
   - ***Write-through***: se escribe a la vez en la caché y en la RAM. Es sencillo, pero genera más tráfico.
   - ***Write-back*** (la habitual): solo se escribe en la caché y la línea se marca como **sucia** (*dirty bit*). Se copia a la RAM cuando se reemplaza.
7. **Prebúsqueda (*prefetch*)**: la CPU detecta patrones de acceso y trae líneas a la caché antes de que se pidan.
8. **Coherencia**: con varios núcleos, un protocolo (por ejemplo, **MESI**) asegura que si un núcleo modifica un dato, los demás no usen una copia antigua.

Organización: la caché puede ser de correspondencia **directa**, **totalmente asociativa** o **asociativa por conjuntos** (la habitual, por ejemplo 8 o 12 vías).

---

## Actividad 2 · Tabla de módulos

Fórmulas:

- **Frecuencia efectiva (MT/s)** = frecuencia del reloj × accesos por ciclo
- **Tasa de transferencia (MB/s)** = frecuencia efectiva × 8 bytes (bus de 64 bits)
- **Nomenclatura:** DDRx-*frecuencia efectiva* · PCx-*tasa de transferencia*

| Nombre del módulo | DDR - número | Frecuencia del reloj | Frecuencia efectiva | Accesos por ciclo | Tasa de transferencia | Tensión |
| --- | --- | --- | --- | --- | --- | --- |
| PC-1600 | DDR-200 | 100 MHz | 200 MHz | 2 | 1.600 MB/s | 2,5 V |
| **PC-2700** | DDR-333 | 166 MHz | **333 MHz** | **2** | **2.666 MB/s** (≈ 2.700) | **2,5 V** |
| **PC2-4800** | **DDR2-600** | 150 MHz | 600 MHz | **4** | **4.800 MB/s** | 1,8 V |
| PC4-21328 | **DDR4-2666** | 333 MHz | **2.666 MHz** | **8** | **21.328 MB/s** | **1,2 V** |
| **PC3-12800** | DDR3-1600 | 200 MHz | **1.600 MHz** | **8** | **12.800 MB/s** | **1,5 V** |
| **PC4-17000** (17.064) | **DDR4-2133** | 266 MHz | **2.133 MHz** | **8** | **17.064 MB/s** | 1,2 V |
| PC2-**6400** | **DDR2-800** | 200 MHz | **800 MHz** | **4** | 6.400 MB/s | **1,8 V** |
| **PC3-16000** | DDR3-**2000** | 250 MHz | 2.000 MHz | **8** | **16.000 MB/s** | **1,5 V** (1,65 V con perfil XMP) |
| PC5-44800 | **DDR5-5600** | **350 MHz** | **5.600 MHz** | **16** | **44.800 MB/s** | 1,1 V |

Cómo se deducen las filas con pocos datos:

- **Fila 3**: 600 ÷ 150 = 4 accesos → DDR2 (lo confirman los 1,8 V).
- **Fila 6**: 266 MHz y 1,2 V → DDR4 (con 8 accesos, 2.133 MT/s). Una DDR3 a 1,2 V no existe (la DDR3L funciona a 1,35 V).
- **Fila 7**: 6.400 ÷ 8 = 800 MT/s; 800 ÷ 200 = 4 accesos → DDR2-800.
- **Fila 9**: 44.800 ÷ 8 = 5.600 MT/s → DDR5-5600; 5.600 ÷ 16 = 350 MHz. En DDR5 cada módulo tiene dos subcanales de 32 bits, pero en total siguen siendo 64 bits, así que la fórmula de los 8 bytes es válida.

---

## Actividad 3 · Clasificación de módulos

| Número | Tipo | Contactos | Tensión de funcionamiento |
| --- | --- | --- | --- |
| 1 | **DDR4 SO-DIMM** (Crucial, portátil) | 260 | 1,2 V |
| 2 | **DDR2 SO-DIMM** (Transcend 2 GB DDR2-800, portátil) | 200 | 1,8 V |
| 3 | **DDR3 SO-DIMM** (Kingston KVR16S11/8 → DDR3-1600, 8 GB, portátil) | 204 | 1,5 V (lo indica la etiqueta) |
| 4 | **DDR2 DIMM** (KomputerBay PC2-6400, Non-ECC Unbuffered, sobremesa) | 240 | 1,8 V |
| 5 | **DDR3 DIMM** con disipador (Kingston HyperX Savage, sobremesa) | 240 | 1,5 V (1,65 V con perfil XMP) |
| 6 | **DDR4 RDIMM VLP** (Crucial, servidor: *registered*, con ECC, perfil muy bajo) | 288 | 1,2 V |

Pistas para identificarlos:

- **SO-DIMM** (cortos, para portátiles): DDR2 200 contactos, DDR3 204 y DDR4 260, cada uno con la muesca en una posición distinta.
- **DIMM** (largos, para sobremesa): DDR2 y DDR3 tienen 240 contactos (la muesca cambia de sitio), y DDR4 tiene 288, con el borde de contactos ligeramente curvado.
- En las etiquetas aparece información útil: "DDR4 SODIMM", "DDR2 800 SO-DIMM", "1.5V", "PC2-6400 DIMM 240Pin", "DDR4 VLP RDIMM".
- **Módulo 5**: la gama HyperX Savage existió en DDR3 y en DDR4. El de la imagen es el DDR3 (240 contactos, borde recto). Si un alumno contesta DDR4 justificándolo, conviene revisar con él la posición de la muesca.

---

## Actividad 4 · Tecnologías de memoria (individual)

Cada alumno explica una. Puntos clave que deberían aparecer (qué es, cómo funciona, ventajas, inconvenientes y dónde se usa):

| Tecnología | Qué es y cómo funciona | Ventajas | Inconvenientes | Dónde se usa |
| --- | --- | --- | --- | --- |
| **HBM3E** | DRAM **apilada en vertical** (8–12 chips) unidos por **TSV** (vías de silicio). Se coloca sobre un *interposer* junto a la GPU/CPU, con un bus de **1.024 bits por pila** | Ancho de banda enorme (≈ 1,2 TB/s por pila), poco consumo por bit transferido, ocupa poco espacio | Muy cara, fabricación compleja, no se puede ampliar | Aceleradores de IA y GPU de centro de datos (NVIDIA H200/B200, AMD Instinct) |
| **GDDR7** | Memoria gráfica sucesora de GDDR6. Usa señal **PAM3** (3 niveles por pulso en lugar de 2) para transmitir más datos por ciclo | Más de 28–32 Gb/s por pin, más ancho de banda con el mismo número de chips, mejor eficiencia | Más cara que GDDR6; más latencia que la DDR (está optimizada para ancho de banda) | Tarjetas gráficas actuales (NVIDIA RTX 50) |
| **Intel Optane** | Basada en **3D XPoint** (Intel y Micron): celdas que cambian de resistencia, **no volátil**, direccionable por bytes. Se vendió como SSD, como caché de disco y como módulos DIMM de memoria persistente | Latencia mucho más baja que la NAND, enorme resistencia a escrituras, no pierde los datos | Cara, menos capacidad que la NAND, necesitaba plataformas Intel concretas | Servidores y estaciones de trabajo. **Descontinuada en 2022**: Micron abandonó 3D XPoint en 2021 y para Intel no era rentable |
| **Memorias 2D y 3D** | **2D (planar)**: las celdas en un solo plano. **3D**: se **apilan capas** de celdas en vertical (3D NAND, con más de 200–300 capas; y 3D DRAM en investigación) | Mucha más capacidad en el mismo espacio y menor coste por GB. Las celdas 3D pueden ser más grandes y duraderas | Fabricación más compleja; más calor en las capas internas | SSD actuales (toda la NAND moderna es 3D), memoria apilada (HBM) |
| **CAMM2** | Estándar **JEDEC (2023)**, basado en el CAMM de Dell. Módulo plano que se **atornilla y presiona** sobre la placa (*compression attached*) en vez de insertarse en una ranura. **Un solo módulo puede dar doble canal** | Más fino, pistas más cortas → más velocidad que SO-DIMM. Se puede **sustituir y ampliar** | Poco extendido todavía; necesita placas diseñadas para él | Portátiles finos y algunas placas de sobremesa (versión DDR5) |
| **LPCAMM2** | Versión de CAMM2 con memoria **LPDDR5X** (de bajo consumo) | Consumo y velocidad de LPDDR, pero **reemplazable** (la LPDDR normalmente va soldada) y ocupa menos que dos SO-DIMM | Pocos modelos, precio más alto | Portátiles (por ejemplo, Lenovo ThinkPad P1 Gen 7) |
| **MRAM** | Memoria **magnetorresistiva**: el bit se guarda en la **orientación magnética** de una unión túnel (MTJ). La resistencia cambia según si las capas magnéticas son paralelas o no. La variante actual es STT-MRAM | **No volátil**, rápida, casi ilimitada en escrituras, resistente a radiación | Densidad baja y coste alto frente a DRAM y NAND | Microcontroladores, sistemas industriales y de automoción, satélites, cachés no volátiles |
| **UltraRAM** | Memoria experimental de la **Universidad de Lancaster** (spin-off Quinas Technology). Usa semiconductores compuestos (InAs/AlSb) con **barreras de túnel resonante** para atrapar la carga | Promete ser **no volátil** con velocidad cercana a la DRAM, muy poco consumo y gran resistencia | **En fase de prototipo/investigación**, aún no se fabrica en masa | Futuro candidato a "memoria universal" (sustituir a la vez la RAM y el almacenamiento) |
