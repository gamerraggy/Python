#Import numpy to work with numbers and lists of numbers easily
import numpy as np

#Import pylot from matplotlib to help us draw graphs and pictures
import matplotlib.pyplot as plt

#import fits from astropy.io to open and use speical space picture files called FITS
from astropy.io import fits

#Import download_file from astropy.utils.data to grab data from the internet without leaving our code
from astropy.utils.data import download_file

#import log stretch and powerstretch from asropy.visualizatio  to make our space pictures more clear
from astropy.visualization import LogStretch, PowerStretch

#import image normalize from astropy.visualization to help make sure our pictures show up nicely in our graphs
from astropy.visualization.mpl_normalize import ImageNormalize

#function to download a space image stored in a FITS file
image_file = download_file('https://fits.gsfc.nasa.gov/samples/WFPC2ASSNu5780205bx.fits', cache=True)
#Image Url: http://data.astropy.org/tutorials/FITS-images/HorseHead.fits

image_data = fits.getdata(image_file)

import pprint #"pretty print" module
header = fits.getheader(image_file)
pprint.pprint(header)

print('Min:', np.min(image_data))
print('Max:', np.max(image_data))
print('Mean:', np.mean(image_data))
print('Stdev:', np.std(image_data))

plt.figure(figsize=(10,10))#set the image size
plt.imshow(image_data, cmap='cividis')
plt.colorbar()
plt.show()
