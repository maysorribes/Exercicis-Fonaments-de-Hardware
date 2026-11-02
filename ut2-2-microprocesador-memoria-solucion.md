# Soluciones · UT2.2 Microprocesador y memoria

Fundamentos de Hardware · CFGS ASIR (1.º curso)

---

## Ejercicio 1

**Explica qué es un transistor y cómo, a partir de transistores, se construyen puertas lógicas y circuitos integrados. ¿Qué significa que un procesador se fabrique en 7 nm?**

### Respuesta

**El transistor** es un componente semiconductor (normalmente de silicio) que funciona como un **interruptor controlado eléctricamente**. Tiene tres terminales; en el tipo que se usa en los procesadores (MOSFET) se llaman *fuente*, *drenador* y *puerta*. Según la tensión aplicada en la puerta, la corriente circula o no entre fuente y drenador. Así representa los dos valores binarios: **conduce = 1**, **no conduce = 0**.

**Puertas lógicas:** combinando varios transistores se obtienen circuitos que realizan operaciones lógicas básicas. Con la tecnología CMOS, por ejemplo:

- Una puerta **NOT** se construye con 2 transistores.
- Una puerta **NAND** o **NOR** se construye con 4 transistores.
- A partir de NAND se puede construir cualquier otra puerta (AND, OR, XOR...).

**Circuitos integrados:** combinando puertas lógicas se construyen circuitos más complejos (sumadores, biestables, registros, multiplexores...) y, a partir de ellos, unidades completas como la ALU. Un **circuito integrado** (chip) es una pieza de silicio en la que se fabrican, todos a la vez, miles de millones de transistores ya interconectados. Se fabrican sobre obleas de silicio mediante **fotolitografía**, que "dibuja" los circuitos con luz ultravioleta capa a capa. Cada oblea se corta después en muchos chips (*dies*).

**7 nm** es el **nodo o proceso de fabricación**. Originalmente indicaba el tamaño de la puerta del transistor. Hoy es sobre todo un **nombre comercial** que identifica la generación de la tecnología, y ya no corresponde a una medida física concreta. Lo importante es que un nodo más pequeño permite:

- Más transistores en el mismo espacio (más densidad).
- Menor consumo y menos calor.
- Frecuencias más altas.

---

## Ejercicio 2

**Compara CISC, RISC y el enfoque híbrido. ¿Por qué ARM destaca en eficiencia energética y x86 en rendimiento?**

### Respuesta

| Característica | CISC | RISC |
|---|---|---|
| Significado | *Complex Instruction Set Computer* | *Reduced Instruction Set Computer* |
| Juego de instrucciones | Muchas instrucciones, algunas muy complejas | Pocas instrucciones y sencillas |
| Longitud de instrucción | Variable | Fija |
| Ciclos por instrucción | Varios | Normalmente uno |
| Acceso a memoria | Muchas instrucciones pueden operar con memoria | Solo *load* y *store* acceden a memoria |
| Registros | Pocos | Muchos |
| Ejecución | Suele usar microcódigo | Por hardware, facilita la segmentación (*pipeline*) |
| Ejemplos | x86 (Intel, AMD) | ARM, RISC-V |

**Enfoque híbrido:** los procesadores x86 actuales mantienen hacia fuera el juego de instrucciones CISC (por compatibilidad con todo el software existente), pero internamente **traducen cada instrucción a microoperaciones sencillas de tipo RISC** (*µops*), que son las que se ejecutan realmente. Así combinan la compatibilidad de CISC con la eficiencia de ejecución de RISC.

**ARM y la eficiencia energética:**

- Sus instrucciones son simples y de longitud fija, por lo que decodificarlas necesita menos circuitería y menos energía.
- Se diseñó desde el principio para dispositivos con batería (móviles, tabletas).
- Usa diseños como **big.LITTLE**, que combinan núcleos potentes con núcleos de bajo consumo.

**x86 y el rendimiento:**

- Se ha diseñado tradicionalmente para equipos de sobremesa y servidores, donde se admite un consumo mucho mayor.
- Trabaja a frecuencias muy altas y con núcleos muy grandes.
- Acumula décadas de optimización y una enorme compatibilidad de software.

> Hoy la diferencia es menor: procesadores ARM como los Apple M ofrecen alto rendimiento, y los x86 más recientes han mejorado mucho su eficiencia.

