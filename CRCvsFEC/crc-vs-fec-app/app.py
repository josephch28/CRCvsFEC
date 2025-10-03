import streamlit as st
import time
import pandas as pd

# -----------------------
# CRC Implementation (con contador de operaciones)
# -----------------------
def crc(data, poly):
    data = list(map(int, data))
    poly = list(map(int, poly))
    poly_len = len(poly)
    padded = data + [0] * (poly_len - 1)
    ops = 0  # contador de operaciones

    for i in range(len(data)):
        if padded[i] == 1:
            for j in range(len(poly)):
                padded[i + j] ^= poly[j]
                ops += 1  # cuenta cada XOR
    remainder = padded[-(poly_len - 1):]
    return ''.join(map(str, remainder)), ops

# -----------------------
# Simple FEC (Hamming(12,8)) con contador de operaciones
# -----------------------
def fec(data):
    d = list(map(int, data))  # bits de datos (8)
    if len(d) != 8:
        raise ValueError("La palabra debe ser de 8 bits")

    code = [0]*12
    code[2], code[4], code[5], code[6], code[8], code[9], code[10], code[11] = d

    ops = 0  # contador de operaciones

    # calcular bits de paridad
    code[0] = code[2] ^ code[4] ^ code[6] ^ code[8] ^ code[10]; ops += 4
    code[1] = code[2] ^ code[5] ^ code[6] ^ code[9] ^ code[10]; ops += 4
    code[3] = code[4] ^ code[5] ^ code[6] ^ code[11]; ops += 3
    code[7] = code[8] ^ code[9] ^ code[10] ^ code[11]; ops += 3

    return ''.join(map(str, code)), ops

# -----------------------
# Streamlit Interface
# -----------------------
st.title("Comparación CRC vs FEC")
st.write("""
Ingrese una palabra de 8 bits y un polinomio en binario para comparar los tiempos de ejecución.

**Nota educativa:**  
El número de operaciones XOR aproximadas representa el costo de implementación en hardware.  
CRC suele ser más eficiente en hardware, aunque en software la diferencia puede variar.
""")

word = st.text_input("Palabra (8 bits):", max_chars=8)
poly = st.text_input("Polinomio (binario):")

if st.button("Comparar"):
    if len(word) != 8 or not all(c in "01" for c in word):
        st.error("La palabra debe ser de 8 bits (0/1).")
    elif not all(c in "01" for c in poly) or len(poly) < 2:
        st.error("El polinomio debe estar en binario y con al menos 2 bits.")
    else:
        # Medir tiempo CRC
        start_crc = time.perf_counter()
        result_crc, ops_crc = crc(word, poly)
        end_crc = time.perf_counter()

        # Medir tiempo FEC (Hamming)
        start_fec = time.perf_counter()
        result_fec, ops_fec = fec(word)
        end_fec = time.perf_counter()

        t_crc = end_crc - start_crc
        t_fec = end_fec - start_fec

        # Mostrar resultados
        st.subheader("Resultados")
        st.write(f"**CRC Resto:** {result_crc}")
        st.write(f"**Tiempo CRC:** {t_crc:.8f} s")
        st.write(f"**Operaciones CRC (XOR):** {ops_crc}")
        st.write(f"**FEC Codificado:** {result_fec}")
        st.write(f"**Tiempo FEC:** {t_fec:.8f} s")
        st.write(f"**Operaciones FEC (XOR):** {ops_fec}")

        # Crear DataFrames para las gráficas
        df_tiempos = pd.DataFrame({
            "Algoritmo": ["CRC", "FEC"],
            "Tiempo (s)": [t_crc, t_fec]
        })
        df_ops = pd.DataFrame({
            "Algoritmo": ["CRC", "FEC"],
            "Operaciones XOR": [ops_crc, ops_fec]
        })

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Comparación de Tiempos (segundos)")
            st.bar_chart(df_tiempos.set_index("Algoritmo"))
        with col2:
            st.subheader("Comparación de Operaciones XOR")
            st.bar_chart(df_ops.set_index("Algoritmo"))