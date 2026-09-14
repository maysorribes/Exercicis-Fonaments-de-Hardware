"""
conversiones.py

Colección de funciones para practicar conversiones entre sistemas numéricos:
binario, octal, decimal, hexadecimal, complemento a 2 e IEEE 754 (32 bits).

Ejecuta este archivo directamente para ver una demo con los ejercicios
del README.md:

    python3 conversiones.py
"""

import struct


# ---------------------------------------------------------------------------
# Conversiones básicas entre bases
# ---------------------------------------------------------------------------

def a_decimal(numero: str, base: int) -> int:
    """Convierte una cadena en la base indicada (2, 8, 16, ...) a decimal."""
    return int(numero, base)


def decimal_a_binario(n: int) -> str:
    return format(n, "b") if n >= 0 else "-" + format(-n, "b")


def decimal_a_octal(n: int) -> str:
    return format(n, "o") if n >= 0 else "-" + format(-n, "o")


def decimal_a_hex(n: int) -> str:
    return format(n, "X") if n >= 0 else "-" + format(-n, "X")


def binario_a_octal(bin_str: str) -> str:
    """Convierte directamente binario a octal agrupando de 3 en 3 bits."""
    bin_str = bin_str.zfill(-len(bin_str) % 3 + len(bin_str))  # relleno inicial
    resto = len(bin_str) % 3
    if resto:
        bin_str = "0" * (3 - resto) + bin_str
    grupos = [bin_str[i:i + 3] for i in range(0, len(bin_str), 3)]
    return "".join(str(int(g, 2)) for g in grupos)


def binario_a_hex(bin_str: str) -> str:
    """Convierte directamente binario a hexadecimal agrupando de 4 en 4 bits."""
    resto = len(bin_str) % 4
    if resto:
        bin_str = "0" * (4 - resto) + bin_str
    grupos = [bin_str[i:i + 4] for i in range(0, len(bin_str), 4)]
    return "".join(format(int(g, 2), "X") for g in grupos)


# ---------------------------------------------------------------------------
# Suma en binario (con comprobación en decimal)
# ---------------------------------------------------------------------------

def suma_binaria(a: str, b: str):
    resultado = decimal_a_binario(int(a, 2) + int(b, 2))
    return resultado, int(a, 2), int(b, 2), int(resultado, 2)


# ---------------------------------------------------------------------------
# Complemento a 2
# ---------------------------------------------------------------------------

def complemento_a_2(n: int, bits: int = 8) -> str:
    """Devuelve la representación en complemento a 2 de n (positivo o negativo)."""
    if n >= 0:
        return format(n, f"0{bits}b")
    return format((1 << bits) + n, f"0{bits}b")


def complemento_a_2_a_decimal(bin_str: str) -> int:
    """Interpreta una cadena binaria en complemento a 2 y devuelve su valor decimal."""
    bits = len(bin_str)
    valor = int(bin_str, 2)
    if bin_str[0] == "1":  # número negativo
        valor -= (1 << bits)
    return valor


# ---------------------------------------------------------------------------
# IEEE 754 - precisión simple (32 bits)
# ---------------------------------------------------------------------------

def ieee754_32(n: float) -> str:
    """Devuelve la representación IEEE 754 de 32 bits de un número, como cadena
    de 32 caracteres '0'/'1' agrupada en signo(1) exponente(8) mantisa(23)."""
    [entero] = struct.unpack(">I", struct.pack(">f", n))
    binario = format(entero, "032b")
    return f"{binario[0]} {binario[1:9]} {binario[9:]}"


# ---------------------------------------------------------------------------
# Demo con los ejercicios del README
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("== Ejercicio 1: binario -> decimal ==")
    for b in ["1101", "100110", "11111"]:
        print(f"  {b}_2 = {a_decimal(b, 2)}")

    print("\n== Ejercicio 2: decimal -> binario ==")
    for d in [25, 100, 17]:
        print(f"  {d} = {decimal_a_binario(d)}_2")

    print("\n== Ejercicio 3: octal <-> decimal ==")
    print(f"  345_8 = {a_decimal('345', 8)}")
    print(f"  200_10 = {decimal_a_octal(200)}_8")

    print("\n== Ejercicio 4: hexadecimal <-> decimal ==")
    print(f"  1A3_16 = {a_decimal('1A3', 16)}")
    print(f"  500_10 = {decimal_a_hex(500)}_16")

    print("\n== Ejercicio 5: binario -> octal y hexadecimal directos ==")
    b = "111010110"
    print(f"  {b}_2 -> octal: {binario_a_octal(b)}_8")
    print(f"  {b}_2 -> hex:   {binario_a_hex(b)}_16")

    print("\n== Ejercicio 6: sumas en binario ==")
    for x, y in [("1101", "1011"), ("10010", "00111")]:
        res, dx, dy, dres = suma_binaria(x, y)
        print(f"  {x}_2 + {y}_2 = {res}_2   ({dx} + {dy} = {dres})")

    print("\n== Ejercicio 8: tabla 16 a 20 ==")
    print(f"  {'Dec':>4} {'Bin':>8} {'Oct':>5} {'Hex':>5}")
    for d in range(16, 21):
        print(f"  {d:>4} {decimal_a_binario(d):>8} {decimal_a_octal(d):>5} {decimal_a_hex(d):>5}")

    print("\n== Ejercicio 9: -18 en complemento a 2 (8 bits) ==")
    print(f"  -18 -> {complemento_a_2(-18, 8)}")
    print(f"  comprobacion -> {complemento_a_2_a_decimal(complemento_a_2(-18, 8))}")

    print("\n== Ejercicio 14: 5.25 en IEEE 754 (32 bits) ==")
    print(f"  5.25 -> {ieee754_32(5.25)}")
