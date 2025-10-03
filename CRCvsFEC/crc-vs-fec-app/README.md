# Comparación CRC vs FEC

Esta aplicación permite comparar el algoritmo CRC y el código FEC (Hamming(12,8)) usando una palabra de 8 bits y un polinomio en binario.  
Se muestran los tiempos de ejecución y la cantidad de operaciones XOR realizadas por cada algoritmo, lo que ayuda a entender el costo computacional y de hardware.

## Cómo usar

1. Instala las dependencias:
   ```
   pip install streamlit pandas
   ```

2. Ejecuta la aplicación:
   ```
   streamlit run app.py
   ```

3. Ingresa una palabra de 8 bits (por ejemplo: `11010101`) y un polinomio en binario (por ejemplo: `1011`).

4. Haz clic en "Comparar" para ver los resultados y las gráficas.

## ¿Qué muestra la app?

- **CRC Resto:** Resultado del cálculo CRC.
- **FEC Codificado:** Palabra codificada con Hamming(12,8).
- **Tiempo CRC/FEC:** Tiempo de ejecución de cada algoritmo.
- **Operaciones XOR:** Cantidad de operaciones XOR realizadas por cada algoritmo.
- **Gráficas:** Comparación visual de tiempos y operaciones.

## Nota educativa

El número de operaciones XOR es una aproximación al costo de implementación en hardware.  
CRC suele ser más eficiente en hardware, aunque en software la diferencia puede variar.

---
