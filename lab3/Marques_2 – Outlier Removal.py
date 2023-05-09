import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv("EURUSD_Daily_Ask_2018.12.31_2019.10.05v2.csv")

# não para ser utilizado
time_test = pd.to_datetime(df["Time (UTC)"],format='%Y.%m.%d %H:%M:%S')

#  avg and standard deviation de close adda

mean_close = df["Close"].mean()
std_close = df["Close"].std()

#Threshold outliers
'''
threshold = 1
df["k"] = abs(mean_close - df["Close"])/std_close
df1 = df[df['k'] <= threshold]
'''
##################

threshold = 1
df["k"] = abs(mean_close - df["Close"])/std_close

df_shifted = df.shift()

df1 = df.where(df['k'] <= threshold, df_shifted)

##################


plt.figure()
plt.subplot(211)
plt.plot(df1["Time (UTC)"], df1["k"])

plt.subplot(212)
plt.plot(df1["Time (UTC)"], df1["Close"])
plt.show()