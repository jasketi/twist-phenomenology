import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- Settings ---
G = 4.302e-6  # Gravitational constant in (kpc * km^2) / (Msun * s^2)
a0 = 1.2e-10  # Twist-predicted acceleration scale (m/s^2)

# Load SPARC data (replace path if needed)
data = pd.read_csv("data/sparc_masses.csv")

# Expected columns: galaxy, radius_kpc, gbar_m_s2, gobs_m_s2
# Group by galaxy
for name, group in data.groupby("galaxy"):
    r = group["radius_kpc"].values
    gbar = group["gbar_m_s2"].values
    gobs = group["gobs_m_s2"].values

    # Twist prediction using fixed MOND-like interpolation
    gtwist = 0.5 * gbar + np.sqrt(0.25 * gbar**2 + gbar * a0)

    # Plot
    plt.figure()
    plt.title(f"{name} | Twist Fit vs Observed")
    plt.loglog(gbar, gobs, 'ko', label="Observed")
    plt.loglog(gbar, gtwist, 'r-', label="Twist Prediction")
    plt.xlabel("g_bar [m/s²]")
    plt.ylabel("g_obs [m/s²]")
    plt.legend()
    plt.grid(True, which='both', ls='--', alpha=0.5)
    plt.savefig(f"figures/{name}_twist_fit.png")
    plt.close()

print("✅ Twist fits completed for all galaxies.")
