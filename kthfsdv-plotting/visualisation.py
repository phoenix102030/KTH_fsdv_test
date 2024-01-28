import numpy as np
import matplotlib.pyplot as plt

class SimpleVisualizer:
    def __init__(self, t_start=0, t_end=10, t_interval=0.1):
        self.t = np.arange(t_start, t_end, t_interval)
        self.lambda_func = lambda t: 5 * np.sin(2 * np.pi * 1 * t)
        self.h_func = lambda t: 3 * np.pi * np.exp(-self.lambda_func(t))
        self.fig, self.ax = plt.subplots()

    def plot(self):
        h = self.h_func(self.t)
        self.ax.plot(self.t, h, label='h(t)')
        self.ax.legend()
        plt.show()

vis = SimpleVisualizer()
vis.plot()
