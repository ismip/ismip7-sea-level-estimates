# Calculate sea-level contribution according to G2020
# https://doi.org/10.5194/tc-14-833-2020
# Symbols are the same as in the paper.
# Suffix 0 refers to reference state.
# z0 in eq 13 and 14 is called zn here to avoid confusion with the reference symbols.

import numpy as np
from slc import sl_constants as c


def get_vaf_G2020(H,b,zn,A):
# eq. 1/13 in https://doi.org/10.5194/tc-14-833-2020
  hf  = np.minimum(b-zn,0.0)*c.RHOSW/c.RHOI
  hall= np.maximum(H+hf,0.0)
  vol = np.sum(hall*A)
  return vol

def get_slc_af_owv_G2020(H0,H,b0,b,zn0,zn,A):
  # eq. 2,3 in https://doi.org/10.5194/tc-14-833-2020
  # Note division by RHOSW to get ocean water volume that would be displaced.  
  sle_af_owv_ref = get_vaf_G2020(H0,b0,zn0,A) / c.AO * c.RHOI/c.RHOSW
  sle_af_owv = get_vaf_G2020(H,b,zn,A) / c.AO * c.RHOI/c.RHOSW
  slc_af_owv = -(sle_af_owv - sle_af_owv_ref)
  return slc_af_owv 


def get_vpov_G2020(b,zn,A):
  # eq. 8/14 in https://doi.org/10.5194/tc-14-833-2020
  # For eq. 8, set zn=0.0
  vol = np.sum((np.maximum(zn-b,0.0)*A))
  #print(zn.flat[0],b.flat[1],zn.flat[0]-b.flat[0])
  return vol

def get_slc_pov_G2020(b0,zn0,b,zn,A):
  # eq. 9 in https://doi.org/10.5194/tc-14-833-2020
  # slc as difference between two states
  sle_pov_ref = get_vpov_G2020(b0,zn0,A) / c.AO
  sle_pov = get_vpov_G2020(b,zn,A) / c.AO
  slc_pov = -(sle_pov - sle_pov_ref)
  return slc_pov
  
  
def get_vden_G2020(H,A):
  # eq. 10 in https://doi.org/10.5194/tc-14-833-2020
  vol = np.sum((H*(c.RHOI/c.RHOFW-c.RHOI/c.RHOSW)*A))
  return vol
  
def get_slc_den_G2020(H0,H,A):
  # eq. 11 in https://doi.org/10.5194/tc-14-833-2020
  # slc as difference between two states
  sle_den_ref = get_vden_G2020(H0,A) / c.AO
  sle_den = get_vden_G2020(H,A) / c.AO
  slc_den = -(sle_den - sle_den_ref)
  return slc_den


def get_slc_G2020(H0,H,b0,b,zn0,zn,A):
  # eq. 12/15 in https://doi.org/10.5194/tc-14-833-2020
  # For eq. 12, set zn=zn0=0.0
  slc_af = get_slc_af_owv_G2020(H0,H,b0,b,zn0,zn,A)
  slc_pov = get_slc_pov_G2020(b0,zn0,b,zn,A)
  slc_den = get_slc_den_G2020(H0,H,A)
  slc = slc_af + slc_pov + slc_den
  return slc


# grounded ice volume change 
def get_vgr_G2020(H,b,sl,A):
  # eq. 4 in https://doi.org/10.5194/tc-14-833-2020  
    mask_gr = H > (b-sl)*c.RHOSW/c.RHOI 
    vol = np.sum((H*A)[ mask_gr ])
    return vol

def get_slc_gr_G2020(H0,H,b0,b,sl0,sl,A):
  sle_gr_ref = get_vgr_G2020(H0,b0,sl0,A) / c.AO * c.RHOI/c.RHOSW
  sle_gr = get_vgr_G2020(H,b,sl,A) / c.AO * c.RHOI/c.RHOSW
  slc_gr = -(sle_gr - sle_gr_ref) 
  return slc_gr


# total ice volume change 
def get_vtot_G2020(H,A):
    H_tot = H *c.RHOSW/c.RHOI 
    vol = np.sum(H_tot)
    return vol

def get_slc_tot_G2020(H0,H,A):
  sle_tot_ref = get_vtot_G2020(H0,A) / c.AO * c.RHOI/c.RHOSW
  sle_tot = get_vtot_G2020(H,A) / c.AO * c.RHOI/c.RHOSW
  slc_tot = -(sle_tot - sle_tot_ref) 
  return slc_tot
