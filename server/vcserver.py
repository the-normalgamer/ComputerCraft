import pyaudio
import websockets
import asyncio
import numpy as np


from dfpwm import DFPWM  # Import the DFPWM encoder class

# Audio Settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000  # Matches CC:Tweaked
CHUNK = 1024  # Buffer size
SERVER_URL = "ws://localhost:8080"  # WebSocket address of CC computer

async def send_audio():
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    encoder = DFPWM()

    async with websockets.connect(SERVER_URL) as ws:
        print("Connected to WebSocket server. Sending audio...")
        while True:
            pcm_data = stream.read(CHUNK, exception_on_overflow=False)
            pcm_samples = np.frombuffer(pcm_data, dtype=np.int16)  # Convert bytes to NumPy array
            dfpwm_data = encoder.encode(pcm_samples)  # Convert PCM to DFPWM

            await ws.send(dfpwm_data)  # Send small DFPWM chunks to CC:Tweaked

asyncio.run(send_audio())
