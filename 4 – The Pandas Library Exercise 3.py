import pandas as pd

df = pd.read_csv("AAPL_yah.csv")

import time

start_time1 = time.process_time()
start_time2 = time.perf_counter()

df["newCol"] = df['Volume'].cumsum()

print("Time used in cumsum -->", time.process_time() - start_time1, "seconds")
print("Time used in cumsum -->", time.perf_counter() - start_time2, "seconds")

import numpy as np

a = np.arange(10)
print(a)

b = np.where(a < 5, a, 10*a)
print(b)

df["signal"] = np.where(df["Close"] > df["Open"], 1.0, 0.0)