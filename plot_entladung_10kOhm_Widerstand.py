import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./data/P12_Messung_10kOhm_2.csv")

plt.figure(figsize=(10,6))

# Plot der ersten Potential-Spalte (Index 1) in Blau
plt.plot(df.iloc[:,0], df.iloc[:,1], color='blue', label="Spannung am Widerstand")
# Plot der zweiten Potential-Spalte (Index 2), verschoben um +4.95, in Rot
plt.plot(df.iloc[:,0], df.iloc[:,2] + 4.95, color='red', label="Spannung am Kondensator")
plt.title('Messung: Entladung eines 100μF Kondensators über einen 10kOhm Widerstand in einem RC-Kreis')

plt.xticks()
plt.yticks()

plt.xlabel("Zeit [t] = s")
plt.ylabel("Potenzial [U] = V")

plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()
