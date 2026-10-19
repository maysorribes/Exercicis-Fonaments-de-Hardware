# Soluciones · UT2P1 Fuentes de alimentación

Fundamentos de Hardware · CFGS ASIR (1.º curso)

> Las partes que dependen de cada grupo (portada, acuerdos de trabajo, fotos, diario de laboratorio y conclusiones) no tienen una solución única. Aquí se indica qué debe aparecer y cuáles son los valores correctos con los que comparar.

---

## 1. Comprobación de la fuente

### 1.1 Preparar los elementos necesarios

> Preparar los elementos necesarios, incluyendo un diario de laboratorio donde anotar los pasos seguidos.

**Solución**

Material mínimo:

- Destornillador de estrella (PH2) y, si hace falta, uno plano.
- **Multímetro digital** con sus dos puntas.
- **Pulsera antiestática** (o, como mínimo, tocar una parte metálica del chasis antes de manipular).
- Un clip o cable puente para encender la fuente fuera del equipo (o un *tester* de fuentes).
- Recipiente o bandeja para los tornillos y bridas para recolocar los cables.
- Móvil o cámara para las fotos.

El **diario de laboratorio** debe recoger, en orden y con hora: qué se hace, con qué herramienta, qué se observa y cualquier incidencia. Es lo que permite al cliente (o al jefe de departamento) ver de forma profesional el trabajo realizado y lo que permite volver a montar el equipo igual que estaba.

---

### 1.2 Precauciones de seguridad

> Toma las precauciones necesarias para poder desmontarlo con seguridad. Debes indicar cuáles has seguido, describirlas y aplicarlas.

**Solución**

| Precaución | Por qué |
| ---------- | ------- |
| Apagar el equipo, poner el interruptor trasero de la fuente en **0** y **desenchufar el cable de red** | Evitar descargas y que la placa reciba los 5 V de *standby* mientras se manipula |
| Pulsar el botón de encendido unos segundos con el equipo desenchufado | Descargar la energía que queda en los condensadores |
| Usar **pulsera antiestática** conectada al chasis | Evitar descargas electrostáticas que dañen componentes |
| Trabajar sobre una **mesa no conductora**, seca y despejada | Evitar cortocircuitos y que se pierdan piezas |
| **No abrir nunca la fuente de alimentación** | Sus condensadores pueden conservar tensiones peligrosas aunque esté desenchufada |
| Sujetar los conectores por la carcasa de plástico, nunca tirando del cable | No dañar cables ni pines |
| Al medir con la fuente encendida, no tocar las puntas metálicas ni hacer contacto entre dos pines | Evitar cortocircuitos y descargas |
| Hacer fotos antes de desconectar nada | Poder volver a conectarlo todo igual |

---

### 1.3 Comprobación inicial

> Haz una foto del PC arrancando. Al conectarlo de nuevo debe funcionar igual que antes.

**Solución**

Foto del equipo encendido mostrando el arranque (POST, BIOS/UEFI o sistema operativo). Al final de la práctica debe aparecer otra foto equivalente que demuestre que el equipo **arranca igual que antes**. Si no la hay o el equipo no arranca, se aplica la penalización del 30 %.

---

### 1.4 Foto del estado previo

> Toma una foto del estado previo al desmontaje.

**Solución**

Foto con la caja abierta en la que se vean claramente la fuente y **todos los conectores que salen de ella** (24 pines de la placa, EPS de la CPU, PCIe de la gráfica, SATA, etc.). Sin esta foto, la práctica puntúa como máximo el 50 %.

---

### 1.5 Test de los pines de la fuente

> Desconecta y realiza el test de los pines de la F.A. Realiza la identificación de los pines de la fuente de alimentación. Al lado de cada pin, debes anotar el valor que ha dado el multímetro.

**Solución**

**Cómo se mide**

1. Multímetro en **tensión continua (V⎓)**, escala de 20 V.
2. Punta **negra** en un pin de masa (COM, cable negro); punta **roja** en el pin que se quiere medir, por la parte trasera del conector.
3. **Apagada**: la fuente enchufada a la red y con el interruptor en 1, pero sin la orden de encendido.
4. **Encendida**: se puentea el pin **PS_ON** (cable verde) con cualquier **COM** (cable negro) con un clip. La fuente arranca sola (se oye el ventilador).

Con la fuente apagada solo hay tensión en dos pines: **+5VSB** (morado, alimentación de reposo, la que permite encender el equipo con el botón o por red) y **PS_ON** (verde, que la fuente mantiene a nivel alto mientras espera la orden de encendido).

**Versión 2.0 (conector de 24 pines)**

