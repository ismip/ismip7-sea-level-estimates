# ismip7-sea-level-estimates
Python scripts to calculate sea-level estimates from ice sheet model simulations


## Jupyter notebooks

```compare_slc_PISMVILMA.ipynb```

```compare_slc_PISMVILMA_global.ipynb```

Juypter notebooks make use of the `slc` tools and model output data on Ghub (https://theghub.org/projects/ismip7sealevel). This Ghub project aims at testing different approaches to estimate sea-level change from ice sheet and bedrock changes. Ice sheet model output data in ISMIP are defined on a regional regular grid in stereographic projection (https://www.climate-cryosphere.org/wiki/index.php?title=Regridding_with_CDO), while sea-level models use a global grid. 


## Dataset ismip2300-coupled

This is model output from a coupled PISM-VILMA simulation with forcing and 175 yr historical spinup analogous to the PIK_PISM contribution in

- Seroussi, H., Pelle, T., Lipscomb, W. H., Abe‐Ouchi, A., Albrecht, T., Alvarez Solas, J., et al. (2024). Evolution of the Antarctic Ice Sheet over the next three centuries from an ISMIP6 model ensemble. Earth&amp;amp;#39;s Future, 12, e2024EF004561. https://doi.org/10.1029/2024EF004561
but here interactively coupled every model year to the GIA and sea-level model VILMA, according to

- Albrecht, T., Bagge, M., and Klemann, V.: Feedback mechanisms controlling Antarctic glacial-cycle dynamics simulated with a coupled ice sheet–solid Earth model, The Cryosphere, 18, 4233–4255, https://doi.org/10.5194/tc-18-4233-2024 , 2024.
PISM ice sheet simulations were performed on a Antarctic polar stereographic projected (https://epsg.io/3031) ISMIP grid with 8km resolution (761x761). Globally gravitationally consistent and mass conserving VILMA simulations were performed on a n256 Gauss-Legendre grid (1024x512) for a 3D Earth structure, based on

- Bagge, M., Klemann, V., Steinberger, B., Latinovi ́ c, M., and Thomas, M.: Glacial-Isostatic Adjustment Models Using Geodynamically Constrained 3D Earth Structures, Geochem. Geophys. Geosyst., 22, e2021GC009853, https://doi.org/10.1029/2021GC009853 , 2021.

contact: albrecht@pik-potsdam.de

