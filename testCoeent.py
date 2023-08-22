# !{sys.executable} -m pip install qutip
import numpy as np
import matplotlib.pyplot as plt
from arc import *  # Import ARC (Alkali Rydberg Calculator)
from qutip import *
from scipy.fft import fft, ifft
from scipy import constants 
from Alk_atom import alk_atom
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D 
from matplotlib import cm  

#setup constants: 
N = 20 # size of the Hilbert space 
alpha=np.linspace(0.01,3,10) # values for the coherent state amplitude 
a = destroy(N) #annihilation operator 
D = displace(N,alpha[0]) # Displacement 
xvec = np.linspace(-9,9,300) 
X,Y = np.meshgrid(xvec, xvec)

k=1 # counter 
for x in alpha: 

#     # Define the cat state. It is a coherent superposition of two coherent states. 
#     # Each coherent state is created by the displacement operator acting on the vacuum. 
#     # the unit() function makes sure that the overall state is normalized. 

    psi=(displace(N,x)*basis(N,0)-displace(N,-1*x)*basis(N,0)).unit();

    # plot the wigner function 
    W=wigner(psi,xvec,xvec) 
    fig =plt.figure() 
    ax = Axes3D(fig,azim=-62.5,elev=25) 
    ax.plot_surface(X, Y, W, cstride=2, cmap=cm.jet,lw=.1) 
    ax.set_xlim3d(-9,9) 
    ax.set_xlim3d(-9,9) 
    ax.set_zlim3d(-.2,0.2) 
    ax.set_axis_off() 
    plt.show()
    # ax.set_frame_on('false') 