| Pin | Color | Señal | Apagada | Encendida |
| --- | ----- | ----- | ------- | --------- |
| 1 | Naranja | +3,3 V | 0 V | ≈ 3,3 V |
| 2 | Naranja | +3,3 V | 0 V | ≈ 3,3 V |
| 3 | Negro | COM (masa) | 0 V | 0 V |
| 4 | Rojo | +5 V | 0 V | ≈ 5 V |
| 5 | Negro | COM | 0 V | 0 V |
| 6 | Rojo | +5 V | 0 V | ≈ 5 V |
| 7 | Negro | COM | 0 V | 0 V |
| 8 | Gris | PWR_OK (Power Good) | 0 V | ≈ 5 V |
| 9 | Morado | +5VSB (*standby*) | **≈ 5 V** | ≈ 5 V |
| 10 | Amarillo | +12 V | 0 V | ≈ 12 V |
| 11 | Amarillo | +12 V | 0 V | ≈ 12 V |
| 12 | Naranja | +3,3 V | 0 V | ≈ 3,3 V |
| 13 | Naranja (+ marrón de sensor) | +3,3 V | 0 V | ≈ 3,3 V |
| 14 | Azul | −12 V | 0 V | ≈ −12 V |
| 15 | Negro | COM | 0 V | 0 V |
| 16 | Verde | PS_ON | **≈ 3,3–5 V** | 0 V (puenteado a masa) |
| 17 | Negro | COM | 0 V | 0 V |
| 18 | Negro | COM | 0 V | 0 V |
| 19 | Negro | COM | 0 V | 0 V |
| 20 | — (blanco en fuentes antiguas) | NC (antes −5 V) | 0 V | 0 V (−5 V en fuentes antiguas) |
| 21 | Rojo | +5 V | 0 V | ≈ 5 V |
| 22 | Rojo | +5 V | 0 V | ≈ 5 V |
| 23 | Rojo | +5 V | 0 V | ≈ 5 V |
| 24 | Negro | COM | 0 V | 0 V |

**Versión 1.0 (conector de 20 pines)**

| Pin | Color | Señal | Apagada | Encendida |
| --- | ----- | ----- | ------- | --------- |
| 1 | Naranja | +3,3 V | 0 V | ≈ 3,3 V |
| 2 | Naranja | +3,3 V | 0 V | ≈ 3,3 V |
| 3 | Negro | COM | 0 V | 0 V |
| 4 | Rojo | +5 V | 0 V | ≈ 5 V |
| 5 | Negro | COM | 0 V | 0 V |
| 6 | Rojo | +5 V | 0 V | ≈ 5 V |
| 7 | Negro | COM | 0 V | 0 V |
| 8 | Gris | PWR_OK | 0 V | ≈ 5 V |
| 9 | Morado | +5VSB | **≈ 5 V** | ≈ 5 V |
| 10 | Amarillo | +12 V | 0 V | ≈ 12 V |
| 11 | Naranja | +3,3 V | 0 V | ≈ 3,3 V |
| 12 | Azul | −12 V | 0 V | ≈ −12 V |
| 13 | Negro | COM | 0 V | 0 V |
| 14 | Verde | PS_ON | **≈ 3,3–5 V** | 0 V (puenteado a masa) |
| 15 | Negro | COM | 0 V | 0 V |
| 16 | Negro | COM | 0 V | 0 V |
| 17 | Negro | COM | 0 V | 0 V |
| 18 | Blanco | −5 V | 0 V | ≈ −5 V |
| 19 | Rojo | +5 V | 0 V | ≈ 5 V |
| 20 | Rojo | +5 V | 0 V | ≈ 5 V |

**¿Cuándo está bien una medida?** La norma ATX admite una tolerancia del **±5 %** en las salidas principales y del **±10 %** en −12 V:

| Salida | Mínimo | Máximo |
| ------ | ------ | ------ |
| +3,3 V | 3,14 V | 3,47 V |
| +5 V y +5VSB | 4,75 V | 5,25 V |
| +12 V | 11,40 V | 12,60 V |
| −12 V | −10,80 V | −13,20 V |

Si alguna salida queda fuera de estos márgenes, no da tensión o la fuente no arranca al puentear PS_ON, **la fuente está averiada y hay que sustituirla**. Si con la fuente apagada no hay 5 V en +5VSB, el equipo no podrá encenderse con el botón aunque el resto de salidas funcione.

---

## 2. Cálculos de rendimiento

### Apartado A

