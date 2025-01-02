import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.scatter(x, y, color='red', marker='o')

plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()