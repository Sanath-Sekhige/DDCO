import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]

y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 2, 3, 4, 5]
y3 = [0, 1, 3, 6, 10, 15]

plt.plot(x, y1, color='blue', linestyle='-', marker='o', label='y = x^2')
plt.plot(x, y2, color='red', linestyle='--', marker='x', label='y = x')
plt.plot(x, y3, color='green', linestyle=':', marker='^', label='y = x(x+1)')

plt.title('Linear PLot (Line Formatting)')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.legend()
plt.grid()
plt.show()
