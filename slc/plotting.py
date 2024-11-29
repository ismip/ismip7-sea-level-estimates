# Plotting 

import cartopy.crs as ccrs
from netCDF4 import Dataset, date2index
import numpy as np
import matplotlib.pyplot as plt

# Plotting a global field
def plot_global(field,lons,lats,label):

  # create figure, axes instances.
  fig = plt.figure(figsize=(10, 5))
  #ax = fig.add_axes([0.05,0.05,0.9,0.9])
  ax = fig.add_subplot(1, 1, 1, projection=ccrs.Robinson())
    
  # make the map global rather than have it zoom in to
  # the extents of any plotted data
  #ax.set_global()

  #ax.stock_img()
  ax.coastlines(lw=0.5,color='k')

  im1 = ax.pcolormesh(lons,lats,field,cmap=plt.cm.RdBu,transform=ccrs.PlateCarree(),shading='nearest')

  ax.gridlines(lw=0.5,color='grey')

  # add colorbar
  cb = fig.colorbar(im1,ax=ax,orientation="vertical",format='$%.1f$',shrink=0.6)
  cb.set_label(label)
    
  # add a title.
  #ax.set_title()

  plt.show()
