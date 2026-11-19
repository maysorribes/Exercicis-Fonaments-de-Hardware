# Soluciones · Almacenamiento y tarjetas de expansión

[← Volver al índice](README.md)

---

## Ejercicio 1

**Explica la diferencia entre almacenamiento primario, secundario y terciario, y pon un ejemplo de cada uno.**

| Tipo | Qué es | Características | Ejemplo |
|---|---|---|---|
| **Primario** | Memoria a la que la CPU accede **directamente** para ejecutar programas. | Muy rápida, cara, poca capacidad y normalmente **volátil** (se pierde al apagar). | Memoria RAM (también registros y caché). |
| **Secundario** | Almacenamiento **permanente** del equipo, siempre conectado. La CPU no accede directamente: los datos pasan antes a la RAM. | No volátil, más lento que la RAM, mucha más capacidad y más barato por GB. | Disco duro (HDD) o SSD. |
| **Terciario** | Almacenamiento masivo para **copias de seguridad y archivo**. Los soportes se montan y desmontan (a menudo con un robot) solo cuando se necesitan. | Enorme capacidad, muy barato por GB, acceso lento. | Biblioteca de cintas magnéticas (LTO) o torres de discos ópticos. |

> En algunos libros el almacenamiento terciario se identifica con los soportes **extraíbles** (DVD, memoria USB, disco externo). La idea es la misma: no está siempre disponible y se usa sobre todo para guardar y transportar datos.

---

## Ejercicio 2

**Describe las partes físicas y lógicas de un disco duro (platos, cabezas, pistas, sectores, cilindros, clúster).**

**Partes físicas**

- **Platos**: discos de aluminio o vidrio recubiertos de material magnético, donde se guardan los datos. Cada plato tiene **dos caras** y todos giran juntos sobre el mismo eje, a velocidad constante (5400, 7200, 10 000 o 15 000 rpm).
- **Cabezas de lectura/escritura**: hay **una por cara**. Flotan a unos nanómetros de la superficie sin tocarla y leen o escriben magnetizando la superficie.
- **Brazo y actuador**: el brazo sujeta las cabezas y el actuador (bobina de voz) lo mueve para colocarlas sobre la pista correcta. Todas las cabezas se mueven a la vez.
- **Motor del eje**: hace girar los platos.
- **Placa controladora**: electrónica que gestiona el disco y se comunica con el equipo (SATA).

**Partes lógicas**

- **Pista**: cada uno de los círculos concéntricos en los que se divide una cara.
- **Sector**: cada una de las divisiones de una pista. Es la **unidad mínima** que el disco lee o escribe: 512 bytes tradicionalmente y 4096 bytes en los discos *Advanced Format* actuales.
- **Cilindro**: conjunto de pistas que están en la **misma posición en todas las caras**. Las cabezas se mueven juntas, así que se puede leer un cilindro entero sin mover el brazo.
- **Clúster** (unidad de asignación): grupo de sectores consecutivos que el **sistema de archivos** usa como unidad mínima para guardar un archivo. Por ejemplo, 4 KB en NTFS = 8 sectores de 512 bytes. Un archivo de 1 KB ocupa igualmente un clúster entero.

> Platos, cabezas y brazo son hardware. Pistas, sectores y cilindros los crea el **formateo de bajo nivel** de fábrica. El clúster lo define el **sistema de archivos** al formatear.

---

## Ejercicio 3

**Un disco duro tiene 6 caras, 2000 pistas por cara y 63 sectores por pista. Calcula el número total de sectores y su capacidad si cada sector ocupa 512 bytes.**

**Número total de sectores**

```
Sectores = caras × pistas por cara × sectores por pista
Sectores = 6 × 2000 × 63 = 756 000 sectores
```

**Capacidad**

```
Capacidad = 756 000 × 512 bytes = 387 072 000 bytes
```

Pasado a otras unidades:

- En unidades decimales (las que usan los fabricantes): 387 072 000 / 1000² ≈ **387 MB**
- En unidades binarias (las que muestra Windows): 387 072 000 / 1024² ≈ **369,14 MiB**

> Datos extra: el disco tiene 2000 cilindros (uno por pista) y 6 cabezas (una por cara), es decir, 3 platos.

---

## Ejercicio 4

**Explica la diferencia entre los sistemas de direccionamiento CHS y LBA. ¿Cuál se usa actualmente?**

**CHS (Cylinder–Head–Sector)**

