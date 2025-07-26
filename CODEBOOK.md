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

### Step-by-step:

1. **Patch CLASS**
   - Use `patch/twist_patch.diff` to add `w = 1` fluid with stiff scaling `ρ ∝ a⁻⁶`

2. **Run CLASS**
   - Use provided file: `ini/twist_planck.ini`
   - Output: H₀, σ₈, ∆N_eff (via a⁻⁶ component)

3. **Fit Galaxy Rotation Curves**
   - Download SPARC data as described above
   - Run `scripts/prepare_sparc.py` to convert to `sparc_masses.csv`
   - Then run `scripts/fit_sparc.py` to compare with twist prediction

4. **Ringdown Forecast**
   - Run `scripts/ringdown_forecast.py` to calculate ∆f/f and compare to ET reach

5. **Plotting and Comparison**
   - Use `scripts/make_plots.py` to regenerate paper figures (e.g. constraints, histograms)

---

## 6. Remarks

- All calculations use public data and standard cosmology tools.
- No extra free parameters beyond `R_⊖` introduced.
- This is not a simulation framework – just a reproducibility record of published work.

---

## License

MIT License.  
Please cite:  
_Ascher, J. (2025). Twist-Topological Phenomenology of Cosmology and Astrophysics, arXiv:YYYY.NNNNN_

