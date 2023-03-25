import numpy as np
import scipy.io.wavfile as wav

# Carrega o arquivo de áudio
sample_rate, audio_data = wav.read('audio.wav')

# Calcula a FFT
fft_data = np.fft.fft(audio_data)
freqs = np.fft.fftfreq(len(audio_data), 1.0/sample_rate)
abs_fft_data = np.abs(fft_data)

# Identifica a frequência dominante
max_index = np.argmax(abs_fft_data[:len(freqs)//2])
max_freq = freqs[max_index]

# Classifica o ruído com base em sua frequência
if max_freq < 100:
    print('Ruído de baixa frequência detectado!')
elif max_freq < 1000:
    print('Ruído de média frequência detectado!')
else:
    print('Ruído de alta frequência detectado!')