---

## Ejercicio 3

**Enumera las partes del microprocesador (encapsulado, caché, FPU, unidad de control, ALU, registros, iGP) y explica brevemente la función de cada una.**

### Respuesta

| Parte | Función |
|---|---|
| **Encapsulado** | Envoltorio que protege el chip de silicio, le da soporte físico, contiene los contactos (pines o pads) para conectarlo al zócalo de la placa base y transmite el calor al disipador a través del IHS (tapa metálica). |
| **Memoria caché** | Memoria SRAM muy rápida integrada en el procesador que guarda los datos e instrucciones más usados para no tener que ir a buscarlos a la RAM, mucho más lenta. Se organiza en niveles (L1, L2, L3). |
| **FPU** (unidad de coma flotante) | Realiza las operaciones con números decimales (coma flotante), muy usadas en cálculo científico, gráficos o multimedia. |
| **Unidad de control** (UC) | Coordina el funcionamiento de todo el procesador: busca las instrucciones en memoria, las decodifica y genera las señales para que el resto de unidades las ejecuten. |
| **ALU** (unidad aritmético-lógica) | Realiza las operaciones aritméticas (suma, resta...) y lógicas (AND, OR, NOT, comparaciones) con números enteros. |
| **Registros** | Pequeñas memorias internas, las más rápidas del sistema, que almacenan temporalmente los datos, direcciones e instrucciones con los que trabaja el procesador en cada momento (por ejemplo, el contador de programa o el acumulador). |
| **iGP** (gráfica integrada) | Procesador gráfico incluido en el mismo chip que genera la imagen sin necesidad de una tarjeta gráfica dedicada. Usa parte de la RAM del sistema como memoria de vídeo. |

---

## Ejercicio 4

**Explica la diferencia entre núcleos físicos e hilos. ¿Qué significa que un procesador sea «8C/16T» y qué tecnologías lo permiten en Intel y en AMD?**

### Respuesta

- **Núcleo físico:** unidad de procesamiento completa e independiente dentro del procesador, con su propia ALU, FPU, registros y caché L1/L2. Cada núcleo es, en la práctica, un procesador.
- **Hilo (thread):** secuencia de instrucciones que el sistema operativo puede asignar a un núcleo. Con la tecnología **SMT** (*Simultaneous Multithreading*), un núcleo físico puede atender **dos hilos a la vez**, aprovechando las unidades que el otro hilo deja libres en cada momento. El sistema operativo ve cada hilo como un **núcleo lógico**.

Un hilo extra no equivale a un núcleo extra: los dos hilos comparten los recursos del mismo núcleo. La mejora de rendimiento suele estar entre un 15 % y un 30 %, según la tarea.

**8C/16T** significa **8 núcleos físicos (Cores) y 16 hilos (Threads)**: cada núcleo ejecuta 2 hilos, así que el sistema operativo ve 16 procesadores lógicos.

**Tecnologías:**

- **Intel:** Hyper-Threading (HT).
- **AMD:** SMT (*Simultaneous Multithreading*).

---

## Ejercicio 5

**Un procesador funciona a 1,3 V y consume 104 W. ¿Qué intensidad circula por él? Y otro con 1,2 V y 75 A, ¿qué potencia consume?**

### Respuesta

Usamos la fórmula de la potencia eléctrica:

```
P = V × I
```

**Primer procesador:** despejamos la intensidad.

```
I = P / V = 104 W / 1,3 V = 80 A
```

**Intensidad: 80 A**

**Segundo procesador:**

```
P = V × I = 1,2 V × 75 A = 90 W
```

**Potencia: 90 W**

---

## Ejercicio 6

**Explica qué es el thermal throttling y cuál es la diferencia entre TjMax, Tdie y TCase.**

### Respuesta

**Thermal throttling** es un mecanismo de protección del procesador: cuando su temperatura se acerca al límite máximo, **reduce automáticamente su frecuencia y su voltaje** para generar menos calor y evitar daños. La consecuencia es una **pérdida de rendimiento**. Si aun así la temperatura sigue subiendo, el equipo se apaga. Suele deberse a una refrigeración insuficiente, pasta térmica seca, polvo o mala ventilación de la caja.

