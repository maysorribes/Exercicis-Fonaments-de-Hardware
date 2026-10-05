<p style="font-size: 1.3em;"><strong>CFGS Administración de Sistemas Informáticos y en Red (1º curso)</strong></p>

Material elaborado para el módulo **Fundamentos de Hardware**

# UT2.1. Cajas, fuente de alimentación y placa base — SOLUCIÓN


## Ejercicio 1. Elementos internos y externos

**Clasifica estos elementos en internos o externos y, dentro de cada grupo, indica su categoría: SSD, teclado, tarjeta gráfica, impresora, fuente de alimentación, tarjeta SD, chipset, altavoces.**

| Elemento | Grupo | Categoría |
| -------- | ----- | --------- |
| SSD | Interno | Almacenamiento |
| Tarjeta gráfica | Interno | Tarjetas controladoras |
| Fuente de alimentación | Interno | Componentes auxiliares |
| Chipset | Interno | Placa base |
| Teclado | Externo | Periférico de entrada |
| Impresora | Externo | Periférico de salida |
| Altavoces | Externo | Periférico de salida |
| Tarjeta SD | Externo | Almacenamiento |

El SSD también puede ser externo (almacenamiento) cuando se conecta por USB, pero lo habitual es que vaya montado dentro del equipo.

## Ejercicio 2. Flujo de aire y cableado

**Explica por qué los ventiladores que extraen aire caliente de una caja deben situarse en posiciones altas y los que introducen aire fresco en posiciones bajas. ¿Por qué es importante canalizar bien los cables?**

Porque el aire caliente pesa menos que el frío y tiende a subir. Si los ventiladores de extracción están arriba y detrás, sacan el aire caliente justo donde se acumula. Si los de entrada están abajo y delante, meten aire fresco por la zona más fría.

Así se crea un circuito que acompaña el movimiento natural del aire: entra frío por abajo, pasa por los componentes, se calienta y sale por arriba.

Canalizar bien los cables es importante porque los cables sueltos se ponen en medio del recorrido del aire y lo frenan. Con los cables recogidos, el aire circula libre y el equipo se refrigera mejor. Además se acumula menos polvo y es más fácil montar y limpiar.

## Ejercicio 3. Servidor blade

**¿Qué es un servidor *blade* y qué ventajas tiene frente a un servidor tradicional?**

Un servidor blade es un servidor tradicional compactado al tamaño de una tarjeta. Cada blade lleva lo imprescindible: procesadores, memoria, controladores de red y adaptadores de entrada/salida. Las conexiones, la alimentación y la refrigeración no van en cada servidor, sino en el chasis donde se insertan, que las comparte entre todos.

Ventajas frente a un servidor tradicional:

- **Aprovecha mejor el espacio:** caben muchos servidores en un solo chasis.
- **Consume menos:** la alimentación y la refrigeración son compartidas en lugar de estar repetidas en cada equipo.
- **Mantenimiento más sencillo:** hay menos cableado y un blade se saca y se sustituye con facilidad.

Por eso se usan sobre todo en granjas de servidores y en centros de proceso de datos.

## Ejercicio 4. Funciones de la fuente de alimentación

**Explica qué hace una fuente de alimentación (transformar, rectificar, filtrar y estabilizar) y para qué se usan las salidas de 5 V y de 12 V.**

La fuente convierte la corriente alterna de 230 V del enchufe en las tensiones continuas y bajas que necesitan los componentes. Lo hace en cuatro fases:

1. **Transformar:** reduce la tensión de la red a valores bajos (12 V, 5 V, 3,3 V). Sigue siendo corriente alterna.
2. **Rectificar:** convierte la corriente alterna en continua, para que circule en un solo sentido. Todavía sale con ondulaciones.
3. **Filtrar:** suaviza esas ondulaciones con condensadores y deja una señal casi plana.
4. **Estabilizar:** mantiene la tensión de salida fija, aunque cambie la tensión de entrada o el consumo del equipo.

Uso de las salidas:

- **5 V:** circuitos electrónicos.
- **12 V:** motores, como los de los ventiladores y los discos duros.

La fuente también protege el equipo: lleva un interruptor y un fusible que se funde si hay un consumo excesivo o un cortocircuito.

## Ejercicio 5. Fuentes modulares, semimodulares y no modulares

**¿Cuál es la diferencia entre una fuente modular, una semimodular y una no modular? ¿Qué ventaja aporta la modular?**

