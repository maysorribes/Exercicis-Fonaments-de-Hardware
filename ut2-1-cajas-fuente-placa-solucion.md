# Soluciones · UT2.1 Cajas, fuente de alimentación y placa base

Fundamentos de Hardware · CFGS ASIR (1.º curso)

---

## Ejercicio 1

> Clasifica estos elementos en internos o externos y, dentro de cada grupo, indica su categoría: SSD M.2, teclado, tarjeta gráfica, impresora, fuente de alimentación, tarjeta SD, chipset, altavoces.

**Solución**

| Elemento | Interno / externo | Categoría |
| -------- | ----------------- | --------- |
| SSD M.2 | Interno | Almacenamiento |
| Tarjeta gráfica | Interno | Tarjeta controladora |
| Fuente de alimentación | Interno | Componente auxiliar |
| Chipset | Interno | Placa base |
| Teclado | Externo | Periférico de entrada |
| Impresora | Externo | Periférico de salida (si es multifunción con escáner, de entrada/salida) |
| Tarjeta SD | Externo | Almacenamiento |
| Altavoces | Externo | Periférico de salida |

---

## Ejercicio 2

> Explica por qué los ventiladores que extraen aire caliente de una caja deben situarse en posiciones altas y los que introducen aire fresco en posiciones bajas. ¿Por qué es importante canalizar bien los cables?

**Solución**

El aire caliente pesa menos que el frío y **tiende a subir** de forma natural (convección). Si los ventiladores de extracción están arriba y detrás, sacan el aire justo donde se acumula el calor; si los de entrada están delante y abajo, meten aire fresco por donde el aire frío tiende a quedarse. Así los ventiladores trabajan **a favor** del movimiento natural del aire y se crea un flujo continuo de delante-abajo a detrás-arriba. Si se colocaran al revés, lucharían contra la convección y el calor se quedaría atrapado en la parte superior de la caja.

Canalizar bien los cables es importante porque:

- Los cables sueltos **bloquean el paso del aire** y crean zonas donde el aire caliente se estanca.
- Acumulan **polvo**, que empeora la refrigeración y puede provocar averías.
- Facilitan el **mantenimiento**: es más fácil acceder a los componentes, limpiarlos o sustituirlos.

---

## Ejercicio 3

> ¿Qué es un servidor *blade* y qué ventajas tiene frente a un servidor tradicional?

**Solución**

Un servidor *blade* es un servidor compactado al tamaño de una tarjeta (una "cuchilla"), que contiene lo imprescindible: procesadores, memoria y controladores de red y de entrada/salida. Se inserta en un **chasis** junto a otros *blades*, y es ese chasis el que proporciona, de forma compartida, la alimentación, la refrigeración y las conexiones.

Ventajas frente a un servidor tradicional:

- **Ocupa mucho menos espacio**: caben muchos servidores en poco sitio del rack.
- **Consume menos**: fuentes de alimentación y ventiladores compartidos en lugar de unos por servidor.
- **Menos cableado**: las conexiones de red y alimentación las gestiona el chasis.
- **Mantenimiento más sencillo**: los *blades* se pueden sustituir en caliente (sin apagar el resto) y se gestionan de forma centralizada.

Por eso se usan sobre todo en centros de proceso de datos y granjas de servidores.

---

## Ejercicio 4

> Explica qué hace una fuente de alimentación (transformar, rectificar, filtrar y estabilizar). Después, observa la tabla de la fuente de 750 W del apartado 3.3: ¿qué salida puede entregar más potencia? ¿Qué componentes se alimentan de ella y por qué crees que es la más importante en un equipo actual?

**Solución**

La fuente convierte la corriente alterna del enchufe (230 V) en las tensiones continuas y bajas que necesita el ordenador. Lo hace en cuatro fases:

1. **Transformar**: reduce la tensión de la red a valores bajos.
2. **Rectificar**: convierte la corriente alterna (que cambia de sentido) en corriente continua (siempre en el mismo sentido), aunque todavía con "ondulaciones".
3. **Filtrar**: suaviza esas ondulaciones mediante condensadores para que la tensión sea casi plana.
4. **Estabilizar (regular)**: mantiene la tensión de salida constante aunque varíen la tensión de entrada o el consumo del equipo.

En la tabla de la fuente de 750 W, la salida que más potencia entrega es la de **+12 V**: 12 V × 62,5 A = **750 W**, es decir, toda la potencia de la fuente. Las de +3,3 V y +5 V juntas solo llegan a 100 W.

De la salida de +12 V se alimentan el **procesador** (conector EPS de 4 u 8 pines), la **tarjeta gráfica** (conectores PCIe), los motores de los discos duros y los ventiladores.

Es la más importante porque el procesador y la tarjeta gráfica son los componentes que **más consumen** en un equipo actual, y ambos se alimentan a 12 V. Las salidas de 3,3 V y 5 V se reservan para la electrónica de bajo consumo (parte de la placa base, USB, SSD).

---

## Ejercicio 5

> ¿Cuál es la diferencia entre una fuente modular, una semimodular y una no modular? ¿Qué ventaja aporta la modular?

**Solución**

| Tipo | Cables |
| ---- | ------ |
| **No modular** | Todos los cables van fijos a la fuente; los que no se usan quedan sueltos dentro de la caja |
| **Semimodular** | Los cables imprescindibles (placa base y CPU) son fijos, y el resto se conectan solo si hacen falta |
| **Modular** | Todos los cables se conectan y desconectan de la fuente según se necesiten |

La ventaja de la modular es que **solo se instalan los cables necesarios**: hay menos cables sueltos en la caja, lo que mejora el **flujo de aire**, facilita el montaje y el mantenimiento y deja el interior más ordenado. Además, un cable dañado se puede sustituir sin cambiar la fuente. Su inconveniente es que suele ser más cara.

---

## Ejercicio 6

> Un equipo tiene un consumo habitual de 300 W y un pico de 450 W. Con una fuente 80 PLUS Gold que rinde un 90 % al 50 % de carga, ¿qué potencia de fuente elegirías para trabajar en su punto de mayor eficiencia y cuánta energía consumiría de la red en uso normal?

**Solución**

**Potencia de la fuente.** La mejor eficiencia se alcanza al 50 % de carga, así que el consumo habitual (300 W) debe ser la mitad de la potencia de la fuente:

300 W ÷ 0,5 = **600 W**

Comprobamos que aguanta el pico: 450 W ÷ 600 W = 0,75 → **75 % de carga**, por debajo del 100 %. La fuente de **600 W** es válida (si no hay de 600 W, la de 650 W, el tamaño comercial más próximo).

**Consumo de la red en uso normal.** Con una eficiencia del 90 %, para entregar 300 W al equipo la fuente debe tomar del enchufe:

300 W ÷ 0,90 = **333,3 W**

Los 33,3 W de diferencia se pierden en forma de calor.

---

## Ejercicio 7

> Si una gráfica consume 120 W, ¿basta con la alimentación que proporciona la ranura PCIe? ¿Qué conector adicional necesitaría?

**Solución**

**No basta.** La ranura PCIe x16 proporciona como máximo **75 W**, y la gráfica necesita 120 W.

Necesita un **conector PCIe de 6 pines**, que aporta otros 75 W:

75 W (ranura) + 75 W (conector de 6 pines) = **150 W** ≥ 120 W

Con eso tiene suficiente, y además le queda margen.

---

## Ejercicio 8

> Explica la diferencia entre los sockets PGA, LGA y BGA. ¿Cuál de ellos no permite ampliar el procesador y por qué?

**Solución**