| Término | Significado |
|---|---|
| **TjMax** (*Junction Temperature Max*) | Temperatura máxima que el fabricante permite en el interior del chip (en la unión de los transistores). Al alcanzarla se activa el thermal throttling. Suele estar entre 95 °C y 105 °C. |
| **Tdie** | Temperatura real del chip de silicio (*die*) en cada momento, medida por los sensores internos del procesador. Es la que muestran los programas de monitorización. |
| **TCase** | Temperatura medida en la superficie exterior del encapsulado, en el centro del IHS (tapa metálica). Siempre es menor que la del interior del chip; el fabricante indica su valor máximo como referencia para diseñar la refrigeración. |

---

## Ejercicio 7

**Explica en qué consiste el overclocking, qué requisitos hacen falta, qué riesgos tiene y qué es el undervolting.**

### Respuesta

**Overclocking:** consiste en hacer funcionar el procesador (o la RAM o la gráfica) a una **frecuencia superior a la de fábrica** para obtener más rendimiento. Se hace desde la BIOS/UEFI o con software del fabricante, subiendo el **multiplicador** o la frecuencia base (BCLK). Normalmente también hay que **subir el voltaje** para que funcione de forma estable.

**Requisitos:**

- **Procesador desbloqueado:** en Intel, los modelos con la letra **K** (o KF); en AMD, la mayoría de los Ryzen.
- **Chipset y placa base que lo permitan:** en Intel, chipsets de la serie **Z**; en AMD, de las series **B** y **X**.
- **Placa base con un buen VRM** (etapa de alimentación del procesador).
- **Buena refrigeración** (disipador de gama alta o refrigeración líquida).
- **Fuente de alimentación** de calidad y con potencia suficiente.

**Riesgos:**

- Inestabilidad del sistema: cuelgues, reinicios, pantallazos azules, errores en los datos.
- Más temperatura y más consumo.
- Reducción de la vida útil del procesador por degradación del silicio.
- Pérdida de la garantía.
- En casos extremos, daño permanente del componente.

**Undervolting:** consiste en **reducir el voltaje** del procesador manteniendo la frecuencia. Como cada chip suele admitir algo menos de voltaje del que trae de fábrica, se consigue menos temperatura, menos consumo, menos ruido y, a veces, más rendimiento sostenido al evitar el thermal throttling. Es muy útil en portátiles. Si se baja demasiado, el sistema se vuelve inestable.

---

## Ejercicio 8

**Explica qué es un acierto y un fallo de caché, y por qué la búsqueda de un dato empieza siempre en la L1. Compara los tres niveles L1, L2 y L3.**

### Respuesta

- **Acierto de caché (*cache hit*):** el procesador busca un dato y lo encuentra en la caché, así que lo obtiene muy rápido.
- **Fallo de caché (*cache miss*):** el dato no está en ese nivel de caché y hay que buscarlo en el siguiente nivel o, en último caso, en la RAM, mucho más lenta. Al traerlo, se copia en la caché para los próximos accesos.

**¿Por qué se empieza por la L1?** Porque es la memoria **más rápida y más cercana al núcleo**. La jerarquía se organiza de la más rápida y pequeña a la más lenta y grande. Si el dato está en L1 (lo más probable, porque guarda los datos más recientes) se obtiene en muy pocos ciclos. Solo si falla se pasa a L2, luego a L3 y finalmente a la RAM.

| Característica | L1 | L2 | L3 |
|---|---|---|---|
| Velocidad | La más rápida (≈ 4-5 ciclos) | Intermedia (≈ 12-15 ciclos) | La más lenta de las tres (≈ 40-50 ciclos) |
| Tamaño típico | 32-64 KB por núcleo | 256 KB - 3 MB por núcleo | 8-96 MB en total |
| Organización | Dividida en instrucciones (L1i) y datos (L1d) | Unificada | Unificada |
| Compartida | Privada de cada núcleo | Normalmente privada de cada núcleo | Compartida por todos los núcleos |
| Coste por byte | El más alto | Intermedio | El más bajo de las tres |

---

## Ejercicio 9

**Compara la DRAM y la SRAM en cuanto a funcionamiento, velocidad, coste y uso típico.**

### Respuesta