La diferencia está en si los cables van fijos a la fuente o se pueden quitar.

| Tipo | Cables |
| ---- | ------ |
| No modular | Todos fijos: salen del interior de la fuente y no se pueden desconectar. |
| Semimodular | Los principales van fijos y el resto se conectan a conectores hembra según se necesiten. |
| Modular | Ninguno fijo: la fuente solo tiene conectores hembra y se enchufan los cables que hagan falta. |

La ventaja de la modular es que solo se montan los cables que se van a usar. Al no haber cables sobrantes dentro de la caja, el aire circula mejor, el montaje es más limpio y es más fácil cambiar un cable o un componente.

## Ejercicio 6. Cálculo de la potencia de la fuente

**Un equipo tiene un consumo habitual de 300 W y un pico de 450 W. Con una fuente 80 PLUS Gold que rinde un 90 % al 50 % de carga, ¿qué potencia de fuente elegirías para trabajar en su punto de mayor eficiencia y cuánta energía consumiría de la red en uso normal?**

Se elige una fuente de **600 W**, que en uso normal consume de la red unos **333 W**.

**1. Potencia de la fuente.** La mayor eficiencia se da al 50 % de carga, así que el consumo habitual debe ser la mitad de la potencia de la fuente:

300 W ÷ 0,5 = 600 W

**2. Comprobación del pico.** La fuente tiene que aguantar también el consumo máximo:

450 W ÷ 600 W = 0,75, es decir, un 75 % de carga

No llega al 100 %, así que la fuente de 600 W soporta el pico sin problema.

**3. Consumo de la red en uso normal.** Con un 90 % de eficiencia, de lo que entra por el enchufe solo llega al equipo el 90 %. Para entregar 300 W hay que tomar de la red:

300 W ÷ 0,90 = 333,3 W

De esos 333,3 W, 300 W llegan al equipo y los 33,3 W restantes se pierden en forma de calor.

## Ejercicio 7. Alimentación de la tarjeta gráfica

**Si una gráfica consume 120 W, ¿basta con la alimentación que proporciona la ranura PCIe? ¿Qué conector adicional necesitaría?**

No basta. La ranura PCIe solo puede dar hasta 75 W, y la gráfica necesita 120 W, así que faltan 45 W.

Necesita un conector **PCIe de 6 pines**, que llega directamente desde la fuente de alimentación. Ese conector aporta otros 75 W, de modo que entre la ranura y el conector la gráfica dispone de hasta 150 W, suficiente para sus 120 W.

## Ejercicio 8. Sockets PGA, LGA y BGA

**Explica la diferencia entre los sockets PGA, LGA y BGA. ¿Cuál de ellos no permite ampliar el procesador y por qué?**

La diferencia está en cómo se hace el contacto entre el procesador y la placa.

| Socket | Significado | Cómo conecta |
| ------ | ----------- | ------------ |
| PGA | Pin Grid Array | Los pines están en el procesador y encajan en los agujeros del zócalo. |
| LGA | Land Grid Array | Los pines están en el zócalo y tocan las superficies planas de contacto del procesador. |
| BGA | Ball Grid Array | En lugar de pines hay pequeñas bolas que se sueldan directamente a la placa. No hay zócalo. |

El **BGA** es el que no permite ampliar el procesador. Como va soldado a la placa, no se puede extraer para poner otro: habría que cambiar la placa entera. A cambio reduce el tamaño y el coste, y por eso se usa en chips de la placa y en portátiles.

## Ejercicio 9. Chipset, puente norte y puente sur

**Explica qué es el chipset y describe la función del puente norte y del puente sur. ¿Por qué ha desaparecido el puente norte en los procesadores actuales?**

El chipset es un conjunto de chips de la placa base que controla el flujo de datos entre el procesador, la memoria y los periféricos. También determina qué componentes se pueden conectar a la placa y con qué limitaciones. Tradicionalmente estaba formado por dos chips:

- **Puente norte (northbridge):** comunica la CPU con los componentes de alta velocidad, que son la memoria RAM y la tarjeta gráfica. Por eso está situado físicamente cerca del procesador.
- **Puente sur (southbridge):** comunica la CPU con los dispositivos más lentos: ranuras PCI y PCI Express x1, conectores SATA, puertos USB, red Ethernet y audio integrado.

