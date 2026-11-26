# Soluciones · UT2P4 Almacenamiento

Fundamentos de Hardware · CFGS ASIR (1.º curso)

> Las actividades 4, 5 y 6 se hacen sobre el ordenador de cada alumno, así que los números cambian en cada entrega. En ellas se resuelve un ejemplo completo y se indica qué hay que comprobar al corregir.
>
> Datos de fabricantes consultados en **noviembre de 2026**.

---

## Actividad 1 · Conectores de almacenamiento de la placa base

> Con las especificaciones de la placa (South Bridge: 1 conector IDE ATA133 para 2 dispositivos, 6 SATA 3 Gb/s, RAID 0/1/10; chip ITE IT8720: 1 conector de disquetera para 1 unidad), contesta:

**¿Cuántos discos duros IDE podemos conectar?**

**2.** Hay un solo conector IDE, pero cada cable IDE admite dos dispositivos: uno configurado como *maestro* y otro como *esclavo* (con los jumpers del disco).

**¿Cuántos discos SATA podemos conectar?**

**6.** SATA es punto a punto: un conector, un dispositivo.

**¿Podemos conectar una disquetera? ¿Y dos disqueteras?**

**Una sí, dos no.** El conector de disquetera del chip ITE IT8720 solo admite *una* unidad. (Los cables de disquetera antiguos tenían dos conectores, pero esta placa solo da soporte a una.)

**En total, ¿cuántos discos duros internos (sin contar la disquetera) podemos conectar?**

**8** = 2 IDE + 6 SATA.

**Si ya tenemos conectados 2 discos duros SATA, ¿cuántos dispositivos de almacenamiento óptico podemos conectar como máximo?**

**6.** Quedan libres 4 conectores SATA (6 − 2) y los 2 dispositivos del conector IDE. Las unidades ópticas (CD, DVD, Blu-ray) existen tanto en SATA como en IDE, así que podemos ocupar todos los huecos libres: 4 + 2 = 6.

**Compara con una placa base actual (con ranuras M.2): ¿qué conectores han desaparecido y cuáles han aparecido?**

Ejemplo: **ASUS TUF GAMING B850-PLUS WIFI** (AM5, 2025).

| | Placa del ejercicio (≈ 2009) | ASUS TUF GAMING B850-PLUS WIFI |
| --- | --- | --- |
| IDE (PATA) | 1 conector (2 dispositivos) | **Desaparece** |
| Disquetera | 1 conector | **Desaparece** |
| SATA | 6 × SATA II (3 Gb/s) | 4 × SATA III (6 Gb/s) |
| M.2 | No tiene | **3 ranuras M.2 (Key M)**: 1 × PCIe 5.0 x4 (desde la CPU) y 2 × PCIe 4.0 x4 |
| RAID | SATA RAID 0, 1, 10 | RAID 0, 1, 5, 10 (AMD RAIDXpert2), también con discos NVMe |

Conclusiones que deberían aparecer:

- **Desaparecen** IDE y la disquetera: tecnologías obsoletas.
- **Baja el número de puertos SATA** (de 6 a 4), pero pasan a 6 Gb/s. Hoy se usan sobre todo para HDD de gran capacidad o unidades ópticas.
- **Aparecen las ranuras M.2 NVMe**, conectadas directamente a líneas PCIe. Son mucho más rápidas (PCIe 5.0 x4 ≈ 15,7 GB/s frente a los 600 MB/s de SATA III) y no necesitan cables de datos ni de alimentación.
- Algunas ranuras **comparten ancho de banda** con otros conectores. En esta placa, al usar la M.2_3 se desactiva la ranura PCIe x16 (G4) que sale del chipset. Es un detalle que conviene que mencionen.

---

## Actividad 2 · Fiabilidad de los SSD

> Para valorar la fiabilidad: TBW, MTBF, años de garantía y DWPD = TBW / (capacidad en TB × 365 × años de garantía).

El DWPD indica cuántas veces se puede escribir **el disco entero cada día** durante la garantía sin superar el TBW. Sirve para comparar discos de distinta capacidad: un TBW mayor en un disco más grande no significa necesariamente que sea más resistente.

### 2.1 Corsair MP600 1 TB vs Samsung 960 PRO 1 TB

| Disco | Capacidad | TBW | MTBF | Garantía | DWPD | Razonamiento |
| --- | --- | --- | --- | --- | --- | --- |
| Corsair Force MP600 1TB (PCIe 4.0) | 1 TB | 1.800 TB | 1.700.000 h | 5 años | 1.800 / (1 × 365 × 5) = **0,99** | Más del doble de TBW con la misma capacidad y garantía, y mayor MTBF |
| Samsung 960 PRO 1TB (PCIe 3.0) | 1 TB | 800 TB | 1.500.000 h | 5 años | 800 / (1 × 365 × 5) = **0,44** | Misma garantía, pero menos TBW y menos MTBF |

**Es más fiable el Corsair MP600 1 TB.** Admite escribir prácticamente el disco entero cada día durante 5 años (≈ 1 DWPD), frente a menos de la mitad en el 960 PRO. También tiene más MTBF.

