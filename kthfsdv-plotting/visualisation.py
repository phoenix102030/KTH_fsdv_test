import numpy as np
import matplotlib.pyplot as plt

class SimpleVisualizer:
    def __init__(self, t_start=0, t_end=5, t_interval=0.1):
        self.t = np.arange(t_start, t_end, t_interval)
        self.fig, self.ax = plt.subplots()

    def lambda_func(self, t):
        return 5 * np.sin(2 * np.pi * 1 * t)

    def h_func(self, t):
        return 3 * np.pi * np.exp(-self.lambda_func(t))
        
    def plot(self):
        h = self.h_func(self.t)
        self.ax.plot(self.t, h, label='h(t)')
        self.ax.legend()
        plt.show()

vis = SimpleVisualizer()
vis.plot()
