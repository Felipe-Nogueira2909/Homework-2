import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import control as ctrl
import scipy.signal as signal

df_systemA = pd.read_csv('HW2_ex1_dataA.csv')
df_systemB = pd.read_csv('HW2_ex2_dataA.csv')

#ITEM A:
# Gráfico Sistema A.
plt.figure(figsize=(10,6))
plt.plot(df_systemA['t'], df_systemA['y_t'], label= 'Sistema A.')
plt.xlabel('tempo(t)')
plt.ylabel('Resposta (y(t))')
plt.title('Resposta do sistema ao longo do tempo.')
plt.legend()
plt.grid(True)

plt.show()

#Gráfico sistema B.
plt.plot(df_systemB['t'], df_systemB['y_t'], label= 'Sistema B.')
plt.xlabel('tempo(t)')
plt.ylabel('Resposta (y(t))')
plt.title('Resposta do sistema ao longo do tempo.')
plt.legend()
plt.grid(True)

plt.show()

#ITEM B:
print("-"*10, "SISTEMA A", "-"*10)
#SISTEMA A (PRIMEIRA ORDEM):
#Tempo de subida para os sistemas A:
peak_value_systemA = df_systemA['y_t'].max() # O valor de pico é o valor máximo de y(t)
steady_state_value_systemA = df_systemA['y_t'].iloc[-1] # valor em regime permanente

# Calculamos 10% e 90% do valor de pico
ten_percent_peak = 0.1 * peak_value_systemA
ninety_percent_peak = 0.9 * peak_value_systemA

t_rise_start = df_systemA['t'][df_systemA['y_t'] >= ten_percent_peak].iloc[0] # O tempo correspondente a 10% do valor de pico
t_rise_end = df_systemA['t'][df_systemA['y_t'] >= ninety_percent_peak].iloc[0] # O tempo correspondente a 90% do valor de pico

# Calculamos o tempo de subida (Rise Time)
rise_time_systemA = t_rise_end - t_rise_start
print(f"Tempo de subida do sistema A é: {rise_time_systemA:.3f} segundos")

#Percent OverShoot:
# Calculamos o Overshoot Percentual (%OS)
percent_overshoot_systemA = ((peak_value_systemA - steady_state_value_systemA) / steady_state_value_systemA) * 100
print(f"Percentual de Overshoot do sistema A é:: {percent_overshoot_systemA:.2f}%")

#Tempo de pico:
tp_systemA = df_systemA['t'][df_systemA['y_t'] == peak_value_systemA].iloc[0]
print(f"Tempo de Pico (Tp) do sistema A: {tp_systemA:.3f} segundos")

#Tempo de estabelecimento:
# Calculamos a faixa de tolerância (2% em torno do valor de regime permanente)
tolerance_lower_bound = 0.98 * steady_state_value_systemA
tolerance_upper_bound = 1.02 * steady_state_value_systemA
ts_systemA = df_systemA['t'][(df_systemA['y_t'] >= tolerance_lower_bound) & (df_systemA['y_t'] <= tolerance_upper_bound)].iloc[-1]

print(f"Tempo de Estabelecimento (Ts)para o sistema A: {ts_systemA:.3f} segundos")

# print(f"Função de Transferência: {G_A}")
#tr = 2,2*tau -> tau = tr/2,2 -> tau = 7,182s -> G(s) = K/tau*s+1 -> K = 1 -> G(s) = 1/7,182s+1
valor_final = df_systemA["y_t"].iloc[-1]

# Calcular 63,2% do valor final
valor_final_63 = 0.632 * valor_final

# Encontrar o tempo correspondente ao valor 63,2%
constante_de_tempo = df_systemA.loc[df_systemA["y_t"] >= valor_final_63, "t"].iloc[0]
print(f"Constante de tempo: {constante_de_tempo:.2f} segundos.")
print("-"*10, "SISTEMA B", "-"*10)
#SISTEMA B (SEGUNDA ORDEM):
#Rise time para os sistemas B:
peak_value_systemB = df_systemB['y_t'].max() # Valor de pico:
steady_state_value_systemB = df_systemB['y_t'].iloc[-1] # Valor em regime permanente

# Calculamos 10% e 90% do valor de pico
ten_percent_peak_B = 0.1 * peak_value_systemB
ninety_percent_peak_B = 0.9 * peak_value_systemB

