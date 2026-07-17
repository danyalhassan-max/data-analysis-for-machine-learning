# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("data.csv")

# ==========================
# Correlation
# ==========================

print(df.corr())

# ==========================
# Line Plot
# ==========================

# df["Pulse"].plot()
# plt.show()

# ==========================
# Scatter Plot
# ==========================

# df.plot(kind="scatter", x="Duration", y="Maxpulse")
# plt.show()

# ==========================
# Histogram
# ==========================

df["Pulse"].plot(kind="hist")
plt.show()