| Socket | Dónde están los pines | Ejemplo |
| ------ | --------------------- | ------- |
| **PGA** (*Pin Grid Array*) | En el **procesador**; encajan en agujeros del zócalo | AMD AM4 |
| **LGA** (*Land Grid Array*) | En el **zócalo**; el procesador solo tiene contactos planos | Intel LGA 1700, AMD AM5 |
| **BGA** (*Ball Grid Array*) | No hay zócalo: el procesador se **suelda** a la placa mediante pequeñas bolas | Portátiles, mini PC, consolas |

El **BGA** es el que no permite ampliar el procesador, porque está **soldado** a la placa: no se puede quitar para poner otro. A cambio, reduce el tamaño y el coste, por eso se usa mucho en portátiles.

---

## Ejercicio 9

> Explica qué es el chipset y describe la función del puente norte y del puente sur. ¿Por qué ha desaparecido el puente norte en los procesadores actuales?

**Solución**

El **chipset** es el conjunto de chips de la placa base que controla el flujo de datos entre el procesador, la memoria y el resto de componentes. Determina qué componentes se pueden conectar a la placa y sus limitaciones.

Tradicionalmente estaba formado por dos chips:

- **Puente norte** (*northbridge*): controlaba los componentes **de alta velocidad**: la comunicación del procesador con la memoria RAM y con la tarjeta gráfica. Estaba situado cerca del procesador.
- **Puente sur** (*southbridge*): controlaba los dispositivos **más lentos**: puertos USB, conectores SATA, ranuras PCIe x1, red, audio y la BIOS.

El puente norte ha desaparecido porque sus funciones (el controlador de memoria, las líneas PCIe para la gráfica y la propia gráfica integrada) se han **integrado dentro del procesador** (entre 2009 y 2011 en Intel). Así la comunicación entre el procesador y la memoria es más directa y rápida. Hoy en la placa solo queda un chip, heredero del puente sur: el **PCH** (*Platform Controller Hub*) en Intel o el **chipset** en AMD, conectado al procesador mediante el bus DMI (Intel) o PCIe (AMD).

---

## Ejercicio 10

> ¿Para qué sirve la pila CR2032 de la placa base? ¿Qué pasaría con la fecha y la hora si se agotara?

**Solución**

La pila CR2032 (de litio, 3 V) mantiene alimentados, con el ordenador apagado y desenchufado:

- La memoria **RAM CMOS**, donde se guarda la **configuración de la BIOS/UEFI**.
- El **reloj de tiempo real** (RTC), que lleva la fecha y la hora.

Si se agotara, cada vez que el equipo se quedara sin corriente:

- **La fecha y la hora se reiniciarían** a un valor por defecto (por ejemplo, la fecha de fabricación de la BIOS) y habría que volver a ajustarlas.
- **La configuración de la BIOS volvería a los valores de fábrica** (orden de arranque, etc.).
- Podrían aparecer avisos al arrancar (como *CMOS battery low* o *CMOS checksum error*) y errores de certificados al navegar por Internet, por la fecha incorrecta.

La solución es sencilla: sustituir la pila, que es barata y fácil de encontrar.

---

## Ejercicio 11

> Compara BIOS y UEFI: cita al menos tres diferencias (particiones, arranque, seguridad...).

**Solución**

| Característica | BIOS | UEFI |
| -------------- | ---- | ---- |
| **Tabla de particiones** | MBR: máximo 4 particiones primarias | GPT: muchas más particiones (128 en Windows) |
| **Tamaño máximo de disco** | 2 TB | Prácticamente ilimitado (hasta 9,4 ZB) |
| **Velocidad de arranque** | Más lenta: carga los controladores uno tras otro | Más rápida: los carga en paralelo |
| **Seguridad** | Sin protección en el arranque | **Secure Boot**: solo arranca software firmado y de confianza |
| **Interfaz** | Solo texto y teclado | Gráfica, admite ratón |
| **Arquitectura** | 16 bits | 32 o 64 bits |

---

## Ejercicio 12 (práctica en el aula)

