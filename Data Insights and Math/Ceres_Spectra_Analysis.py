from astropy.io import fits
from specutils import Spectrum1D
from astropy.visualization import quantity_support
import matplotlib.pyplot as plt
file = fits.open('Data Insights and Math/ceres.fits')
# file.info()

header = file[0].header
# print(header[:10])

del header['BUNIT']


spectra = Spectrum1D.read(file)

quantity_support() # we use quantity_support to numerically convert the values before plotting them using matplotlib
fig, ax = plt.subplots()
ax.set_title("1D Spectra Visualization of Ceres")
ax.step(spectra.spectral_axis, spectra.flux)
plt.show()