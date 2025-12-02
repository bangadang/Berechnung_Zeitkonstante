import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("P12_Messung_10kOhm_2.csv")

plt.figure(figsize=(10,6))

# Plot des Logarithmus des ersten Potentials in Blau (nicht sichtbar im Output)
plt.plot(df.iloc[:,0], np.log(df.iloc[:,1]), color='blue')
# Plot des Logarithmus des zweiten Potentials, verschoben um +4.95, in Rot
plt.plot(df.iloc[:,0], np.log(df.iloc[:,2] + 4.95), color='red')

plt.xlabel("Zeit (min)")
plt.ylabel("exp(Potenzial)") # Die Achsenbeschriftung ist hier ungenau, es ist np.log(Potential)

plt.grid(True)
plt.tight_layout()
plt.show()
