import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("DCOILBRENTEUv2.csv")

# minmax (normalized)
minmax_price = (df["DCOILBRENTEU"] - df["DCOILBRENTEU"].min()) / (df["DCOILBRENTEU"].max() - df["DCOILBRENTEU"].min())

# z score value

zscore_price = ( (df["DCOILBRENTEU"]-df["DCOILBRENTEU"].mean()) ) / df["DCOILBRENTEU"].std()

#plots de minmax e z value
plt.figure()
plt.subplot(211)
plt.plot(df["DATE"],minmax_price)
plt.xticks(df["DATE"][::300])

plt.subplot(212)
plt.plot(df["DATE"],zscore_price)
plt.xticks(df["DATE"][::300])
plt.show()


# 30 day period
df["AVERAGE"] = minmax_price.rolling(window=30).mean()

plt.figure()
plt.plot(df["DATE"],df["AVERAGE"])
plt.xticks(df["DATE"][::300])
plt.show()
