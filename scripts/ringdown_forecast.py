import numpy as np
import matplotlib.pyplot as plt

# --- Physical constants ---
reference_R = 120  # Mpc
ref_shift = 0.0061  # Reference shift at R = 120 Mpc

# Define twist radii (in Mpc)
R_vals = np.linspace(90, 180, 100)

# Calculate fractional shifts ∆f/f
shift_vals = ref_shift * (reference_R / R_vals)**2

# --- Plotting ---
plt.figure(figsize=(8, 5))
plt.plot(R_vals, 100 * shift_vals, label="Twist Prediction", color='crimson')
plt.axhline(0.1, color='gray', linestyle='--', label="ET sensitivity threshold (~0.1%)")

plt.xlabel("Twist Radius R⊕ [Mpc]")
plt.ylabel("QNM Frequency Shift Δf/f [%]")
plt.title("Gravitational Ringdown Prediction vs. Einstein Telescope Sensitivity")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.savefig("figures/ringdown_forecast.png")
plt.show()

print("✅ Ringdown forecast plot saved as figures/ringdown_forecast.png")
