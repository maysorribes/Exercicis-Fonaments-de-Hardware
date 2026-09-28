<p style="font-size: 1.3em;"><strong>CFGS Administración de Sistemas Informáticos y en Red (1º curso)</strong></p>

Material elaborado para el módulo **Fundamentos de Hardware**

# Tema 1. Arquitectura de computadores — SOLUCIÓN (documento para el profesorado)

!!! warning "Página no enlazada"
    Esta página existe en el sitio pero **no aparece en el menú de navegación**. Solo es accesible con el enlace directo. No compartas este enlace con el alumnado.

## Ejercicio 1. Elementos de un sistema informático

| Elemento | Clasificación |
| -------- | -------------- |
| Monitor de 27 pulgadas | Hardware |
| Windows 11 | Software (sistema operativo) |
| Técnica de soporte que instala los equipos del aula | Parte humana |
| Manual de la placa base en PDF | Documentación |
| LibreOffice Calc | Software (aplicación) |
| Unidad SSD NVMe | Hardware |
| Firmware UEFI de la placa base | Software (**caso dudoso**, ver nota) |
| Controlador (driver) de la impresora | Software |
| Usuario que trabaja con el programa de contabilidad | Parte humana |
| Hoja de características (datasheet) de un procesador | Documentación |

!!! note "Nota"
    El firmware es software, porque son instrucciones, pero está grabado en un chip de memoria flash de la placa y viene de fábrica con el hardware. Por eso se considera un caso intermedio. También se acepta la respuesta de que el manual en PDF es software (un archivo) si el alumno lo razona, aunque su función en el sistema es la de documentación.

## Ejercicio 2. Von Neumann y Harvard

| Característica | Von Neumann | Harvard |
| --------------- | ------------ | -------- |
| Memoria para datos e instrucciones | Una única memoria compartida | Dos memorias físicamente separadas |
| Número de buses de acceso a memoria | Un conjunto de buses compartido | Buses independientes para cada memoria |
| ¿Puede leer instrucción y dato a la vez? | No: accede primero a uno y después al otro | Sí, de forma simultánea |
| Complejidad y coste | Más sencilla y barata | Más compleja y cara |
| Ejemplo de dispositivo | Ordenador personal (PC) | Microcontroladores (Arduino), procesadores digitales de señal (DSP) |

- **Actividad 1.** Porque el diseño Von Neumann es **más sencillo y barato**. Además, es más flexible: una sola memoria se reparte según haga falta entre programas y datos. Un PC necesita cargar programas desde el disco como si fueran datos y después ejecutarlos, algo natural cuando todo está en la misma memoria.

- **Arduino Uno** sigue la arquitectura **Harvard**: programa en flash y variables en SRAM, con buses separados.

- La CPU puede leer a la vez una instrucción (de L1i) y un dato (de L1d), que es la ventaja de Harvard. Como la memoria principal sigue siendo única, se habla de **arquitectura Harvard modificada**: Harvard dentro del procesador y Von Neumann hacia fuera.

## Ejercicio 3. Componentes de la CPU y de la memoria

| Función | Componente | Función | Componente |
| ------- | ---------- | ------- | ---------- |
| 1 | E (Acumulador) | 5 | D (Reloj) |
| 2 | F (Registro de estado) | 6 | G (RDM) |
| 3 | A (Contador de programa) | 7 | H (RIM) |
| 4 | B (Registro de instrucción) | 8 | C (Decodificador) |

## Ejercicio 4. Frecuencia de reloj

- T = 1/f. **1 MHz:** 1 / 10⁶ = **1 µs**. **3,2 GHz:** 1 / (3,2 × 10⁹) = **0,3125 ns**. **5 GHz:** 1 / (5 × 10⁹) = **0,2 ns**.

- 4 ciclos × 0,3125 ns = **1,25 ns** por instrucción. En un segundo: 1 / 1,25 ns = **800 millones de instrucciones** (800 MIPS).

- 3,2 × 10⁹ / 10⁶ = **3200 veces** más ciclos por segundo.

- **No.** La frecuencia es la de **cada núcleo**: los 8 núcleos trabajan a 3,2 GHz en paralelo, cada uno con su propia tarea. El rendimiento total puede ser mayor que el de un solo núcleo, pero no equivale a un procesador de 25,6 GHz, porque no todos los programas pueden repartir su trabajo entre varios núcleos.

## Ejercicio 5. Buses: ancho y capacidad de memoria

- **16 bits:** 2¹⁶ = 65 536 bytes = **64 KiB**. **20 bits:** 2²⁰ = 1 048 576 bytes = **1 MiB**.

- **32 bits:** 2³² = 4 294 967 296 bytes = **4 GiB**. Es todo lo que puede direccionar un sistema de 32 bits. Además, parte de ese espacio de direcciones se reserva para dispositivos (tarjeta gráfica, PCI Express...), así que en la práctica un Windows de 32 bits solo aprovecha entre 3 y 3,5 GB de RAM.

- 64 GiB = 2⁶ × 2³⁰ = 2³⁶ bytes → **36 líneas** de dirección.

- 256 KiB = 262 144 bytes. Con palabras de 2 bytes: 262 144 / 2 = 131 072 palabras = 2¹⁷ → **17 líneas** de dirección. El bus de datos debe tener como mínimo **16 bits**.

- **Actividad 2.** Para poder transferir una palabra completa en un solo acceso. Si el bus fuera más estrecho, cada palabra necesitaría varias transferencias, lo que haría el sistema más lento y complicaría el control.

- 3200 × 10⁶ transferencias/s × 64 bits / 8 = 3200 × 10⁶ × 8 bytes = **25,6 GB/s**. En doble canal se duplica: **51,2 GB/s**.