Localiza cada sector con tres números: **cilindro, cabeza y sector**, que corresponden a la geometría física del disco.

- Los sectores se numeran desde 1, y cilindros y cabezas desde 0.
- Problema: los campos tienen un tamaño máximo. Con la BIOS clásica (1024 cilindros, 255 cabezas y 63 sectores) el límite es de unos **8,4 GB**.
- Además, los discos modernos tienen más sectores en las pistas exteriores que en las interiores (*zoned recording*), así que su geometría real ya no encaja en CHS.

**LBA (Logical Block Addressing)**

Numera todos los sectores del disco **de forma lineal**: 0, 1, 2, 3… hasta el último. El sistema operativo solo pide "el bloque número N" y la controladora del disco sabe dónde está físicamente.

- Es más sencillo e independiente de la geometría.
- LBA de 48 bits permite discos de hasta 128 PiB.

Conversión de CHS a LBA:

```
LBA = (C × cabezas + H) × sectores_por_pista + (S − 1)
```

**Actualmente se usa LBA.** CHS solo se conserva por compatibilidad. La tabla de particiones **MBR** usa LBA de 32 bits (límite de 2 TiB) y **GPT** usa LBA de 64 bits.

---

## Ejercicio 5

**Compara un HDD y un SSD (tiempo de acceso, ruido, calor, resistencia). ¿Qué es una celda de puerta flotante?**

| Característica | HDD | SSD |
|---|---|---|
| **Tiempo de acceso** | 5–12 ms: hay que mover el brazo y esperar a que gire el plato. | 0,02–0,1 ms: no tiene partes móviles. Es unas 100 veces más rápido. |
| **Ruido** | Se oyen el giro de los platos y el movimiento de las cabezas. | Silencioso. |
| **Calor y consumo** | Más consumo (6–10 W) por el motor. | Menos consumo en general. Los NVMe rápidos pueden calentarse y a veces llevan disipador. |
| **Resistencia a golpes** | Frágil: un golpe en funcionamiento puede hacer que la cabeza toque el plato. | Muy resistente: no tiene piezas mecánicas. |
| **Desgaste** | Mecánico (motor, cabezas). | Las celdas soportan un número limitado de escrituras (TBW). |
| **Precio por GB** | Más barato. | Más caro. |
| **Capacidad máxima** | Muy alta (más de 20 TB). | Alta, pero más cara a igual capacidad. |

**Celda de puerta flotante**

Es la celda básica de la memoria flash NAND. Se trata de un **transistor MOSFET con una puerta extra, la puerta flotante**, rodeada de aislante (óxido) por todas partes.

- Para **escribir**, se aplica una tensión alta y los electrones atraviesan el óxido por **efecto túnel**, quedando **atrapados** en la puerta flotante.
- La carga atrapada cambia la tensión con la que conduce el transistor. Leyendo esa tensión se sabe si guarda un 0 o un 1 (o varios bits, según el tipo de celda).
- Como el óxido aísla la puerta, la carga **se mantiene sin corriente**: por eso la memoria flash **no es volátil**.
- Cada escritura y borrado **desgasta el óxido**, y por eso las celdas tienen un número limitado de ciclos.

> Muchas memorias 3D NAND actuales usan una variante llamada *charge trap*, pero el principio es el mismo: atrapar carga para guardar bits.

---

## Ejercicio 6

**Explica la diferencia entre un SSD M.2 SATA y un M.2 NVMe. ¿Qué velocidad máxima aproximada tiene cada uno?**

**M.2** es solo el **formato físico** (la tarjeta y la ranura). Por la misma ranura pueden ir dos interfaces distintas:

| | M.2 SATA | M.2 NVMe |
|---|---|---|
| **Bus** | SATA III, el mismo que un SSD de 2,5" | PCI Express (normalmente x4), conectado casi directamente a la CPU |
| **Protocolo** | AHCI, pensado para discos mecánicos: 1 cola de 32 órdenes | NVMe, pensado para memoria flash: hasta 65 535 colas de 65 536 órdenes |
| **Muesca habitual** | B+M (dos muescas) | M (una muesca) |
| **Velocidad máxima** | **≈ 550–600 MB/s** (límite de SATA III, 6 Gb/s) | PCIe 3.0 x4: **≈ 3500 MB/s**<br>PCIe 4.0 x4: **≈ 7000 MB/s**<br>PCIe 5.0 x4: **≈ 14 000 MB/s** |

