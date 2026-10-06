import numpy as np
import matplotlib.pyplot as plt

# Eje X común (SNR de 0 a 10 dB)
rango_snr_db = np.arange(0, 11, 1.0)

# ---------------------------------------------------------
# TUS VECTORES SIMULADOS (Reemplaza con tus datos reales)
# ---------------------------------------------------------
ber_sim_bpsk = np.array([0.078, 0.056, 0.037, 0.022, 0.012, 0.005, 0.002, 0.0007, 0.00018, 0.00004, 0.00001])
ber_sim_qpsk = np.array([0.078, 0.056, 0.037, 0.022, 0.012, 0.005, 0.002, 0.0007, 0.00018, 0.00004, 0.00001]) 
ber_sim_8psk = np.array([0.145, 0.115, 0.085, 0.058, 0.034, 0.017, 0.0075, 0.0028, 0.0009, 0.00025, 0.00006])

# Conversión automática de BER a SER simulada según los bits por símbolo (bps)
ser_sim_bpsk = ber_sim_bpsk                          # BPSK (bps = 1) -> SER = BER
ser_sim_qpsk = 1.0 - (1.0 - ber_sim_qpsk)**2         # QPSK (bps = 2)
ser_sim_8psk = 1.0 - (1.0 - ber_sim_8psk)**3         # 8PSK (bps = 3)

# ---------------------------------------------------------
# GRÁFICA 1: TASA DE ERROR DE BIT (BER) - SOLO SIMULACIÓN
# ---------------------------------------------------------
plt.figure(figsize=(9, 6))
plt.semilogy(rango_snr_db, ber_sim_bpsk, marker='o', color='blue', linestyle='-', linewidth=1.5, markersize=7, label='BPSK Simulada')
plt.semilogy(rango_snr_db, ber_sim_qpsk, marker='^', color='red', linestyle='-', linewidth=1.5, markersize=7, label='QPSK Simulada')
plt.semilogy(rango_snr_db, ber_sim_8psk, marker='s', color='green', linestyle='-', linewidth=1.5, markersize=7, label='8PSK Simulada')

plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('$E_b/N_0$ (dB)', fontsize=12)
plt.ylabel('Tasa de Error de Bit (BER)', fontsize=12)
plt.title('Rendimiento BER - Comparativa de Modulaciones M-PSK (Simulación)', fontsize=14)
plt.legend(fontsize=11)
plt.ylim(1e-6, 1)
plt.tight_layout()
plt.savefig('BER_Solo_Simulado.png', dpi=300)

# ---------------------------------------------------------
# GRÁFICA 2: TASA DE ERROR DE SÍMBOLO (SER) - SOLO SIMULACIÓN
# ---------------------------------------------------------
plt.figure(figsize=(9, 6))
plt.semilogy(rango_snr_db, ser_sim_bpsk, marker='o', color='blue', linestyle='-', linewidth=1.5, markersize=7, label='BPSK Simulada')
plt.semilogy(rango_snr_db, ser_sim_qpsk, marker='^', color='red', linestyle='-', linewidth=1.5, markersize=7, label='QPSK Simulada')
plt.semilogy(rango_snr_db, ser_sim_8psk, marker='s', color='green', linestyle='-', linewidth=1.5, markersize=7, label='8PSK Simulada')

plt.grid(True, which='both', linestyle='--', alpha=0.7)
plt.xlabel('$E_b/N_0$ (dB)', fontsize=12)
plt.ylabel('Tasa de Error de Símbolo (SER)', fontsize=12)
plt.title('Rendimiento SER - Comparativa de Modulaciones M-PSK (Simulación)', fontsize=14)
plt.legend(fontsize=11)
plt.ylim(1e-6, 1)
plt.tight_layout()
plt.savefig('SER_Solo_Simulado.png', dpi=300)

print("\n¡Gráficas generadas con éxito!")
print("Archivos guardados en la carpeta: 'BER_Solo_Simulado.png' y 'SER_Solo_Simulado.png'.")
plt.show()