| Característica | DRAM (RAM dinámica) | SRAM (RAM estática) |
|---|---|---|
| Funcionamiento | Cada bit se guarda como una carga en un **condensador** con un transistor (1T1C). El condensador se descarga, así que necesita **refresco** periódico. | Cada bit se guarda en un **biestable** de unos 6 transistores. **No necesita refresco** mientras tenga alimentación. |
| Velocidad | Más lenta | Mucho más rápida |
| Densidad | Alta (muchos bits en poco espacio) | Baja (ocupa mucho más por bit) |
| Coste | Barata | Muy cara |
| Consumo | Consume también en el refresco | Consumo bajo en reposo |
| Uso típico | Memoria principal (módulos DDR), memoria de las tarjetas gráficas (GDDR) | Memoria caché del procesador (L1, L2, L3) y registros |

Las dos son **volátiles**: pierden la información al quitar la alimentación.

---

## Ejercicio 10

**Calcula la tasa de transferencia y el nombre estándar de un módulo DDR4-3200, y la frecuencia efectiva y real de un módulo PC4-25600.**

### Respuesta

Fórmulas:

- Tasa de transferencia (MB/s) = frecuencia efectiva (MHz) × 8 bytes (bus de 64 bits)
- Frecuencia efectiva (MHz) = tasa de transferencia (MB/s) / 8 bytes
- Frecuencia real (MHz) = frecuencia efectiva / prefetch (DDR: 2, DDR2: 4, DDR3: 8, **DDR4: 8**)

**a) DDR4-3200**

La frecuencia efectiva es 3200 MHz.

```
Tasa de transferencia = 3200 MHz × 8 bytes = 25 600 MB/s
```

- **Tasa de transferencia:** 25 600 MB/s
- **Nombre estándar:** **PC4-25600**

**b) PC4-25600**

La tasa de transferencia es 25 600 MB/s.

```
Frecuencia efectiva = 25 600 MB/s / 8 bytes = 3200 MHz
Frecuencia real     = 3200 MHz / 8          = 400 MHz
```

- **Frecuencia efectiva:** 3200 MHz (es un DDR4-3200)
- **Frecuencia real:** **400 MHz**

---

## Ejercicio 11

**¿Qué información almacena el chip SPD de un módulo de RAM y para qué se utiliza?**

### Respuesta

El **SPD** (*Serial Presence Detect*) es un pequeño chip de memoria no volátil (EEPROM) soldado en el propio módulo de RAM. Almacena las características del módulo:

- Tipo de memoria (DDR3, DDR4, DDR5...).
- Capacidad y organización (número de chips, rangos o *ranks*).
- Frecuencias de funcionamiento soportadas.
- Temporizaciones o latencias (CL, tRCD, tRP, tRAS...) para cada frecuencia.
- Voltaje de funcionamiento.
- Fabricante, número de serie y fecha de fabricación.
- Perfiles de overclocking: **XMP** (Intel) o **EXPO** (AMD).

**Uso:** al arrancar el equipo, la **BIOS/UEFI lee el SPD** de cada módulo y configura automáticamente el controlador de memoria con la frecuencia, las latencias y el voltaje adecuados, sin que el usuario tenga que hacerlo a mano. Si se activa el perfil XMP/EXPO, usa los valores de ese perfil. Los programas como CPU-Z también leen el SPD (pestaña *SPD*) para mostrar la información del módulo.

---

## Ejercicio 12

**Explica qué es el dual channel, qué requisitos exige y en qué ranuras deben ponerse los módulos.**

### Respuesta

**Dual channel** (doble canal) es una tecnología en la que el controlador de memoria **accede a dos módulos a la vez**, cada uno por un canal independiente. Así el bus pasa de 64 a 128 bits y se **duplica el ancho de banda teórico** respecto a usar un solo módulo. Por ejemplo, dos módulos DDR4-3200 en dual channel ofrecen 2 × 25 600 MB/s = 51 200 MB/s.

**Requisitos:**

- Que el **procesador (controlador de memoria) y la placa base** lo soporten.
- Instalar los módulos **por parejas** (2 o 4 módulos).
- Lo recomendable es que sean **idénticos**: misma capacidad, frecuencia y latencias, a ser posible un kit del mismo fabricante. Si las frecuencias o latencias son distintas, todos funcionan con los valores del más lento.

**Ranuras:** cada módulo de la pareja debe ir en un **canal distinto** (canal A y canal B). La posición exacta la indica el **manual de la placa base**:

- Muchas placas marcan con el **mismo color** las ranuras que forman pareja.
- En las placas de 4 ranuras lo habitual es usar la **A2 y la B2**, que suelen ser la **segunda y la cuarta** contando desde el procesador.