> Ojo: no todas las ranuras M.2 admiten los dos tipos. Hay que mirar en el manual de la placa si la ranura es SATA, PCIe o ambas.

---

## Ejercicio 7

**Ordena de mayor a menor durabilidad los tipos de celda SLC, MLC, TLC y QLC, y explica la relación entre bits por celda, precio y vida útil.**

De mayor a menor durabilidad: **SLC > MLC > TLC > QLC**

| Tipo | Bits por celda | Niveles de tensión | Ciclos aproximados (P/E) | Precio por GB |
|---|---|---|---|---|
| SLC (*Single*) | 1 | 2 | 50 000 – 100 000 | Muy alto |
| MLC (*Multi*) | 2 | 4 | 3000 – 10 000 | Alto |
| TLC (*Triple*) | 3 | 8 | 1000 – 3000 | Medio |
| QLC (*Quad*) | 4 | 16 | 100 – 1000 | Bajo |

**Relación**

- **Más bits por celda → más capacidad con el mismo silicio → más barato por GB.**
- Pero para guardar *n* bits la celda debe distinguir **2ⁿ niveles de carga**. Cuantos más niveles, más juntos están entre sí y más fácil es confundirlos. Eso obliga a escribir con más precisión, que es **más lento**, y hace que el desgaste del óxido provoque errores antes, así que la **vida útil es menor**.
- En resumen: a más bits por celda, **más barato y más capacidad, pero menos duración y menos velocidad de escritura**. SLC se usa en entornos profesionales, TLC es lo habitual en equipos domésticos y QLC se usa para mucha capacidad a bajo precio.

---

## Ejercicio 8

**Explica qué hace el comando TRIM, por qué alarga la vida del SSD y por qué nunca hay que desfragmentar un SSD.**

**Qué hace TRIM**

En un SSD no se puede escribir encima de datos antiguos: hay que **borrar antes**, y solo se puede borrar un **bloque entero** (muchas páginas a la vez).

Cuando se borra un archivo, el sistema operativo solo lo marca como libre en el sistema de archivos y **el SSD no se entera**. Para el disco, esas páginas siguen teniendo datos válidos.

**TRIM** es la orden con la que el sistema operativo **avisa al SSD de qué páginas ya no se usan**. Así el SSD puede borrarlas en segundo plano y tenerlas listas para la siguiente escritura.

En Windows se comprueba con:

```
fsutil behavior query DisableDeleteNotify
```

Un resultado de `0` significa que **TRIM está activado**.

**Por qué alarga la vida del SSD**

- Sin TRIM, cuando el SSD reorganiza sus bloques (recolección de basura) copia también datos que en realidad ya estaban borrados. Son **escrituras inútiles** que gastan ciclos de las celdas.
- Con TRIM, el SSD sabe qué datos son basura y no los copia. Hay **menos escrituras**, así que el disco **se desgasta menos y dura más**. Además, mantiene su **velocidad de escritura**.

**Por qué no hay que desfragmentar un SSD**

1. **No sirve de nada**: desfragmentar junta los trozos de un archivo para que el cabezal de un HDD no tenga que saltar. Un SSD no tiene cabezal y accede igual de rápido a cualquier posición.
2. **Ni siquiera es real**: el SSD reparte internamente los datos entre sus celdas (nivelación de desgaste), así que lo que el sistema ve "contiguo" no lo está físicamente.
3. **Lo desgasta**: desfragmentar implica mover y reescribir gigas de datos, lo que gasta ciclos de escritura sin ningún beneficio.

> Por eso, cuando Windows "optimiza" un SSD no lo desfragmenta: lanza un *retrim*, es decir, vuelve a enviar TRIM de todo el espacio libre.

---

## Ejercicio 9

**¿Qué diferencia hay entre PCI y PCI Express? ¿Se puede instalar una tarjeta x1 en una ranura x16? ¿Y una x16 en una x1? Explica por qué.**

| | PCI | PCI Express (PCIe) |
|---|---|---|
| **Tipo de bus** | **Paralelo**: 32 bits enviados a la vez | **Serie**, mediante carriles (*lanes*) |
| **Topología** | Bus **compartido**: todas las tarjetas se reparten el ancho de banda | Conexión **punto a punto**: cada ranura tiene sus propios carriles |
| **Comunicación** | Half-duplex | Full-duplex (envía y recibe a la vez) |
| **Velocidad** | 133 MB/s en total (33 MHz) | Por carril y sentido: 3.0 ≈ 1 GB/s, 4.0 ≈ 2 GB/s, 5.0 ≈ 4 GB/s |
| **Ranuras** | Un solo tamaño | x1, x4, x8, x16 (número de carriles) |
| **Estado** | Obsoleto | Estándar actual |

