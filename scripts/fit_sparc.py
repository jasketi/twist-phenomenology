import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# --- Settings ---
a0 = 1.2e-10  # Twist-predicted acceleration scale (m/s^2)
input_file = "data/sparc_masses.csv"

# Check for required data file
if not os.path.exists(input_file):
    raise FileNotFoundError(
        f"\n❌ Data file '{input_file}' not found.\n\n"
        "Please download SPARC rotation curve data from:\n"
        "→ http://astroweb.cwru.edu/SPARC/\n\n"
        "Then use the script 'scripts/prepare_sparc.py' to convert it to the required format.\n"
    )

# Load preprocessed SPARC data
df = pd.read_csv(input_file)

# Group by galaxy and fit
for name, group in df.groupby("galaxy"):
    r = group["radius_kpc"].values
    gbar = group["gbar_m_s2"].values
    gobs = group["gobs_m_s2"].values

    # Twist prediction
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
