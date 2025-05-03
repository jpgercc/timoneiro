import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import librosa

# === PARÂMETROS ===
audio_path = "sinatra.mp3"       # Caminho do seu MP3
blocksize = 16384                # Maior bloco para mais precisão (~0.37s)
hopsize = blocksize              # Mantém sincronizado
samplerate = 44100               # Librosa converte para isso
alpha = 0.5                      # Suavização (0 = muito suave, 1 = nenhum filtro)

# === CARREGA O ÁUDIO ===
audio, sr = librosa.load(audio_path, sr=samplerate, mono=True)
total_blocks = len(audio) // hopsize
cursor = [0]  # Lista para passar por referência

# === CONFIGURAÇÃO DO PLOT ===
x_fft = np.fft.rfftfreq(blocksize, 1 / samplerate)
fig, ax = plt.subplots()
line, = ax.semilogx(x_fft, np.zeros_like(x_fft))
ax.set_xlim(20, samplerate / 2)
ax.set_ylim(-100, 0)
ax.set_xlabel("Frequência (Hz)")
ax.set_ylabel("Amplitude (dB)")
plt.title("Espectro em tempo real do MP3")

# Para suavização
prev_amplitude = np.zeros_like(x_fft)

# === CALLBACK DE ÁUDIO ===
def callback(outdata, frames, time, status):
    i = cursor[0]
    start = i * hopsize
    end = start + blocksize
    if end > len(audio):
        outdata[:] = np.zeros((frames, 1))
        raise sd.CallbackStop()
    else:
        block = audio[start:end]
        outdata[:] = block.reshape(-1, 1)
        cursor[0] += 1

# === ANIMAÇÃO DO PLOT ===
def update_plot(frame):
    i = cursor[0]
    start = i * hopsize
    end = start + blocksize
    if end > len(audio):
        return line,

    block = audio[start:end] * np.blackman(blocksize)
    fft = np.fft.rfft(block)
    amplitude = np.abs(fft) / blocksize
    amplitude /= np.max(amplitude) + 1e-10  # Normaliza para 0–1
    amplitude_db = 20 * np.log10(amplitude + 1e-10)  # Em dB

    # Suavização
    global prev_amplitude
    smoothed = alpha * amplitude_db + (1 - alpha) * prev_amplitude
    prev_amplitude = smoothed

    # Frequência dominante
    dominant_bin = np.argmax(amplitude)
    dominant_freq = x_fft[dominant_bin]
    print(f"Frequência dominante: {dominant_freq:.2f} Hz")

    line.set_ydata(smoothed)
    return line,

# === INICIA STREAM E ANIMAÇÃO ===
stream = sd.OutputStream(samplerate=samplerate, channels=1, blocksize=hopsize, callback=callback)

with stream:
    ani = animation.FuncAnimation(fig, update_plot, interval=100)
    plt.show()
