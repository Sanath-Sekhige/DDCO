import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 6))
sns.barplot(x="day", y="total_bill", data=tips, palette="Blues_d")

plt.title("Total Bill by Day", fontsize=16)
plt.xlabel("Day of the Week", fontsize=12)
plt.ylabel("Total Bill ($)", fontsize=12)

plt.show()