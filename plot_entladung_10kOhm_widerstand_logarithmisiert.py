import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("./data/P12_Messung_100kOhm_3.csv")

plt.figure(figsize=(10,6))

# Plot des Logarithmus des zweiten Potentials, verschoben um +4.95, in Rot
plt.plot(df.iloc[:,0], np.log(df.iloc[:,2] + 4.95), color='red', label="logarithmierte Spannung am Kondensator")

plt.xlabel("Zeit [t] = s")
plt.ylabel("Potential logarithmiert [U] = V")

plt.title('Messung: Entladung eines 100μF Kondensators über einen 100kOhm Widerstand in einem RC-Kreis, logarithmiert')
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()
