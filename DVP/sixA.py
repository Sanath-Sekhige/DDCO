import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plt.plot(x, y, label = 'y = x^2', color='green', marker='o')

plt.title('Linear Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.legend()
plt.grid()
plt.show()