### 2.2 Samsung 960 PRO 512 GB, 1 TB y 2 TB

| Disco | Capacidad | TBW | MTBF | Garantía | DWPD | Orden |
| --- | --- | --- | --- | --- | --- | --- |
| 960 PRO 1TB | 1 TB | 800 TB | 1.500.000 h | 5 años | 800 / (1 × 1.825) = **0,438** | 1.º |
| 960 PRO 512GB | 0,512 TB | 400 TB | 1.500.000 h | 5 años | 400 / (0,512 × 1.825) = **0,428** | 2.º |
| 960 PRO 2TB | 2 TB | 1.200 TB | 1.500.000 h | 5 años | 1.200 / (2 × 1.825) = **0,329** | 3.º |

Razonamiento:

- **Empatan en MTBF (1,5 millones de horas) y en garantía (5 años)**, así que el criterio de desempate es el **DWPD**.
- El de 1 TB y el de 512 GB están casi igualados (0,44 y 0,43): el de 1 TB tiene exactamente el doble de TBW, pero un poco más del doble de capacidad. Queda por delante el de 1 TB por muy poco.
- El de 2 TB tiene el mayor TBW en valor absoluto (1.200 TB), pero no el triple que el de 1 TB, aunque su capacidad sí es el doble. Proporcionalmente aguanta menos escrituras: **es el menos fiable**.

> Al corregir: si un alumno ordena por TBW absoluto (2 TB > 1 TB > 512 GB) sin calcular el DWPD, el razonamiento está incompleto. Si se usa "500 GB" en vez de 512 GB, el DWPD sale 0,438 y empata con el de 1 TB. Se admite siempre que expliquen el criterio de desempate.

---

## Actividad 3 · Características de un disco a partir de su nombre

| Nombre | Información que se puede deducir |
| --- | --- |
| **Seagate BarraCuda 3.5" 2TB SATA 3** | Fabricante Seagate, gama **BarraCuda** (doméstica, para sobremesa). **3,5"** → disco **mecánico (HDD)** de ordenador de sobremesa. **2 TB** de capacidad. Interfaz **SATA III (6 Gb/s, ≈ 600 MB/s teóricos**, muy por encima de lo que da un HDD). No indica rpm ni caché. |
| **WD Red Plus 4TB 3.5" 5400 RPM 128MB caché SATA 6 Gb/s CMR** | Western Digital, gama **Red** → pensado para **NAS** (funcionamiento 24/7, varios discos juntos). HDD de **3,5"**, **4 TB**, **5.400 rpm** (más silencioso y de menor consumo que uno de 7.200 rpm, pero algo más lento), **128 MB de caché** (búfer), **SATA III**. **CMR**: grabación magnética convencional, con pistas que no se solapan (no SMR). Rinde mejor en escrituras continuas y en RAID; por eso la gama "Plus" lo especifica. |
| **WD Blue SN550 SSD 1TB NVMe M.2 PCIe Gen 3** | WD gama **Blue** (uso general, gama media). **SN** = serie NVMe de WD. **SSD** de **1 TB**, formato **M.2** (el tamaño no aparece, normalmente 2280), protocolo **NVMe** sobre **PCIe 3.0** (en M.2 suele ser x4 → hasta ≈ 3,9 GB/s teóricos). Necesita una ranura M.2 Key M con soporte PCIe/NVMe. |
| **SanDisk SSD Plus 1TB SATA III** | SanDisk (marca de WD), gama **Plus** (de entrada). **SSD** de **1 TB** con interfaz **SATA III** → máximo teórico ≈ 600 MB/s, protocolo AHCI. Como no dice M.2, será de **2,5"** con conectores SATA de datos y alimentación. |
| **Western Digital Black SN750 NVMe 1TB SSD M.2 PCI Express 3.0** | WD gama **Black** → alto rendimiento / *gaming*. SSD **NVMe** de **1 TB** en **M.2**, **PCIe 3.0** (x4 → ≈ 3,9 GB/s teóricos). Más rápido que el SN550 de la misma generación por ser de gama superior. |
| **WD Black SN850 1TB SSD NVMe M.2 PCIe 4.0 sin Disipador Térmico** | WD Black, SSD **NVMe** de **1 TB**, **M.2**, **PCIe 4.0** (x4 → ≈ 7,9 GB/s teóricos, el doble que PCIe 3.0). **Sin disipador**: más delgado, para portátiles o para placas que ya tienen disipador M.2 propio. A estas velocidades se calienta y puede bajar el rendimiento si no se refrigera (*thermal throttling*). En una placa con PCIe 3.0 funciona, pero limitado a esa velocidad. |
| **Crucial T705 2TB SSD NVMe M.2 PCIe Gen5 con disipador** | Crucial (Micron), SSD **NVMe** de **2 TB**, **M.2**, **PCIe 5.0** (x4 → ≈ 15,8 GB/s teóricos). **Con disipador** porque a estas velocidades genera mucho calor. Para aprovecharlo hace falta una placa con ranura M.2 PCIe 5.0 (por ejemplo, AM5 B850/X870 o Intel Z790/Z890). Hay que comprobar también que el disipador cabe junto a la tarjeta gráfica. |

