import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sb


iris = pd.read_csv("iris.data", names=["s_length","s_width","p_length","p_width","class"])

print(iris["p_width"])

sb.relplot(data=iris,x=iris["s_length"],y=iris["s_width"], hue=iris["class"], size=iris["p_width"], kind="scatter")
plt.show()
