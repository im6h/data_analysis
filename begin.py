import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_json('json/data.json')
plt.plot(data.total_confirmed, data.total_deaths)
plt.xlabel('confirmed')
plt.ylabel('deaths')
plt.show()
#print(data.head())
