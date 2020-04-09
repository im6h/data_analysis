import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_json('json/data.json')
print(data)
last_updated = pd.to_datetime(data["last_updated"]).dt.strftime('%m-%d')

plt.plot(last_updated,data.total_confirmed,marker='o',color='red',linewidth=2)
plt.plot(last_updated,data.total_deaths, marker='o', color='gray',linewidth=2)
plt.plot(last_updated,data.total_recovered,marker='o',color='green',linewidth=2)
plt.show()
