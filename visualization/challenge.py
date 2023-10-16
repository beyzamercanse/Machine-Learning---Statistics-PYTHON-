import numpy as np
import matplotlib.pyplot as plt

# generate data

# 100 linearly spaced values between 0.001 and 10.
data_linear = np.linspace(start=0.001, stop=10, num=100)  # y=x
data_log = np.exp(data_linear)  # y = e**x

# linear scale
plt.plot(data_log[:40])
plt.plot(data_linear)
plt.show()

# log scale
plt.plot(data_log)
plt.plot(data_linear)
plt.yscale("log")
plt.show()