## Ejercicio 6. Tipos de memoria

| Uso | Tipo de memoria | ¿Volátil? |
| --- | ---------------- | ---------- |
| Módulos de memoria principal de un portátil | DRAM (DDR4/DDR5) | Sí |
| Memoria caché dentro del procesador | SRAM | Sí |
| Chip donde está grabado el firmware UEFI, que se puede actualizar | Flash (tipo de EEPROM) | No |
| Memoria de la placa que conserva la fecha y la hora con una pila | CMOS RAM | Sí, pero la pila la mantiene |
| Memoria USB (pendrive) y SSD | Flash | No |
| Chip que se programaba con luz ultravioleta en los equipos de los años 80 | EPROM | No |

La **DRAM** guarda cada bit en un condensador que se descarga con el tiempo, así que hay que leerlo y reescribirlo periódicamente (refresco). La **SRAM** usa biestables, que mantienen su estado mientras haya alimentación. No se usa SRAM para toda la memoria principal porque necesita unos seis transistores por bit, frente a un transistor y un condensador en la DRAM: ocupa mucho más espacio y es mucho más cara. Por eso se reserva para la caché, pequeña y muy rápida.

## Ejercicio 7. Periféricos y mecanismos de E/S

| Dispositivo | Tipo de periférico |
| ------------ | -------------------- |
| Teclado | Entrada |
| Monitor táctil | Entrada/salida |
| Impresora multifunción | Entrada/salida |
| Disco SSD externo USB | Almacenamiento |
| Tarjeta de red Wi-Fi | Comunicación |
| Webcam | Entrada |
| Auriculares con micrófono | Entrada/salida |
| Lector de huellas dactilares | Entrada |
| Proyector | Salida |

**Mecanismos de E/S:**

- **Pulsar una tecla:** por **interrupciones**. El teclado avisa a la CPU solo cuando hay una pulsación, y la CPU no pierde tiempo esperando.
- **Copiar 20 GB:** **DMA**. El controlador transfiere los datos directamente a la memoria y la CPU queda libre para otras tareas.
- **Consultar un botón continuamente:** **E/S programada** (sondeo o *polling*). Es sencilla, pero la CPU está ocupada todo el tiempo.
- **Paquete de red:** **interrupción y DMA**. La tarjeta copia el paquete a la memoria por DMA y avisa a la CPU con una interrupción cuando ha terminado.

El **controlador de E/S** es la parte del interfaz que gestiona la comunicación entre la CPU y el periférico. Ejemplos: la parte hardware sería la controladora USB de la placa base o el chip controlador de un SSD; la parte software, el *driver* que instala el sistema operativo.

## Ejercicio 8. Simulación del ciclo de instrucción

| Fase | PC | RDM | RIM | RI | ACC | Qué ocurre |
| ----- | --- | --- | --- | --- | --- | ---------- |
| Inicio | 0 | – | – | – | 0 | Estado inicial |
| Búsqueda 1 | 1 | 0 | LOAD 10 | LOAD 10 | 0 | Lee la instrucción de la dirección 0 |
| Ejecución 1 | 1 | 10 | 5 | LOAD 10 | 5 | Lee el dato de la dirección 10 y lo carga en ACC |
| Búsqueda 2 | 2 | 1 | ADD 11 | ADD 11 | 5 | Lee la instrucción de la dirección 1 |
| Ejecución 2 | 2 | 11 | 7 | ADD 11 | 12 | Lee el 7; la ALU calcula 5 + 7 |
| Búsqueda 3 | 3 | 2 | STORE 12 | STORE 12 | 12 | Lee la instrucción de la dirección 2 |
| Ejecución 3 | 3 | 12 | 12 | STORE 12 | 12 | Pasa ACC al RIM y lo escribe en la dirección 12 |
| Búsqueda 4 | 4 | 3 | HALT | HALT | 12 | Lee HALT; al ejecutarla, el programa se detiene |

- La dirección 12 contiene **12**.

- Por el **bus de direcciones** viaja la dirección de la instrucción (el valor del PC, copiado al RDM). Por el **bus de control**, la orden de lectura de memoria y la señal de reloj. Por el **bus de datos**, la instrucción leída, que llega al RIM.

- Con −5: 5 + (−5) = **0**, y se activa el *flag* de **cero (Z)**. Con −7: 5 + (−7) = **−2**, y se activa el *flag* de **signo o negativo (N)**.

- Porque **datos e instrucciones están en la misma memoria** (instrucciones en las direcciones 0 a 3 y datos en 10 a 12), **se accede a ellos indicando su dirección** y **la ejecución es secuencial**: el PC se incrementa en 1 tras cada búsqueda.

## Ejercicio 9. Práctica con un equipo real

Respuesta abierta: los valores dependen del equipo de cada alumno. Al corregir, comprobar que los datos son coherentes entre sí (por ejemplo, que la frecuencia máxima sea mayor que la base y que el tipo de RAM corresponda a la generación del procesador).

- La L1 está dividida (**L1i** para instrucciones y **L1d** para datos) porque es la más cercana al núcleo y se consulta en cada ciclo. Separarla permite leer una instrucción y un dato a la vez, como en Harvard. La L2 y la L3 son **unificadas**, porque están más lejos y lo que se busca en ellas es aprovechar mejor la capacidad.

- **No coincide del todo.** La máquina virtual ve el modelo del procesador del equipo físico, pero solo los núcleos y la memoria que se le han asignado en VirtualBox. Los discos y otros periféricos aparecen como dispositivos virtuales (por ejemplo, *VBOX HARDDISK* o *VirtualBox USB Tablet*).
