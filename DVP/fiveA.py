import matplotlib.pyplot as plt
import numpy as np

data = ['Apple', 'Banana', 'Orange', 'Grapes']
sizes = np.array([30, 25, 15, 30])

plt.pie(sizes, labels=data, autopct='%1.0f%%', startangle=140)

plt.title('Fruit Distribution')

plt.show()