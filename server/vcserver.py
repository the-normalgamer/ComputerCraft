import asyncio
import websockets
import pyaudio
import numpy as np

from dfpwm import DFPWM  # Import our custom DFPWM encoder

# Audio Settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 8000  # Matches CC:Tweaked's speaker
CHUNK = 1024

# List of connected clients
connected_clients = set()

async def audio_stream():
    """Captures microphone audio, encodes it, and sends it to all clients."""
    encoder = DFPWM()
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("🎤 Microphone streaming started...")

    while True:
        pcm_data = stream.read(CHUNK, exception_on_overflow=False)
        pcm_samples = np.frombuffer(pcm_data, dtype=np.int16)  # Convert bytes to NumPy array
        dfpwm_data = encoder.encode(pcm_samples)  # Convert PCM to DFPWM

        # Send data to all connected CC:Tweaked clients
        if connected_clients:
            await asyncio.gather(*(client.send(dfpwm_data) for client in connected_clients))

async def handle_connection(websocket, path):
    """Handles new CC:Tweaked clients connecting to the WebSocket server."""
    print(f"🔌 New connection from {websocket.remote_address}")
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            pass  # Clients don't need to send anything, just receive
    except:
        pass
    finally:
        print(f"❌ Connection closed: {websocket.remote_address}")
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(handle_connection, "0.0.0.0", 8080)  # Host on all interfaces, port 8080
    print("🖥️ WebSocket Server listening on ws://localhost:8080")
    await asyncio.gather(server.wait_closed(), audio_stream())

asyncio.run(main())  # Start the server & audio streaming
