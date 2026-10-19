# Soluciones · UT2P3 Procesadores actuales

Fundamentos de Hardware · CFGS ASIR (1.º curso)

> Las partes que dependen de cada grupo (portada, índice, reparto del trabajo, debate y conclusiones) no tienen una solución única. Aquí se indican los datos correctos con los que comparar y los argumentos que deberían aparecer.
>
> Datos actualizados a **octubre de 2026**. En los chips de móvil, Apple y Qualcomm no publican todas las cifras (frecuencias exactas, consumo). Cuando un dato procede de pruebas o filtraciones y no del fabricante, se indica.

---

## Ejercicio 1 · Tabla de cada procesador

> Recopilar en una tabla la información de cada procesador y, después de la tabla, comentar lo más destacable.

### 1.1 Apple A20 Pro

| Especificaciones | Apple A20 Pro |
| ---------------- | ------------- |
| Tipo | SoC para móvil (iPhone 18 Pro, 18 Pro Max y iPhone Duo) |
| Presentación | Septiembre de 2026 |
| Arquitectura | ARMv9 (diseño propio de Apple con licencia de arquitectura ARM) |
| Proceso de fabricación | 2 nm (TSMC N2) |
| Núcleos CPU | 6 (2 de alto rendimiento "super cores" + 4 de eficiencia) |
| Hilos | 6 |
| Frecuencia máxima | ≈ 4,9 GHz en los núcleos de rendimiento (dato de Geekbench, Apple no lo publica) |
| GPU | Apple, 7 núcleos, con trazado de rayos por hardware y aceleradores neuronales |
| NPU | Neural Engine de 32 núcleos (2 × 16) |
| Memoria | 12 GB, montada en el mismo encapsulado, junto al chip |
| Consumo | No publicado (del orden de pocos vatios) |
| Rendimiento orientativo | Geekbench 6: ≈ 4.700 mononúcleo / ≈ 12.500 multinúcleo |

**Comentarios de lo más destacable**

- Lo más destacable es su **rendimiento por núcleo**: en mononúcleo supera a cualquier otro chip de móvil y a muchos procesadores de sobremesa, con solo 6 núcleos y un consumo muy bajo.
- Es un **SoC**: CPU, GPU, NPU, controlador de memoria y la propia RAM van en un único encapsulado. Por eso no se puede ampliar ni sustituir nada.
- Sacará el mejor rendimiento en **tareas de usuario del día a día, fotografía y vídeo, juegos de móvil e IA local** (modelos de lenguaje ejecutados en el propio teléfono).
- Hay que tener en cuenta que **no se compra por separado**: solo existe dentro de un iPhone y solo ejecuta iOS. Para un informático, no sirve como equipo de trabajo principal.

---

### 1.2 Qualcomm Snapdragon 8 Elite Gen 6

| Especificaciones | Snapdragon 8 Elite Gen 6 |
| ---------------- | ------------------------ |
| Tipo | SoC para móvil Android (Xiaomi, OnePlus, Honor, Motorola…) |
| Presentación | Septiembre de 2026 (Snapdragon Summit) |
| Arquitectura | ARMv9, núcleos Oryon de diseño propio de Qualcomm |
| Proceso de fabricación | 2 nm (TSMC) |
| Núcleos CPU | 8 (2 Prime + 6 Performance) |
| Hilos | 8 |
| Frecuencia máxima | 5,0 GHz (Prime) / 4,0 GHz (Performance) |
| Caché CPU | 16 MB |
| GPU | Adreno, con trazado de rayos por hardware |
| NPU | Hexagon |
| Memoria | LPDDR5X o LPDDR6, hasta 24 GB |
| Almacenamiento | UFS 5.0 |
| Conectividad integrada | Módem 5G X105 (con conexión por satélite), Wi-Fi (FastConnect 8800), Bluetooth 6.0 |
| Variante superior | Snapdragon 8 Elite **Extreme** Gen 6 (más memoria para la GPU y más IA) |

**Comentarios de lo más destacable**

- Lo más destacable es que llega a **5 GHz en un móvil** y que **integra el módem 5G** en el propio chip, algo que el A20 Pro no hace (Apple usa un módem aparte).
- Tiene **más núcleos que el A20 Pro** (8 frente a 6). En multinúcleo se queda algo por detrás, y en mononúcleo bastante más.
- Sacará el mejor rendimiento en **juegos de móvil** (GPU Adreno muy potente), **IA local** y conectividad.
- Hay que tener en cuenta que, igual que el A20 Pro, **no se compra suelto**: va dentro del móvil del fabricante que lo elija. Su rendimiento real depende mucho de la refrigeración de cada teléfono.

