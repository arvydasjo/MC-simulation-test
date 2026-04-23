import numpy as np
import time
import platform



start = time.time()

S0 = 100
mu = 0.08
sigma = 0.20
T = 1
N = 252
dt = T / N

simulations = 500000

Z = np.random.normal(size=(simulations, N))
log_returns = (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z
S = S0 * np.exp(np.cumsum(log_returns, axis=1))[:, -1]

mean_val = np.mean(S)
median_val = np.median(S)
var_5 = np.percentile(S, 5)

end = time.time()
exec_time = end - start

print("Vidutine kaina:", mean_val)
print("Mediana:", median_val)
print("VaR 5%:", var_5)
print("Vykdymo laikas:", exec_time)

if platform.system() == "Linux":
    env = "vm"
else:
    env = "local"

filename = f"results_{env}.txt"

with open(filename, "w") as f:
    f.write(f"Environment: {env}\n")
    f.write(f"MC simulation number: {simulations}\n")
    f.write(f"Average price: {mean_val}\n")
    f.write(f"Median: {median_val}\n")
    f.write(f"VaR 5%: {var_5}\n")
    f.write(f"Execution time: {exec_time}\n")