El puente norte ha desaparecido como chip separado porque sus funciones se han integrado dentro del propio procesador, a partir de Intel Sandy Bridge (2011). Al estar el control de la memoria y de los gráficos dentro de la CPU, los datos recorren menos camino y todo el equipo funciona más rápido.

Hoy solo queda un chip, heredero del puente sur, unido al procesador por un bus de alta velocidad llamado DMI en Intel y UMI en AMD.

## Ejercicio 10. Pila CR2032

**¿Para qué sirve la pila CR2032 de la placa base? ¿Qué pasaría con la fecha y la hora si se agotara?**

La pila CR2032 alimenta la memoria RAM CMOS y el reloj de tiempo real (RTC) cuando el ordenador está apagado. Gracias a ella se conserva la configuración de la BIOS y el reloj sigue contando aunque el equipo esté desenchufado.

Si se agotara, el reloj se pararía cada vez que el equipo se quedara sin corriente. Al encenderlo, la fecha y la hora volverían a un valor de fábrica y habría que ponerlas en hora de nuevo. También se perdería la configuración de la BIOS, que volvería a los valores por defecto en cada arranque.

## Ejercicio 11. BIOS frente a UEFI

**Compara BIOS y UEFI: cita al menos tres diferencias (particiones, arranque, seguridad...).**

UEFI es el sucesor de la BIOS: hace el mismo trabajo de iniciar el hardware y dar paso al sistema operativo, pero sin sus limitaciones.

| Aspecto | BIOS | UEFI |
| ------- | ---- | ---- |
| Tabla de particiones | MBR, con entradas de 32 bits | GPT, con entradas de 64 bits |
| Número de particiones | Máximo 4 primarias | Muchas más |
| Tamaño máximo de disco | 2 TB | Hasta 9,4 ZB |
| Arranque | Carga módulos y controladores uno detrás de otro (secuencial), más lento | Los carga en paralelo, más rápido |
| Seguridad | Sin arranque seguro | Secure Boot: solo deja ejecutar controladores y servicios genuinos en el arranque |

## Ejercicio 12. Práctica en el aula

**Abre un equipo del aula (apagado, desenchufado y con las precauciones antiestáticas) e identifica: la caja y su flujo de ventilación, la fuente de alimentación y sus conectores, el socket, las ranuras de RAM y de expansión, los conectores SATA/M.2, la pila CMOS y el chipset. Haz un esquema o fotografías anotadas.**

La respuesta depende del equipo que se abra, así que esta tabla sirve de guía de lo que debe aparecer identificado en el esquema o en las fotografías.

Antes de abrir el equipo:

- Apagar el equipo y desenchufar el cable de corriente.
- Tocar una parte metálica de la caja o ponerse la pulsera antiestática.
- Retirar el panel lateral y hacer una foto general del interior.

| Elemento | Cómo reconocerlo | Qué debe anotarse |
| -------- | ---------------- | ----------------- |
| Caja | Chasis metálico que lo contiene todo | Tipo (minitorre, semitorre, gran torre) y material |
| Flujo de ventilación | Ventiladores delante, detrás y arriba | Cuáles meten aire y cuáles lo sacan, con flechas |
| Fuente de alimentación | Caja metálica con ventilador, de donde salen todos los cables | Potencia (W) de la etiqueta, certificación 80 PLUS y si es modular |
| Conectores de la fuente | Cables que salen de la fuente | ATX de 24 pines, CPU de 4 u 8 pines, PCIe de 6 u 8 pines, SATA y Molex |
| Socket | Debajo del disipador del procesador | Tipo (PGA, LGA o BGA) y modelo, serigrafiado en la placa |
| Ranuras de RAM | Ranuras largas con pestañas, junto al socket | Cuántas hay, cuántas están ocupadas y tipo de DDR |
| Ranuras de expansión | Ranuras paralelas en la parte baja de la placa | Cuántas PCI Express x16, x1 y PCI, y qué tarjetas llevan |
| Conectores SATA | Pequeños conectores en forma de L, en el borde de la placa | Cuántos hay y qué unidades tienen conectadas |
| Ranura M.2 | Ranura pequeña y plana con un tornillo al final | Si existe y si lleva un SSD instalado |
| Pila CMOS | Pila redonda plateada, tipo CR2032 | Dónde está situada |
| Chipset | Chip bajo un disipador pequeño, lejos del socket | Modelo, serigrafiado en la placa o en el manual |
