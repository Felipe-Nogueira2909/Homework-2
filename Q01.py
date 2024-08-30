import pandas as pd
import matplotlib.pyplot as plt

df_systemA = pd.read_csv('HW2_ex1_dataA.csv')
df_systemB = pd.read_csv('HW2_ex2_dataA.csv')

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

#Tr:
# 1. Encontrar o valor de pico e seu índice correspondente
# O valor de pico é o valor máximo de y(t)
peak_value = df_systemB['y_t'].max()

# 2. Calcular 10% e 90% do valor de pico
ten_percent_peak = 0.1 * peak_value
ninety_percent_peak = 0.9 * peak_value

# 3. Encontrar os tempos correspondentes a 10% e 90% do valor de pico
# O tempo correspondente a 10% do valor de pico
t_rise_start = df_systemB['t'][df_systemB['y_t'] >= ten_percent_peak].iloc[0]

# O tempo correspondente a 90% do valor de pico
t_rise_end = df_systemB['t'][df_systemB['y_t'] >= ninety_percent_peak].iloc[0]

# 4. Calcular o tempo de subida (Rise Time)
# O tempo de subida é o tempo que leva para a resposta ir de 10% a 90% do valor de pico
rise_time = t_rise_end - t_rise_start

print(f"Tempo de subida (Rise Time): {rise_time:.3f} segundos")

#Overshoot percent
# 1. Encontrar o valor de pico e seu índice correspondente
# O valor de pico é o valor máximo de y(t)
peak_value = df_systemB['y_t'].max()

# 2. Identificar o valor em regime permanente
# Neste caso, vamos considerar o último valor de y_t como sendo o valor em regime
steady_state_value = df_systemB['y_t'].iloc[-1]

# 3. Calcular o Overshoot Percentual (%OS)
percent_overshoot = ((peak_value - steady_state_value) / steady_state_value) * 100

print(f"Percentual de Overshoot: {percent_overshoot:.2f}%")

#Time peak
# 1. Encontrar o valor de pico e seu índice correspondente
# O valor de pico é o valor máximo de y(t)
peak_value = df_systemB['y_t'].max()

# 2. Identificar o tempo correspondente ao pico (Tp)
# O tempo de pico é o tempo em que ocorre o valor máximo de y(t)
tp = df_systemB['t'][df_systemB['y_t'] == peak_value].iloc[0]

print(f"Tempo de Pico (Tp): {tp:.3f} segundos")

#Ts
# 1. Identificar o valor em regime permanente
# Neste caso, vamos considerar o último valor de y_t como sendo o valor em regime
steady_state_value = df_systemB['y_t'].iloc[-1]

# 2. Calcular a faixa de tolerância (2% em torno do valor de regime permanente)
tolerance_lower_bound = 0.98 * steady_state_value
tolerance_upper_bound = 1.02 * steady_state_value

# 3. Identificar o tempo de estabelecimento (Ts)
# O tempo de estabelecimento é o primeiro tempo após o qual a resposta permanece dentro da faixa de tolerância
ts = df_systemB['t'][(df_systemB['y_t'] >= tolerance_lower_bound) & (df_systemB['y_t'] <= tolerance_upper_bound)].iloc[-1]

print(f"Tempo de Estabelecimento (Ts): {ts:.3f} segundos")