> Determina cuál sería la potencia que debería tener una fuente de alimentación con certificación 80+Gold para que un equipo cuyo consumo máximo puntual sea de 705 W y en su actividad normal (la mayor parte del tiempo) tenga un consumo de 480 W y que permita conseguir la mejor eficiencia energética posible. Una vez calculado, determina las posibles ampliaciones que podremos hacer.

**Solución**

La certificación 80 PLUS Gold exige estas eficiencias (red de 115 V):

| Carga | 20 % | 50 % | 100 % |
| ----- | ---- | ---- | ----- |
| Eficiencia mínima | 87 % | **90 %** | 87 % |

La eficiencia máxima se consigue **al 50 % de carga**, así que el consumo normal del equipo debe ser aproximadamente la mitad de la potencia de la fuente:

$$P_{fuente} = \frac{480\ W}{0{,}5} = 960\ W \;\rightarrow\; \textbf{fuente comercial de 1000 W 80+ Gold}$$

Comprobaciones:

- Consumo normal: 480 / 1000 = **48 %** de carga, en la zona de máxima eficiencia.
- Pico máximo: 705 / 1000 = **70,5 %** de carga; la fuente lo cubre con holgura.
- Consumo real de la red en uso normal: 480 W / 0,90 ≈ **533 W**; la diferencia (≈ 53 W) se pierde en forma de calor en la fuente.

**Ampliaciones posibles**

- Margen hasta la potencia nominal: 1000 − 705 = **295 W** en el pico.
- Para no tener la fuente al límite, conviene que el pico no supere el 80–90 % (800–900 W), así que el margen razonable es de **unos 100–200 W**.
- Con ese margen caben ampliaciones como más memoria RAM (≈ 3–5 W por módulo), más discos (SSD ≈ 5–8 W; HDD ≈ 6–10 W), más ventiladores o refrigeración líquida (≈ 2–5 W por ventilador; 10–20 W la bomba), o **cambiar la gráfica o la CPU por otra que consuma hasta unos 150–200 W más**.
- Cualquier ampliación hará que el consumo normal supere el 50 % de carga y la eficiencia baje un poco, aunque seguirá cerca del 90 %.

Se dan por buenas otras potencias comerciales cercanas (por ejemplo, 850 W, con un consumo normal del 56 % de carga) si el grupo lo justifica, pero la que más se ajusta al criterio del 50 % es la de **1000 W**.

---

### Apartado B

> Usando el PC del apartado A, indica cuál sería su gasto al tener el PC encendido ininterrumpidamente un mes con el precio actual del kWh (tarifa de mercado, octubre de 2026, sin impuestos): punta 0,229 €/kWh, llano 0,189 €/kWh, valle 0,129 €/kWh.

**Solución** (tomando como referencia **octubre de 2026**)

**1. Días y horas de cada franja**

Octubre de 2026 tiene 31 días: 9 son de fin de semana y el lunes 12 es festivo nacional, así que hay **21 días laborables** y **10 días que son valle completo**.

| Franja | Horas por día laborable | Cálculo | Horas en el mes |
| ------ | ----------------------- | ------- | --------------- |
| Punta | 8 h (10–14 y 18–22) | 21 × 8 | **168 h** |
| Llano | 8 h (8–10, 14–18 y 22–24) | 21 × 8 | **168 h** |
| Valle | 8 h (0–8) + 24 h los festivos | 21 × 8 + 10 × 24 | **408 h** |
| **Total** | | | **744 h** (= 31 × 24) |

**2. Potencia que se paga**

La compañía eléctrica factura lo que la fuente **toma de la red**, no lo que entrega al equipo. Con un consumo normal de 480 W y una eficiencia del 90 %:

$$P_{red} = \frac{480\ W}{0{,}90} \approx 533{,}3\ W = 0{,}5333\ kW$$

**3. Energía y coste**

| Franja | Energía (kWh) | Precio (€/kWh) | Coste |
| ------ | ------------- | -------------- | ----- |
| Punta | 168 × 0,5333 = 89,60 | 0,229 | 20,52 € |
| Llano | 168 × 0,5333 = 89,60 | 0,189 | 16,93 € |
| Valle | 408 × 0,5333 = 217,60 | 0,129 | 28,07 € |
| **Total** | **396,80 kWh** | | **65,52 €** |

**El equipo cuesta unos 65,52 € al mes** (sin impuestos ni término de potencia).

Si el grupo **no tiene en cuenta la eficiencia** y calcula directamente con 480 W, obtiene 357,12 kWh y **58,97 €**. El planteamiento es correcto, pero se debe señalar que se pagan los ≈ 53 W que se pierden en la fuente. Si eligen otro mes, el resultado cambia según el número de días laborables y festivos; se corrige con el mismo método.