t_rise_start_B = df_systemB['t'][df_systemB['y_t'] >= ten_percent_peak_B].iloc[0]
t_rise_end_B = df_systemB['t'][df_systemB['y_t'] >= ninety_percent_peak_B].iloc[0]

# Calculamos o tempo de subida (Rise Time)
rise_time_systemB = t_rise_end_B - t_rise_start_B
print(f"Tempo de subida do sistema B é: {rise_time_systemB:.3f} segundos")

#Percent OverShoot:
# Calculamos o Overshoot Percentual (%OS)
percent_overshoot_systemB = ((peak_value_systemB - steady_state_value_systemB) / steady_state_value_systemB) * 100
print(f"Percentual de Overshoot do sistema B é:: {percent_overshoot_systemB:.2f}%")

#Tempo de pico:
tp_systemB = df_systemB['t'][df_systemB['y_t'] == peak_value_systemB].iloc[0]
print(f"Tempo de Pico (Tp) do sistema B: {tp_systemB:.3f} segundos")

#Tempo de estabelecimento:
# Calculamos a faixa de tolerância (2% em torno do valor de regime permanente)
tolerance_lower_bound_B = 0.98 * steady_state_value_systemB
tolerance_upper_bound_B = 1.02 * steady_state_value_systemB

# Identificamos o tempo de estabelecimento (Ts)
ts_systemB = df_systemB['t'][(df_systemB['y_t'] >= tolerance_lower_bound_B) & (df_systemB['y_t'] <= tolerance_upper_bound_B)].iloc[-1]
print(f"Tempo de Estabelecimento (Ts)para o sistema B: {ts_systemB:.3f} segundos")

#OmegaD:
omega_d_systemB = 2 * np.pi / tp_systemB
print(f"Wd: {omega_d_systemB:.3f}")
#zeta:
zeta_systemB = -np.log(percent_overshoot_systemB / 100) / np.sqrt(np.pi**2 + (np.log(percent_overshoot_systemB / 100))**2)
print(f"ζ: {zeta_systemB:.3f}")
#omegaN:
omega_n_systemB = np.pi / (tp_systemB * np.sqrt(1 - zeta_systemB**2))
print(f"Wn: {omega_n_systemB:.3f}")
#Ganho:
K_B = steady_state_value_systemB * (omega_n_systemB ** 2)

numerator_systemB = [K_B]
denominator_systemB = [1, 2*zeta_systemB*omega_n_systemB, omega_n_systemB**2]

#Definir a função de transferência
G_A = ctrl.TransferFunction(numerator_systemB, denominator_systemB)
print(G_A)

a = 1/constante_de_tempo
K_B = 120 * a
G_B = ctrl.TransferFunction(K_B, [1, a])
print(f"Função de transferência do sistema A:{G_B}")

#Item C:
#Sistema B.
TB_s = signal.TransferFunction(numerator_systemB, denominator_systemB)
tempo_TB, resposta_TB = signal.step(TB_s)
# Plotamos a comparação entre a resposta ao degrau do sistema TA(s) e dos dados fornecidos
plt.figure(figsize=(10, 6))
plt.plot(df_systemB['t'], df_systemB['y_t'], label='Sistema B', color='blue')
plt.plot(tempo_TB, resposta_TB, label='Sistema TB(s)', color='red', linestyle='--')
plt.title('Comparação das Respostas ao Degrau: Sistema B vs TB(s)')
plt.xlabel('Tempo (s)')
plt.ylabel('Resposta (y(t))')
plt.legend()
plt.grid(True)
plt.show()

#SistemaA.
numerator_systemA = [16.2]
denominator_systemA = [1, 0.135]
TA_s = ctrl.TransferFunction(numerator_systemA, denominator_systemA)

# Calculando a resposta ao degrau unitário
tempo_TA, resposta_TA = ctrl.step_response(TA_s)
# Plotando a comparação entre a resposta ao degrau do sistema G(s) e os dados fornecidos
plt.figure(figsize=(10, 6))
plt.plot(df_systemA['t'], df_systemA['y_t'], label='Sistema A', color='blue')
plt.plot(tempo_TA, resposta_TA, label='Sistema TA(s)', color='red', linestyle='--')
plt.title('Comparação das Respostas ao Degrau: Sistema TA(s) vs Sistema A')
plt.xlabel('Tempo (s)')
plt.ylabel('Resposta (y(t))')
plt.legend()
plt.grid(True)
plt.show()