**¿Una tarjeta x1 en una ranura x16?** **Sí.** La tarjeta solo usa el primer carril y el resto de contactos de la ranura quedan libres. Funciona a velocidad x1, que es la que necesita.

**¿Una tarjeta x16 en una ranura x1?** **No**, físicamente no entra porque el conector de la tarjeta es más largo que la ranura.

- Excepción: algunas ranuras x1 son "abiertas" por el final. Ahí sí entraría, pero funcionaría a velocidad x1.
- También hay ranuras con tamaño físico x16 pero cableadas eléctricamente a x4. Hay que mirar el manual de la placa.

PCIe negocia automáticamente con la tarjeta el número de carriles que se usarán, y por eso estas combinaciones son compatibles.

---

## Ejercicio 10

**Compara memoria de vídeo compartida y dedicada, con ventajas e inconvenientes.**

| | Memoria compartida | Memoria dedicada (VRAM) |
|---|---|---|
| **Qué es** | La gráfica integrada usa una **parte de la RAM del sistema** como memoria de vídeo. | La tarjeta gráfica tiene **su propia memoria** (GDDR6, GDDR6X, GDDR7, HBM) en la misma placa. |
| **Ventajas** | Más barata (no hay chips extra).<br>Menos consumo y calor.<br>Ideal para portátiles y ofimática.<br>La cantidad puede ajustarse según las necesidades. | **Mucho más ancho de banda**: cientos de GB/s, hasta más de 1 TB/s.<br>No le quita RAM al sistema.<br>No compite con la CPU por el acceso a memoria.<br>Imprescindible para juegos, edición de vídeo, 3D e IA. |
| **Inconvenientes** | **Menos ancho de banda**: la RAM DDR es más lenta que la GDDR.<br>**Resta RAM** al sistema.<br>Compite con la CPU por el bus de memoria.<br>Rendimiento gráfico limitado. | Más cara.<br>Más consumo y calor.<br>La cantidad es fija: no se puede ampliar. |

---

## Ejercicio 11

**Explica las tres frecuencias de una GPU (base, game y boost) y la diferencia entre core clock y memory clock.**

**Las tres frecuencias**

- **Base clock**: frecuencia **mínima garantizada** con la que la GPU funciona a plena carga en condiciones normales.
- **Game clock**: frecuencia **típica esperada mientras se juega**. Es un término de **AMD**; NVIDIA no lo usa y solo indica base y boost.
- **Boost clock**: frecuencia **máxima** que la GPU puede alcanzar de forma automática y puntual si la temperatura, el consumo y el voltaje lo permiten. No está garantizada de forma sostenida.

Por tanto: **base ≤ game ≤ boost**. Con buena refrigeración la GPU pasará más tiempo cerca del boost.

**Core clock y memory clock**

- **Core clock**: frecuencia del **procesador gráfico** (los núcleos que hacen los cálculos). Las tres frecuencias anteriores se refieren a él. Se mide en MHz.
- **Memory clock**: frecuencia de la **memoria de vídeo (VRAM)**. Determina, junto con el ancho del bus, el **ancho de banda** de la memoria. En GDDR suele indicarse como velocidad efectiva por pin (por ejemplo, 20 Gbps), que es varias veces la frecuencia real del reloj.

```
Ancho de banda (GB/s) = velocidad efectiva (Gbps) × ancho de bus (bits) / 8
Ejemplo: 20 Gbps × 256 bits / 8 = 640 GB/s
```

---

## Ejercicio 12

**Explica qué papel juegan la API gráfica y el driver cuando un videojuego muestra una escena en pantalla. Cita dos API gráficas y su plataforma principal.**

El proceso es una cadena:

```
Videojuego → API gráfica → Driver → GPU → Monitor
```