Velocidades teóricas de referencia por línea PCIe: 3.0 ≈ 0,985 GB/s · 4.0 ≈ 1,97 GB/s · 5.0 ≈ 3,94 GB/s (× 4 líneas en M.2).

---

## Actividad 4 · Vida restante del SSD con CrystalDiskInfo

> Cada alumno tiene sus propios datos. Ejemplo resuelto con valores habituales de un equipo de aula.

Datos leídos en CrystalDiskInfo (ejemplo):

| Dato | Valor |
| --- | --- |
| Modelo | SSD NVMe de 500 GB |
| Estado de salud | Bueno (**92 %**) |
| Horas de encendido | **9.000 h** |
| Total de escrituras del host | **18 TB** (18.000 GB) |
| TBW del fabricante (ficha técnica) | **300 TB** |

Días de uso = 9.000 ÷ 24 = **375 días**.

**Método a) Por el estado de salud**

- Vida consumida = 100 − 92 = 8 %
- Días restantes ≈ 375 × (92 ÷ 8) = 375 × 11,5 = **4.312 días ≈ 11,8 años**

**Método b) Por las escrituras**

- Ritmo de escritura = 18 TB ÷ 375 días = 0,048 TB/día
- TB que quedan = 300 − 18 = 282 TB
- Días restantes ≈ 282 ÷ 0,048 = **5.875 días ≈ 16 años**

**Comparación:** los dos métodos dan resultados distintos. El método a se basa en el indicador de desgaste que calcula el propio disco y el b, en el TBW que garantiza el fabricante. Lo prudente es quedarse con el **valor menor**. En cualquier caso, son estimaciones: el disco puede fallar antes por otros motivos (controladora, temperatura, cortes de luz) y normalmente aguanta más allá del TBW.

Al corregir, comprobar que:

- La captura muestra **salud, horas de encendido y total de escrituras**, y que esos datos son los que aparecen en los cálculos.
- El TBW procede de la **ficha técnica de su modelo** (no inventado).
- Si el disco marca **100 %**, han usado el método b, ya que en el a se dividiría por 0.
- Si el disco es un **HDD**, CrystalDiskInfo no muestra el porcentaje de salud ni el TBW. En ese caso deberían indicarlo y razonar con los atributos SMART (sectores reasignados, pendientes, etc.).

---

## Actividad 5 · Comprobar TRIM

Comando (en CMD como administrador):

```
fsutil behavior query DisableDeleteNotify
```

Salida habitual en Windows 11:

```
NTFS DisableDeleteNotify = 0  (Disabled)
ReFS DisableDeleteNotify = 0  (Disabled)
```

- **0 → TRIM activado.** Lo que está "Disabled" es *DisableDeleteNotify* ("desactivar el aviso de borrado"). Es una doble negación: si no se desactiva el aviso, Windows sí avisa al SSD de los bloques borrados, y eso es TRIM.
- **1 → TRIM desactivado.** Se activaría con `fsutil behavior set DisableDeleteNotify 0`. En el aula no se debe cambiar sin permiso.
- Si aparece "*no está configurado actualmente*" en ReFS, es normal: el equipo no usa ese sistema de archivos.

Lo esperado en la entrega: la captura del comando y una frase indicando si TRIM está activo (en los equipos del aula, **sí**).

---

## Actividad 6 · Optimizar unidades

En la captura de **Optimizar unidades** se debe ver:

- **Tipo de medio:** *Unidad de estado sólido* (SSD) o *Unidad de disco duro* (HDD).
- **Última ejecución:** una fecha reciente (de la última semana si la optimización programada funciona).
- **Estado actual:** *Correcto* (o *Requiere optimización*, si llevaba tiempo sin ejecutarse).

**¿Cada cuánto se ejecuta la optimización programada?**

Por defecto, **semanalmente**. Se ve en el apartado *Optimización programada → Frecuencia: Semanal*, y se puede cambiar en *Cambiar configuración*.

**¿Qué hace Windows al "optimizar" un SSD y en qué se diferencia de desfragmentar un HDD?**

- **En un SSD**, *optimizar* = **enviar TRIM** (*retrim*) de todo el espacio libre de la unidad. Así el SSD sabe qué bloques ya no contienen datos válidos, los borra internamente cuando le conviene (recolección de basura) y luego escribe más rápido. **No mueve archivos.**
- **En un HDD**, *optimizar* = **desfragmentar**: junta en posiciones contiguas los trozos de cada archivo para que el cabezal no tenga que saltar por el plato. Así se reducen los tiempos de búsqueda.
- Desfragmentar un SSD **no tiene sentido**. Como no tiene piezas móviles, el tiempo de acceso es el mismo esté donde esté el dato, y mover archivos solo gasta ciclos de escritura de las celdas. Por eso Windows distingue el tipo de medio y aplica a cada uno su operación.
