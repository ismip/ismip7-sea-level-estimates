# Plotting 

from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset, date2index
import numpy as np
import matplotlib.pyplot as plt

# Plotting a global field
def plot_global(field,lons,lats):

  # create figure, axes instances.
  fig = plt.figure()
  ax = fig.add_axes([0.05,0.05,0.9,0.9])
  
  # create Basemap instance.
  # coastlines not used, so resolution set to None to skip
  # continent processing (this speeds things up a bit)
  m = Basemap(projection='kav7',lon_0=0,resolution=None)
  
  # draw line around map projection limb.
  # color background of map projection region.
  # missing values over land will show up this color.
  m.drawmapboundary(fill_color='0.3')
  
  # plot field
  im1 = m.pcolormesh(lons,lats,field,cmap=plt.cm.jet,latlon=True)
  
  # draw parallels and meridians, but don't bother labelling them.
  m.drawparallels(np.arange(-90.,99.,30.))
  m.drawmeridians(np.arange(-180.,180.,60.))
  
  # add colorbar
  cb = m.colorbar(im1,"bottom", size="5%", pad="2%")
  # add a title.
  #ax.set_title('SST and ICE analysis for %s'%date)
  plt.show()
