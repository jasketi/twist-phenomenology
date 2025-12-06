# twist-phenomenology

**Supporting material for the paper:**  
**Jörg Ascher (2025)**  
*“Twist-Topological Phenomenology of Cosmology and Astrophysics”*  


---

## 📚 Purpose

This repository provides scripts, parameters, and documentation for reproducing the numerical results in the above paper. It includes:

- CLASS input files for twist cosmology
- Python scripts for fitting galaxy rotation curves
- Forecasts for black hole ringdown signatures
- Documentation for parameter values and data usage

---

## 🧪 Quickstart (Manual)

1. Patch and compile CLASS (see `patch/twist_patch.diff`)
2. Run with `ini/twist_planck.ini`
3. Fit SPARC data with `scripts/fit_sparc.py`
4. Run QNM forecasts with `scripts/ringdown_forecast.py`

→ To enable the twist fluid, apply the patch file `patch/twist_patch.diff`  
   using `patch -p1 < patch/twist_patch.diff` inside the CLASS root directory.  
   Alternatively, add the few lines shown there manually to `background.c`.


---

## 📂 Contents

- `CODEBOOK.md` – full technical documentation
- `scripts/` – Python scripts for plotting and fitting
- `ini/` – CLASS input files
- `patch/` – patch file for CLASS source
- `figures/` – output plots
- `data/` – referenced datasets (SPARC, Planck, etc.)

---

## 📜 Citation

If you use this repository, please cite:

> Ascher, J. (2025). *Twist-Topological Phenomenology of Cosmology and Astrophysics*. arXiv:YYYY.NNNNN

---

