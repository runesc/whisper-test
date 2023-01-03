import pyaudio
import wave
# Inicializar PyAudio
p = pyaudio.PyAudio()

# Abrir un flujo de audio
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=16000,
                input=True,
                frames_per_buffer=1024)

# Iniciar la grabación
print("Grabando...")
frames = []

# Grabar durante 5 segundos
for i in range(0, int(16000 / 1024 * 5)):
    data = stream.read(1024)
    frames.append(data)

# Detener la grabación
stream.stop_stream()
stream.close()
p.terminate()

# Guardar el archivo de audio grabado
wave_file = wave.open("grabacion.wav", "wb")
wave_file.setnchannels(1)
wave_file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
wave_file.setframerate(16000)
wave_file.writeframes(b''.join(frames))
wave_file.close()

print("Grabación guardada en grabacion.wav")
