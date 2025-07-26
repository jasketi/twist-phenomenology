# CODEBOOK.md

**Supporting Calculations and Data for**  
**“Twist-Topological Phenomenology of Cosmology and Astrophysics”**  
_Last updated: 2025-07-26_

---

## 1. Purpose

This document explains all physical parameters, datasets, tools, and scripts used to generate the numerical results in the paper.

It is intended to ensure full transparency and reproducibility for interested readers and researchers.

---

## 2. Key Model Ingredients

| Symbol / Quantity     | Description                                        | Value / Use                          |
|------------------------|----------------------------------------------------|---------------------------------------|
| `Ω_{w=1}`              | Energy density of twist-induced stiff fluid        | ~ 2.4 × 10⁻⁴ (fixed)                  |
| `R_⊖`                  | Twist scale (from BBN: R > 90 Mpc)                 | Scanned across 90–180 Mpc             |
| `α_em`                 | Fine-structure constant                            | Interpreted as return angle (2π/137)  |
| `Δf/f` (Ringdown)      | QNM frequency shift                                | ~ 0.6%                                |
| `Υ_*`                  | Stellar mass-to-light ratio (SPARC fits)           | Fixed in parity-free variant          |

---

## 3. Tools and Simulations

| Tool / Framework       | Purpose / Use                                      | Source / Notes                        |
|------------------------|----------------------------------------------------|----------------------------------------|
| `CLASS v3.3`           | Boltzmann solver with added `w = 1` fluid          | https://github.com/lesgourg/class_public |
| `Python 3.x`           | Plotting, χ² evaluation, MCMC diagnostics          | NumPy, SciPy, Matplotlib               |
| `MontePython` (opt.)   | MCMC sampling of `R_⊖` and likelihoods             | Used for posterior scans               |
| `ET Forecast`          | QNM detectability simulations                      | Based on ET Design Report              |

---

## 4. Data Sources

| Dataset                 | Use / Constraint                     | Availability / Reference |
|--------------------------|---------------------------------------|---------------------------|
| Planck 2018              | TT, TE, EE + lensing                 | https://pla.esac.esa.int |
| ACT DR4                  | TB/EB parity-violating spectra       | https://act.princeton.edu |
| SPARC v2.3               | Galaxy rotation curve data. Used to derive g_obs and g_bar for twist model validation. Not included in this repository. |  
Publicly available at: [http://astroweb.cwru.edu/SPARC/](http://astroweb.cwru.edu/SPARC/)

→ Please download the file `SPARC_all.csv` or `SPARC_all_rotcurves.csv` manually.  
→ You may use the helper script `scripts/prepare_sparc.py` to convert it to `sparc_masses.csv` format.

---

## 5. Reproduction Steps

This section outlines how to reproduce the main results of the paper using the provided files and a patched version of CLASS.

### Step-by-step:

1. **Patch CLASS**
   - Use the patch file located at `patch/twist_patch.diff` to add a `w = 1` twist fluid with energy density scaling \( \rho \propto a^{-6} \)
   - See Section 6 below for detailed instructions

2. **Run CLASS**
   - Use the input file `ini/twist_planck.ini`
   - This will output values for H₀, σ₈, and ∆N_eff with the twist component included

3. **Fit Galaxy Rotation Curves**
   - Download SPARC data as described in Section 4
   - Run `scripts/prepare_sparc.py` to convert it into `data/sparc_masses.csv`
   - Run `scripts/fit_sparc.py` to perform twist-based fits and generate plots

4. **Ringdown Forecast**
   - Run `scripts/ringdown_forecast.py` to compute the predicted ∆f/f as a function of R_⊖
   - The script creates `figures/ringdown_forecast.png` for visual comparison with ET sensitivity

5. **Plotting and Summary**
   - (Optional) Use `scripts/make_plots.py` to re-create constraint plots and histograms as shown in the paper

---

## 6. CLASS Patch Instructions

The twist fluid (w = 1) is not part of standard CLASS. You must either apply a small patch (recommended) or add it manually.

### 6.1 Option A – Apply the provided patch

1. Clone the official CLASS repository:
   git clone https://github.com/lesgourg/class_public.git
   cd class_public

2. Apply the patch:
   patch -p1 < path/to/patch/twist_patch.diff

3. Compile CLASS:
   make

After patching, you can activate the twist fluid in your `.ini` file via:

use_twist_fluid = yes  
Omega_twist = 2.4e-4

---

### 6.2 Option B – Manual integration (if patching is not possible)

To manually add the twist fluid, edit the file `source/background.c` in CLASS.

**a) In the energy density sum:**

if (pba->has_twist == _TRUE_) {  
  rho_twist = pba->Omega0_twist * rho_crit_today / pow(a,6);  
  pressure_twist = rho_twist;  
  *rho_tot += rho_twist;  
  *p_tot += pressure_twist;  
}

**b) In `background_read_parameters()` (read from ini):**

class_read_flag("use_twist_fluid", pba->has_twist);  
class_read_double("Omega_twist", pba->Omega0_twist);

**c) In `background_init()` (default values):**

pba->has_twist = _FALSE_;  
pba->Omega0_twist = 0.0;

Then compile CLASS as usual:
make

---

After either method, CLASS will recognize and use the twist fluid throughout background evolution and perturbation handling.

---

## License

MIT License.  
Please cite:  
_Ascher, J. (2025). Twist-Topological Phenomenology of Cosmology and Astrophysics, arXiv:YYYY.NNNNN_

