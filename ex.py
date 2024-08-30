import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# Definindo a função de transferência: Numerador e Denominador
numerator = [2, 0]  # Exemplo: 2s + 0 (não há termo constante, então o zero está em s = 0)
denominator = [1, 2, 5]  # s^2 + 2s + 5 (polos complexos conjugados)

# Obtendo os polos e zeros
system = signal.TransferFunction(numerator, denominator)
poles = system.poles
zeros = system.zeros

# Plotando o mapa de polos e zeros
plt.figure(figsize=(8, 8))
plt.scatter(np.real(poles), np.imag(poles), color='red', marker='x', s=100, label='Polos')
plt.scatter(np.real(zeros), np.imag(zeros), color='blue', marker='o', s=100, label='Zeros')
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title('Mapa de Polos e Zeros para a função de transferência G(s).')
plt.grid(True)
plt.legend()
plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.show()