---

### 1.3 Intel Core Ultra 7 270K Plus

| Especificaciones | Core Ultra 7 270K Plus |
| ---------------- | ---------------------- |
| Tipo | CPU de sobremesa (Arrow Lake Refresh) |
| Lanzamiento | Marzo de 2026 |
| Arquitectura | x86-64 (núcleos Lion Cove P y Skymont E) |
| Proceso de fabricación | TSMC N3B (tile de cómputo), diseño de chiplets (tiles) |
| Núcleos | 24 (8 P-cores + 16 E-cores) |
| Hilos | 24 (sin Hyper-Threading) |
| Frecuencia turbo máxima | 5,5 GHz (P) / 4,7 GHz (E) |
| Caché | 40 MB L2 + 36 MB L3 (76 MB en total) |
| Potencia | 125 W base / 250 W turbo máximo |
| Memoria | DDR5-7200 (JEDEC), doble canal |
| Socket | LGA1851 (placas serie 800) |
| GPU integrada | Sí, Intel Graphics (Xe) |
| NPU | Sí, integrada (unos 13 TOPS) |
| Multiplicador desbloqueado | Sí (sufijo **K**) |
| Precio de lanzamiento | 299 $ |

**Comentarios de lo más destacable**

- Lo más destacable son sus **24 núcleos por menos de 300 $**. En multinúcleo iguala o supera al Core Ultra 9 285K, que costaba casi el doble.
- **Desaparece el Hyper-Threading**: tiene tantos hilos como núcleos. Intel compensa con muchos E-cores.
- Sacará el mejor rendimiento en **tareas multinúcleo**: compilar, virtualizar varias máquinas, comprimir, renderizar o codificar vídeo.
- Hay que tener en cuenta que al instalar este procesador:
  - necesita una **placa LGA1851** (serie 800), y la siguiente generación (Nova Lake) cambia de socket, así que **no hay actualización futura** en esa placa;
  - consume hasta **250 W**, así que pide una **refrigeración líquida o un disipador de gama alta** y una fuente adecuada;
  - en juegos es bueno, pero queda por detrás de los AMD X3D.

---

### 1.4 AMD Ryzen 7 9850X3D

| Especificaciones | Ryzen 7 9850X3D |
| ---------------- | --------------- |
| Tipo | CPU de sobremesa (Zen 5 con 3D V-Cache) |
| Lanzamiento | Enero de 2026 |
| Arquitectura | x86-64, Zen 5 |
| Proceso de fabricación | TSMC N4P (núcleos) + N6 (chip de E/S) |
| Núcleos | 8 |
| Hilos | 16 (SMT) |
| Frecuencia | 4,7 GHz base / 5,6 GHz turbo |
| Caché | 8 MB L2 + **96 MB L3** (32 MB + 64 MB de 3D V-Cache) |
| TDP | 120 W |
| Memoria | DDR5-5600 (JEDEC), doble canal |
| Socket | AM5 |
| GPU integrada | Sí, Radeon básica (2 CU) |
| NPU | No |
| Multiplicador desbloqueado | Sí |
| Precio de lanzamiento | 499 $ |

**Comentarios de lo más destacable**

- Lo más destacable son sus **96 MB de caché L3**. La caché extra (3D V-Cache) va **apilada en vertical** bajo los núcleos, y eso lo convierte en el **procesador más rápido para juegos** del momento.
- Es igual que el 9800X3D, pero con **400 MHz más de turbo**. La mejora en juegos es pequeña.
- Sacará el mejor rendimiento en **juegos** y en programas que trabajan con muchos datos repetidos (simulación, algunas bases de datos).
- Hay que tener en cuenta que al instalar este procesador:
  - usa **socket AM5**, que AMD mantiene también para Zen 6, así que la placa tiene **recorrido de actualización**;
  - solo tiene **8 núcleos**: en multinúcleo puro rinde menos que el Intel de 24 núcleos, y cuesta más;
  - su GPU integrada sirve solo para tener imagen, no para jugar.

---

### 1.5 Comparativa

> Comparación a 4 columnas sobre lo más destacable, con una columna para el ganador.

