# ... import statements ...
df = pd.read_csv("P12_Messung_100kOhm_3.csv")

t = df.iloc[:,0]                  # Zeit in Spalte 0
V = df.iloc[:,2] + 4.95           # Verschobenes Potential (rot) in Spalte 2

# Auswahl des Datenbereichs für den Fit (Zeit zwischen 0 und 10 Minuten)
mask = (t >= 0) & (t <= 10)
t_sel = t[mask]
V_sel = V[mask]

logV = np.log(V_sel)              # Logarithmierung der ausgewählten Potentialwerte

# Lineare Regression: np.polyfit(x-Werte, y-Werte, Grad des Polynoms)
m, b = np.polyfit(t_sel, logV, 1) # m ist die Steigung (Steigung = -1/tau)

print("Steigung =", m)