---

## Ejercicio 13

**¿En qué se diferencia la memoria HBM de la DDR? ¿Para qué se diseñó y por qué era interesante Optane?**

### Respuesta

**Diferencias entre HBM y DDR:**

| Característica | DDR | HBM (*High Bandwidth Memory*) |
|---|---|---|
| Disposición | Chips colocados uno al lado de otro en un módulo (DIMM) que se inserta en la placa | Chips **apilados en vertical** (3D) y unidos con conexiones a través del silicio (TSV) |
| Ubicación | En las ranuras de la placa base, lejos del procesador | En el mismo encapsulado que el procesador o la GPU, junto a él sobre un *interposer* |
| Ancho del bus | 64 bits por módulo | 1024 bits por pila (o más) |
| Frecuencia | Alta | Más baja |
| Ancho de banda | Moderado | Muy alto |
| Consumo por dato transferido | Mayor | Menor |
| Coste | Bajo | Muy alto |
| Ampliable | Sí, se cambian los módulos | No, va integrada |

**Para qué se diseñó HBM:** para aplicaciones que necesitan mover enormes cantidades de datos por segundo: **tarjetas gráficas de gama alta, aceleradores de inteligencia artificial y supercomputación (HPC)**. Ofrece mucho más ancho de banda que la DDR o la GDDR, consumiendo menos y ocupando menos espacio.

**Intel Optane:** era una memoria desarrollada por Intel y Micron con la tecnología **3D XPoint**. Era interesante porque:

- Es **no volátil**: conserva los datos sin alimentación, como un SSD.
- Es mucho **más rápida** que la memoria flash NAND de los SSD, con una latencia más cercana a la de la RAM.
- Soporta muchas más escrituras, así que es **más duradera** que la NAND.
- Se podía usar como SSD muy rápido, como caché de un disco duro o en módulos DIMM como memoria persistente.

En resumen, cubría el hueco entre la RAM (rápida pero volátil) y el almacenamiento (persistente pero lento). Intel la descontinuó en 2022 por su alto precio y su baja demanda.

---

## Ejercicio 14 (práctica en el aula)

**Con una herramienta de información del sistema (por ejemplo, CPU-Z), identifica en un equipo del aula el modelo de procesador, número de núcleos e hilos, tamaño de las cachés L1/L2/L3, y tipo, capacidad, frecuencia y latencia de la RAM instalada.**

### Respuesta

Los valores dependen del equipo de cada alumno. Dónde encontrar cada dato en CPU-Z:

| Dato | Pestaña de CPU-Z | Campo |
|---|---|---|
| Modelo de procesador | **CPU** | *Name* y *Specification* |
| Núcleos e hilos | **CPU** | *Cores* y *Threads* (abajo a la derecha) |
| Caché L1 | **CPU** o **Caches** | *L1 Data* y *L1 Inst.* |
| Caché L2 | **CPU** o **Caches** | *Level 2* |
| Caché L3 | **CPU** o **Caches** | *Level 3* |
| Tipo de RAM | **Memory** | *Type* |
| Capacidad de RAM | **Memory** | *Size* |
| Frecuencia de RAM | **Memory** | *DRAM Frequency* |
| Latencia de RAM | **Memory** | *CAS# Latency (CL)* |
| Módulos instalados (por ranura) | **SPD** | Desplegable *Memory Slot Selection* |

**Atención a la frecuencia de la RAM:** CPU-Z muestra en *DRAM Frequency* la frecuencia del **bus**, que es la mitad de la efectiva. Por ejemplo, si muestra 1600 MHz, el módulo es un DDR4-3200 (1600 × 2 = 3200 MHz efectivos) y su frecuencia real es 3200 / 8 = 400 MHz.

En la pestaña **Memory**, el campo *Channel #* indica si la memoria funciona en *Single* o *Dual* channel.

**Ejemplo de tabla de resultados:**

| Dato | Valor obtenido |
|---|---|
| Modelo de procesador | |
| Núcleos / hilos | |
| Caché L1 | |
| Caché L2 | |
| Caché L3 | |
| Tipo de RAM | |
| Capacidad de RAM | |
| Frecuencia de RAM (efectiva) | |
| Latencia (CL) | |
| Canal (single / dual) | |
