import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D', 'E']
values = [4, 7, 1, 8, 5]

plt.bar(categories, values, color='skyblue')

plt.title('Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')

plt.show()