import numpy as np
import matplotlib.pyplot as plt

sample1 = -np.log(np.random.uniform(0.0, 1.0, 10000))

sample2_1 = np.sqrt(-2 * np.log(np.random.uniform(0.0, 1.0, 10000)))
sample2_2 = np.cos(2 * np.pi * np.random.uniform(0.0, 1.0, 10000))
sample2 = sample2_1 * sample2_2

sample3_1 = np.random.uniform(0.0, 1.0, 10000)
sample3_2 = np.random.uniform(0.0, 1.0, 10000)
sample3_3 = sample3_1 - sample3_2
sample3 = sample3_1 / sample3_3
if __name__ == '__main__':
    fig, axs = plt.subplots(3)
    axs[0].hist(sample1, bins='auto', color='b', rwidth=0.8)
    axs[0].set_title('Simulate X = -ln(U) for U ~ Unif(0,1)')
    axs[1].hist(sample2, bins='auto', color='b', rwidth=0.8)
    axs[1].set_title('Simulate Z = sqrt(-2ln(X))cos(2piY) for iid X, Y ~ Unif(0,1)')
    axs[2].hist(sample3, bins=range(-30, 30), color='b', rwidth=0.8)
    axs[2].set_title('Simulate Z = X/(X - Y) for iid X, Y ~ Unif(0,1)')
    plt.subplots_adjust(hspace=0.5)
    plt.show()