| Comparativa | A20 Pro | Snapdragon 8 Elite Gen 6 | Core Ultra 7 270K Plus | Ryzen 7 9850X3D | Ganador |
| ----------- | ------- | ------------------------ | ---------------------- | --------------- | ------- |
| Tipo | SoC móvil | SoC móvil | CPU sobremesa | CPU sobremesa | — |
| Arquitectura | ARMv9 | ARMv9 | x86-64 | x86-64 | — |
| Proceso | 2 nm | 2 nm | 3 nm (N3B) | 4 nm (N4P) | A20 Pro / Snapdragon |
| Núcleos | 6 | 8 | 24 | 8 | **Core Ultra 7 270K Plus** |
| Hilos | 6 | 8 | 24 | 16 | **Core Ultra 7 270K Plus** |
| Frecuencia máxima | ≈ 4,9 GHz | 5,0 GHz | 5,5 GHz | 5,6 GHz | **Ryzen 7 9850X3D** |
| Caché L3 / mayor caché | No publicada (SLC compartida) | 16 MB (CPU) | 36 MB | 96 MB | **Ryzen 7 9850X3D** |
| Memoria | 12 GB en el encapsulado | LPDDR5X / LPDDR6 (hasta 24 GB) | DDR5-7200 | DDR5-5600 | Core Ultra (velocidad) |
| Consumo | Pocos W | Pocos W | 125-250 W | 120 W | **A20 Pro / Snapdragon** |
| NPU (IA) | 32 núcleos | Hexagon | Sí, básica | No | **A20 Pro / Snapdragon** |
| Módem 5G integrado | No | Sí | No | No | **Snapdragon** |
| Rendimiento mononúcleo | Muy alto | Alto | Muy alto | Muy alto | **A20 Pro** (para su consumo) |
| Rendimiento multinúcleo | Medio | Medio | Muy alto | Alto | **Core Ultra 7 270K Plus** |
| Juegos | Móvil | Móvil | Muy bueno | El mejor | **Ryzen 7 9850X3D** |
| Ampliable / sustituible | No | No | Sí | Sí | Intel / AMD |
| Plataforma con futuro | — | — | No (cambia socket) | Sí (AM5) | **Ryzen 7 9850X3D** |
| Precio | No se vende suelto | No se vende suelto | 299 $ | 499 $ | **Core Ultra 7 270K Plus** |

**Conclusión de la comparativa**

No hay un ganador absoluto porque se comparan **dos móviles con dos de sobremesa**:

- Entre los **móviles**, el **A20 Pro** gana en rendimiento de CPU y GPU, y el **Snapdragon** gana en número de núcleos, frecuencia y conectividad (módem integrado).
- Entre los **de sobremesa**, el **Core Ultra 7 270K Plus** gana en multinúcleo y precio, y el **Ryzen 7 9850X3D** gana en juegos y en plataforma (AM5).
- Los chips ARM de móvil ganan claramente en **eficiencia** (rendimiento por vatio).

---

## Ejercicio 2 · Debate

> Cada grupo defiende que su procesador es el mejor para las tareas de un informático; los demás le indican las contras.

**Solución**

No hay una respuesta única. Se valora que los argumentos se apoyen en los datos del ejercicio 1. Estos son los que deberían salir:

| Procesador | A favor | En contra |
| ---------- | ------- | --------- |
| **A20 Pro** | El mejor mononúcleo; muy eficiente; IA local potente; trabaja muchas horas con batería. | Solo en iPhone e iOS; no se puede virtualizar ni montar un servidor; no es ampliable; 6 núcleos. |
| **Snapdragon 8 Elite Gen 6** | 8 núcleos a 5 GHz; módem 5G y Wi-Fi integrados; está en muchas marcas; Android es más abierto (terminal, root, depuración). | Solo en móviles; menor rendimiento por núcleo que Apple; el rendimiento depende de la refrigeración del móvil. |
| **Core Ultra 7 270K Plus** | 24 núcleos: ideal para **compilar, virtualizar varias máquinas, contenedores** y codificar; NPU integrada; DDR5-7200; el más barato de los de sobremesa. | Sin Hyper-Threading; hasta 250 W de consumo y mucho calor; socket LGA1851 sin futuro; por detrás en juegos. |
| **Ryzen 7 9850X3D** | El mejor en juegos; 96 MB de L3; 16 hilos; AM5 permite actualizar a Zen 6 sin cambiar placa; consume menos que el Intel a plena carga (120 W). | Solo 8 núcleos; más caro; no tiene NPU; en virtualización y compilación pesada rinde menos que el Intel. |

**Conclusión esperada:** para las **tareas de un informático** (virtualización, compilación, servidores de pruebas, varias máquinas virtuales abiertas), el procesador más adecuado es uno **de sobremesa x86**. Por número de núcleos y precio, el mejor es el **Core Ultra 7 270K Plus**. Si se valora poder actualizar en el futuro, o el equipo también se usa para jugar, el **Ryzen 7 9850X3D** es una buena alternativa. Los dos de móvil quedan descartados como equipo de trabajo principal.

---

