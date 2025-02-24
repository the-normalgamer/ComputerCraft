import numpy as np

class DFPWM:
    def __init__(self):
        self.s = 0.0
        self.lp = 0.0

    def encode(self, pcm):
        dfpwm = bytearray()
        for i in range(0, len(pcm), 8):
            byte = 0
            for j in range(8):
                if i + j < len(pcm):
                    sample = pcm[i + j] / 32768.0  # Normalize to -1.0 to 1.0
                    self.lp += (sample - self.lp) * 0.1  # Low-pass filter
                    bit = int(self.lp > self.s)
                    byte |= bit << j
                    self.s += (bit - 0.5) * 0.02  # Adjust step size
            dfpwm.append(byte)
        return dfpwm
