import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# Parâmetros
Fs = 50000         # Frequência de amostragem (50kHz, alta para precisão)
T = 1              # Duração do sinal (1 segundo)
Fc = 100          # Frequência da portadora (1 kHz)
Fm = 10            # Frequência da moduladora (10 Hz)
beta = 5           # Índice de modulação

# Gerando o vetor de tempo
t = np.linspace(0, T, int(Fs*T), endpoint=False)

# Onda modulante (som)
moduladora = np.sin(2 * np.pi * Fm * t)

# Onda portadora modulada em frequência (FM)
portadora = np.cos(2 * np.pi * Fc * t + beta * np.sin(2 * np.pi * Fm * t))

# Normaliza o sinal para evitar distorções no áudio
portadora /= np.max(np.abs(portadora))

# Toca o som
sd.play(portadora, samplerate=Fs)
sd.wait()  # Aguarda a reprodução terminar

# Plotando as ondas
plt.figure(figsize=(10, 6))

# Onda modulante
plt.subplot(2, 1, 1)
plt.plot(t, moduladora)
plt.title('Onda Modulante (FM)')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

# Onda FM
plt.subplot(2, 1, 2)
plt.plot(t, portadora)
plt.title('Onda FM')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