## Ejercicio 3 · Futuro

> Para cada familia de procesadores, buscar las nuevas generaciones que se están fabricando y cómo mejorarán a los actuales. Si es posible, hacer la primera tabla.

**Solución**

Ninguna de estas generaciones está a la venta todavía (octubre de 2026). Los datos son **anuncios parciales o filtraciones** y pueden cambiar.

| Familia | Próxima generación | Fecha prevista | Mejoras esperadas |
| ------- | ------------------ | -------------- | ----------------- |
| Apple | **A21 / A21 Pro** (iPhone de 2027) | Septiembre de 2027 | Proceso 2 nm mejorado (TSMC N2P) solo en el Pro, algo más de rendimiento y eficiencia, más IA. Se habla del A22 Pro en 1,4 nm para 2028. |
| Qualcomm | **Snapdragon 8 Elite Gen 7** | Finales de 2027 (Snapdragon Summit) | Sin datos fiables todavía. Se espera 2 nm mejorado (N2P), más IA y mejor GPU. |
| Intel | **Core Ultra 400 "Nova Lake-S"** | Intel habló de finales de 2026; filtraciones más recientes lo sitúan a principios de 2027 | Hasta **52 núcleos** (16 P + 32 E + 4 LP-E); gran caché L3 (**bLLC**) para competir con los X3D de AMD; **DDR5-8000**; Wi-Fi 7 y Thunderbolt 5 integrados; NPU en todos los modelos; **nuevo socket LGA1954**. |
| AMD | **Ryzen 10000 "Olympic Ridge" (Zen 6)** | Primera mitad de 2027 | Hasta **12 núcleos por CCD** (hasta 24 núcleos en sobremesa); núcleos fabricados en **2 nm (TSMC N2P)**; nuevas instrucciones AVX-512; **mismo socket AM5**. |

**Ejemplo de tabla del ejercicio 1 con la próxima generación de Intel (datos no definitivos):**

| Especificaciones | Core Ultra 9 (Nova Lake-S, modelo superior) |
| ---------------- | ------------------------------------------- |
| Núcleos | 52 (16 P + 32 E + 4 LP-E) |
| Chips de cómputo | 2 (en los modelos de más de 28 núcleos) |
| Caché | Hasta unos 288 MB de bLLC |
| Memoria | DDR5-8000, doble canal |
| Potencia | Hasta 175 W de base |
| Socket | LGA1954 |
| Integrado | NPU, Wi-Fi 7, Thunderbolt 5 |

**Cómo mejorarán a los actuales**

- **Más núcleos**: Intel pasa de 24 a 52 y AMD de 16 a 24 en lo más alto de la gama.
- **Más caché**: Intel copia la idea del 3D V-Cache de AMD con el bLLC.
- **Procesos más pequeños** (2 nm), que dan más rendimiento con menos consumo.
- **Memoria más rápida**: DDR5-8000 en Intel, y LPDDR6 en los móviles.
- **Más IA integrada**: la NPU pasa a estar en todos los procesadores.
- **Plataforma**: Intel vuelve a cambiar de socket, y AMD mantiene AM5, así que un usuario de AMD puede actualizar sin cambiar la placa.

---

### Fuentes

- [Apple A20 Pro – iGeeksBlog](https://www.igeeksblog.com/apple-a20-pro-everything-you-need-to-know/)
- [Apple A20 Pro en Geekbench – Notebookcheck](https://www.notebookcheck.net/Apple-A20-Pro-storms-Geekbench-with-near-5-GHz-clocks-and-a-massive-single-core-lead-over-Qualcomm-and-MediaTek.1395700.0.html)
- [Snapdragon 8 Elite Gen 6 – IT Daily](https://itdaily.com/news/workplace/qualcomm-snapdragon-8-elite-gen-6-extreme/)
- [Snapdragon 8 Elite Gen 6 – Beebom](https://gadgets.beebom.com/news/qualcomm-snapdragon-8-elite-gen-6-launched-2nm-power-5-ghz-oryon-cores)
- [Core Ultra 7 270K Plus review – Club386](https://www.club386.com/?p=137873)
- [Ryzen 7 9850X3D review – Club386](https://www.club386.com/amd-ryzen-7-9850x3d-review/)
- [Core Ultra 400 Nova Lake – heise](https://heise.de/-11255217)
- [Zen 6 – Wikipedia](https://en.wikipedia.org/wiki/Zen_6)
- [A21 Pro – Rutab](https://rutab.net/b/video-games/2026/06/19/apple-gotovit-moschnyy-chip-a21-pro-dlya-iphone-2027-goda-na-novom-tehprocesse.html)