1. **El videojuego** decide qué hay que dibujar: modelos 3D, texturas, luces, cámara.
2. **La API gráfica** es una **interfaz estándar** de funciones ("dibuja estos triángulos", "aplica esta textura"). Gracias a ella, el programador escribe el juego una vez **sin preocuparse de qué tarjeta gráfica concreta** tiene el usuario.
3. **El driver**, del fabricante de la GPU (NVIDIA, AMD, Intel), **traduce** las llamadas de la API a las instrucciones concretas que entiende **esa GPU**, compila los *shaders* y gestiona la VRAM. Por eso actualizar los drivers puede mejorar el rendimiento en juegos.
4. **La GPU** ejecuta esas instrucciones, genera la imagen (*frame*) en la VRAM y la envía por la salida de vídeo al monitor, decenas de veces por segundo (FPS).

**API gráficas**

| API | Plataforma principal |
|---|---|
| **DirectX** (Direct3D 12) | Windows y Xbox (Microsoft) |
| **Vulkan** | Multiplataforma: Windows, Linux, Android |
| **Metal** | macOS e iOS (Apple) |
| **OpenGL** | Multiplataforma (antecesora de Vulkan) |

---

## Ejercicio 13

**Compara las salidas de vídeo VGA, DVI, HDMI y DisplayPort.**

| | VGA | DVI | HDMI | DisplayPort |
|---|---|---|---|---|
| **Señal** | **Analógica** | Digital (DVI-D), analógica (DVI-A) o ambas (DVI-I) | Digital | Digital |
| **Conector** | DE-15 azul, 15 pines en 3 filas, con tornillos | Grande, blanco, con tornillos | Pequeño (también mini y micro) | Con pestaña de bloqueo (también mini DP y USB-C) |
| **Audio** | No | No (en general) | **Sí** | **Sí** |
| **Resolución máxima típica** | Hasta 2048×1536, pero la calidad se degrada | Single link: 1920×1200 a 60 Hz<br>Dual link: 2560×1600 a 60 Hz | 2.0: 4K a 60 Hz<br>2.1: 4K a 120 Hz, 8K a 60 Hz (48 Gbps) | 1.4: 8K a 60 Hz (con DSC)<br>2.0/2.1: hasta 80 Gbps |
| **Extras** | — | — | CEC (controlar dispositivos con un solo mando), ARC/eARC (audio de vuelta a la barra de sonido) | Varios monitores en cadena (MST), FreeSync/G-Sync, sale por USB-C |
| **Uso típico** | Proyectores y equipos antiguos | Monitores antiguos | **Televisores**, consolas, monitores | **Monitores de PC**, gaming, varias pantallas |
| **Estado** | Obsoleto | Obsoleto | Actual | Actual |

> VGA, al ser analógica, sufre pérdidas e interferencias con cables largos. Las demás transmiten la imagen digital sin pérdida.

---

## Ejercicio 14

**Explica las diferencias entre una CPU y una GPU (número y tipo de núcleos, uso de los transistores, tipo de tareas).**

| | CPU | GPU |
|---|---|---|
| **Número de núcleos** | **Pocos**: de 4 a 24 en equipos de sobremesa, algo más en servidores. | **Miles**: núcleos CUDA en NVIDIA, *stream processors* en AMD. |
| **Tipo de núcleos** | **Muy potentes y complejos**, con alta frecuencia. Cada uno ejecuta instrucciones complicadas y muy variadas. | **Sencillos y especializados**. Cada uno es menos potente, pero trabajan todos a la vez. |
| **Uso de los transistores** | Gran parte se dedica a **caché** y a **lógica de control**: predicción de saltos, ejecución fuera de orden. El objetivo es que **cada tarea termine cuanto antes** (baja latencia). | La mayoría se dedica a **unidades de cálculo** (ALU). Poca caché y poco control por núcleo. El objetivo es **hacer muchos cálculos a la vez** (alto rendimiento total). |
| **Tipo de tareas** | **Secuenciales y variadas**: sistema operativo, lógica de programas, ofimática, decisiones con muchas condiciones. | **Masivamente paralelas**, es decir, la misma operación sobre muchos datos: gráficos (cada píxel), IA, minería, simulaciones científicas, edición de vídeo. |

> Analogía: la CPU es un pequeño grupo de ingenieros que resuelve cualquier problema complejo. La GPU es un ejército de miles de operarios que hacen todos la misma operación sencilla a la vez.

---

## Ejercicio 15

**¿Para qué sirve una tarjeta RAID? ¿Qué ventajas ofrece?**

Una **tarjeta RAID** (RAID por hardware) es una tarjeta de expansión, normalmente PCIe, con su **propio procesador** que gestiona varios discos y los presenta al sistema operativo como si fueran **un solo disco**. Sirve para mejorar el **rendimiento**, la **tolerancia a fallos** o ambas cosas, según el nivel de RAID:

