# Calculate sea-level contribution using volume above floatation
# Following ISMIP6: https://doi.org/10.5194/tc-14-3071-2020; https://doi.org/10.1029/2024EF004561; https://zenodo.org/records/10528582
# Converting Vaf directly to freshwater
# Suffix 0 refers to reference state.

import numpy as np
from slc import sl_constants as c

# Vaf assuming B (and S) in an absolute reference frame like in A2020
def get_vaf(H,B,S,A):
  hf  = np.maximum(S-B,0.0)*c.RHOSW/c.RHOI
  hall= np.maximum(H-hf,0.0)
  vol = np.sum(hall*A)
  return vol

def get_slc_vaf(H0,H,B0,B,S0,S,A):
  # ISMIP6: Converting Vaf directly to freshwater
  sle_af_ref = get_vaf(H0,B0,S0,A) / c.AO * c.RHOI/c.RHOFW
  sle_af = get_vaf(H,B,S,A) / c.AO * c.RHOI/c.RHOFW
  slc_af = -(sle_af - sle_af_ref)
  return slc_af 


# Vaf assuming B is given relative to sea level at that time or S=0 
def get_vaf_HBA(H,B,A):
  hf  = np.maximum(-B,0.0)*c.RHOSW/c.RHOI
  hall= np.maximum(H-hf,0.0)
  vol = np.sum(hall*A)
  return vol

def get_slc_vaf_HBA(H0,H,B0,B,A):
  # ISMIP6: Converting Vaf directly to freshwater
  sle_af_ref = get_vaf_HBA(H0,B0,A) / c.AO * c.RHOI/c.RHOFW
  sle_af = get_vaf_HBA(H,B,A) / c.AO * c.RHOI/c.RHOFW
  slc_af = -(sle_af - sle_af_ref)
  return slc_af 


# Grounded ice volume change 
def get_vgr(H,B,S,A):
    mask_gr = H > (B-S)*c.RHOSW/c.RHOI 
    vol = np.sum((H*A)[ mask_gr ])
    return vol

def get_slc_vgr(H0,H,B0,B,S0,S,A):
  sle_gr_ref = get_vgr(H0,B0,S0,A) / c.AO * c.RHOI/c.RHOFW
  sle_gr = get_vgr(H,B,S,A) / c.AO * c.RHOI/c.RHOFW
  slc_gr = -(sle_gr - sle_gr_ref)
  return slc_gr


# Total ice volume change 
def get_vtot(H,A):
    H_tot = H *c.RHOSW/c.RHOI 
    vol = np.sum(H_tot*A)
    return vol

def get_slc_vtot(H0,H,A):
  sle_tot_ref = get_vtot(H0,A) / c.AO * c.RHOI/c.RHOFW
  sle_tot = get_vtot(H,A) / c.AO * c.RHOI/c.RHOFW
  slc_tot = -(sle_tot - sle_tot_ref) 
  return slc_tot


# For global mean sea-level calculations 
def get_mean(R,A):
    mean = np.sum(R*A)
    return mean

def get_mean_diff(R0,R,A,Atot):
  mean_ref = get_mean(R0,A) / Atot 
  mean = get_mean(R,A) / Atot
  mean_diff = mean - mean_ref
  return mean_diff
