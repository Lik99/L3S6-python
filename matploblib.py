import matplotlib.pyplot as plt
import numpy as np

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
dev_y = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752]



py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]


js_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
js_dev_y = [50000, 48876, 53850, 57287, 63016, 65998, 80509, 70000, 71496, 75370, 83640]

#plt.plot(dev_x, dev_y, color='r', linestyle = '--', marker='o', label='Salaire moyen Dev')
#plt.plot(py_dev_x, py_dev_y,color='k',linewidth=5, label='Salaire moyen Dev Python')

#plt.bar(dev_x, dev_y, color='r', label='Salaire moyen Dev')
#plt.bar(py_dev_x, py_dev_y,label='Salaire moyen Dev Python')

x_indices = np.arange(len(dev_x))
width = 0.25
plt.bar(x_indices - width,dev_y,width=width, label = 'Salaire moyen Dev')
plt.bar(np.arange(len(py_dev_x)),py_dev_y,width=width, label = 'Salaire moyen Dev')
plt.bar(np.arange(len(js_dev_x))+width,js_dev_y,width=width, label = 'Salaire moyen Dev')

plt.xticks(ticks = x_indices, label=dev_y)

plt.title("Salaire pour chaque age")
plt.xlabel("Age")
plt.ylabel("Salaire")
plt.legend()
plt.grid()

print(plt.style.available)
#plt.savefig('salaireDev.png')

plt.show()
