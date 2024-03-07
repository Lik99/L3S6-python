import matplotlib.pyplot as plt

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]



py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]


js_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
js_dev_y = [50000, 48876, 53850, 57287, 63016, 65998, 80509, 70000, 71496, 75370, 83640]

plt.plot(dev_x, dev_y)
plt.plot(py_dev_x, py_dev_y, lable = "Salaire oyen Dev Python")

plt.title("Salaire pour chaque age")
plt.xlabel("Age")
plt.ylabel("Salaire")
plt.legend()

plt.show()
