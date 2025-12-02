import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("P12_Messung_10kOhm_2.csv")

plt.figure(figsize=(10,6))

# Plot der ersten Potential-Spalte (Index 1) in Blau
plt.plot(df.iloc[:,0], df.iloc[:,1], color='blue')
# Plot der zweiten Potential-Spalte (Index 2), verschoben um +4.95, in Rot
plt.plot(df.iloc[:,0], df.iloc[:,2] + 4.95, color='red')

plt.xlabel("Zeit (min)")
plt.ylabel("Potenzial (V)")

plt.grid(True)
plt.tight_layout()
plt.show()