- RAID 0: reparte los datos entre discos. Es más rápido, pero no tiene redundancia.
- RAID 1: espejo. Los dos discos guardan lo mismo.
- RAID 5 y RAID 6: reparte datos y paridad. Aguanta el fallo de 1 o 2 discos, respectivamente.
- RAID 10: combina espejo y reparto de datos.

**Ventajas frente al RAID por software o el de la placa base**

- **No carga la CPU**: los cálculos de paridad los hace el procesador de la tarjeta.
- **Mayor rendimiento**, gracias a su **caché propia**, a menudo protegida con batería o condensador (BBU) para no perder datos si se va la luz.
- **Independiente del sistema operativo**: el SO solo ve un disco.
- Más **puertos** para conectar discos y soporte de niveles avanzados (RAID 5, 6, 50, 60).
- **Hot swap**: permite cambiar un disco averiado sin apagar y reconstruir el RAID automáticamente.

**Inconvenientes**: es cara y, si la tarjeta se estropea, a veces hace falta otra del mismo fabricante para recuperar los datos.

> Importante: **RAID no es una copia de seguridad**. Protege frente al fallo de un disco, pero no frente a un borrado accidental, un virus o un ransomware.

---

## Ejercicio 16 (práctica en el aula)

**En un equipo del aula, identifica el tipo de disco (HDD/SSD), su interfaz (SATA/M.2/NVMe), las ranuras de expansión libres y usadas, y la tarjeta gráfica (integrada o dedicada, y su VRAM). Documéntalo en una tabla.**

La respuesta depende del equipo de cada alumno. Esta es una **guía de corrección** con un ejemplo.

**Cómo obtener la información**

| Dato | Con el equipo encendido (Windows) | Con el equipo abierto |
|---|---|---|
| Tipo de disco | Administrador de tareas → Rendimiento → Disco (pone "SSD" o "HDD").<br>Optimizar unidades → columna "Tipo de medio".<br>CrystalDiskInfo. | HDD de 3,5" o 2,5" con cable SATA, SSD de 2,5" o tarjeta M.2 en la placa. |
| Interfaz | CrystalDiskInfo → campo "Interfaz" o "Modo de transferencia" (SATA/600, NVM Express, PCIe 3.0 x4…). | Cable SATA de datos, o tarjeta M.2 (mirar la muesca y la etiqueta: "NVMe" o "SATA"). |
| Ranuras de expansión | Manual o web de la placa (modelo en `msinfo32`). | Contar las ranuras PCIe x1 y x16 (y M.2) y anotar cuáles están ocupadas y con qué. |
| Tarjeta gráfica | `dxdiag` → pestaña Pantalla (nombre y "Memoria de pantalla"/VRAM).<br>Administrador de tareas → GPU.<br>GPU-Z. | Si el monitor va conectado a la placa base: integrada. Si va a una tarjeta en una ranura PCIe x16: dedicada. |

**Ejemplo de tabla**

| Componente | Dato | Cómo se ha comprobado |
|---|---|---|
| Tipo de disco | SSD | Administrador de tareas → Disco 0 (SSD) |
| Modelo y capacidad | Kingston NV2 500 GB | CrystalDiskInfo |
| Interfaz | M.2 NVMe (PCIe 4.0 x4) | CrystalDiskInfo → NVM Express |
| Ranuras PCIe x16 | 1 (libre) | Inspección visual |
| Ranuras PCIe x1 | 2 (1 usada por tarjeta Wi-Fi, 1 libre) | Inspección visual |
| Ranuras M.2 | 2 (1 usada por el SSD, 1 libre) | Inspección visual + manual de la placa |
| Tarjeta gráfica | Integrada: Intel UHD Graphics 730 | `dxdiag` / Administrador de tareas |
| VRAM | Compartida (usa la RAM del sistema; `dxdiag` muestra la memoria compartida) | `dxdiag` → Pantalla |

**Criterios para corregir**

- Los datos son coherentes entre sí. Por ejemplo, un SSD NVMe no puede ir por cable SATA.
- Indica cómo ha obtenido cada dato, con capturas o fotos.
- Distingue bien entre ranuras **libres y usadas**.
- En la gráfica dice si es **integrada o dedicada** y si la memoria es **compartida o VRAM dedicada**, con su cantidad.