> Abre un equipo del aula (apagado, desenchufado y con las precauciones antiestáticas) e identifica: la caja y su flujo de ventilación, la fuente de alimentación y sus conectores, el socket, las ranuras de RAM y de expansión, los conectores SATA/M.2, la pila CMOS y el chipset. Haz un esquema o fotografías anotadas.

**Solución**

La respuesta depende de cada equipo. Guía para identificar cada elemento:

| Elemento | Cómo reconocerlo |
| -------- | ---------------- |
| **Caja y flujo de aire** | Tipo de caja (mini-torre, semitorre...). Los ventiladores delanteros e inferiores meten aire y los traseros y superiores lo sacan; la flecha del lateral del ventilador indica el sentido |
| **Fuente de alimentación** | Caja metálica, normalmente abajo o arriba en la parte trasera. Su etiqueta indica la potencia. Conectores: ATX de 24 pines (placa), EPS de 4/8 pines (CPU), PCIe de 6/8 pines (gráfica), SATA y Molex |
| **Socket** | Debajo del disipador de la CPU. Su nombre suele estar serigrafiado en la placa (por ejemplo, LGA 1700) |
| **Ranuras de RAM** | Ranuras largas con pestañas en los extremos, junto al socket |
| **Ranuras de expansión** | Ranuras PCIe (x16 la más larga, para la gráfica; x1 las cortas) |
| **Conectores SATA / M.2** | SATA: conectores pequeños en forma de L, normalmente en el borde de la placa. M.2: ranura pequeña con un tornillo de sujeción, a veces bajo un disipador metálico |
| **Pila CMOS** | Pila plateada y redonda (CR2032), del tamaño de una moneda |
| **Chipset** | Chip cubierto por un disipador, normalmente en la parte inferior derecha de la placa |

Se valora que el esquema o las fotografías indiquen claramente cada elemento y que se hayan respetado las medidas de seguridad.

---

## Ejercicio 13

> Quieres montar un PC pequeño con una placa Mini-ITX. ¿Cabría en una caja ATX? ¿Y una placa ATX en una caja Mini-ITX? ¿Cuántas tarjetas de expansión podrías instalar como máximo en la Mini-ITX?

**Solución**

- **Placa Mini-ITX en caja ATX: sí cabe.** ATX, Micro-ATX y Mini-ITX comparten la posición de los agujeros de anclaje, así que una caja ATX admite las tres. Una placa pequeña siempre cabe en una caja grande.
- **Placa ATX en caja Mini-ITX: no cabe.** La placa ATX mide 305 × 244 mm y la Mini-ITX, 170 × 170 mm: la caja es demasiado pequeña. Una placa grande nunca cabe en una caja pequeña.
- **Tarjetas de expansión en la Mini-ITX: una sola**, porque solo tiene una ranura PCIe. Normalmente se usa para la tarjeta gráfica.

---

## Ejercicio 14

> ¿Qué diferencia hay entre un SSD M.2 SATA y uno M.2 NVMe? ¿Se distinguen a simple vista? ¿Cómo sabrías cuál admite la ranura M.2 de tu placa?

**Solución**

Los dos usan el mismo **conector M.2**, pero cambian el **bus** y el **protocolo**:

| | SSD M.2 SATA | SSD M.2 NVMe |
| - | ------------ | ------------ |
| **Bus** | SATA | PCIe |
| **Protocolo** | AHCI (pensado para discos mecánicos) | NVMe (pensado para memoria flash) |
| **Velocidad máxima** | Unos 550 MB/s | Desde unos 3500 MB/s (PCIe 3.0) hasta más de 12 000 MB/s (PCIe 5.0) |

**A simple vista casi no se distinguen.** A veces se reconocen por las muescas del conector (los SATA suelen tener dos y los NVMe, una), pero no es un método fiable: hay que consultar las especificaciones del SSD.

Para saber qué admite la ranura M.2 de la placa, hay que consultar el **manual** o la **web del fabricante**, que indican ranura por ranura si admite SATA, NVMe o ambos (y qué generación de PCIe).
