import matplotlib.pyplot as plt
import numpy as np

data = np.random.randint(1, 10, size=100)

plt.hist(data, bins=8, color='skyblue', edgecolor='black')

plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

plt.show()