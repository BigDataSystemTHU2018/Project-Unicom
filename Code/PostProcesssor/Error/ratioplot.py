import numpy as np
import matplotlib.pyplot as plt

x = [24,48,72,96,120,144,168]
y1 = [45.66,42.49,41.17,40.52,40.07,39.83,39.82]
y2 = [53.01,46.02,42.34,39.96,38.22,36.76,35.60]
y3 = [48.80,43.20,40.19,38.37,37.10,36.10,35.35]
y4 = [51.49,43.94,39.96,37.40,35.46,33.91,32.70]
y0 = [40.07,40.59,40.80,40.68,40.46,40.27,40.16]

plt.plot(x, y1,label="model1",marker = "o")
plt.plot(x, y2,label="model2",marker = "*")
plt.plot(x, y3,label="model3",marker = "+")
plt.plot(x, y4,label="model4",marker = "_")
plt.plot(x, y0,label="interpolation",marker = "s")
plt.xlabel("Time/h")
plt.ylabel("accuracy(%)")
plt.title('line chart')
plt.legend(loc="best")
plt.title("Change trend with time")



plt.savefig('accuracy.png',dpi=200)
plt.show()

xx = [24,48,72,96,120,144,168]
yy1 = [100,100,100,97.91,98.33,98.61,98.88]
yy2 = [100,100,100,97.91,85.83,71.52,61.30]
yy3 = [100,87.50,91.66,87.50,78.33,65.27,55.95]
yy4 = [100,95.83,97.22,85.41,68.33,56.94,48.80]
yy0 = [20.83,27.08,29.16,28.12,22.20,18.75,16.07]

plt.plot(xx, yy1,label="model1",marker = "o")
plt.plot(xx, yy2,label="model2",marker = "*")
plt.plot(xx, yy3,label="model3",marker = "+")
plt.plot(xx, yy4,label="model4",marker = "_")
plt.plot(xx, yy0,label="interpolation",marker = "s")
plt.xlabel("Time/h")
plt.ylabel("accuracy(%)")
plt.title('line chart')
plt.legend(loc="best")
plt.title("Change trend with time")



plt.savefig('accuracyRSME.png',dpi=200)
plt.show()
