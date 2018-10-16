import numpy as np
import matplotlib.pyplot as plt



__author__ = "Saeed Moghimi"
__copyright__ = "Copyright 2017, NOAA"
__license__ = "GPL"
__version__ = "1.1"
__email__ = "moghimis@gmail.com"


"""
Simple routine to plot a descriptive plot for bias correction

"""



def set_leg(ax, loc = None):
    if loc is None:
       loc = 'best'
    #loc = np.random.randint(0,10)
    leg = ax.legend(loc = loc ,ncol=5,fontsize=11)
    try:
        frame=leg.get_frame()
        frame.set_edgecolor('None')
        frame.set_facecolor('None')
    except:
        pass



plt.xkcd()
plt.close('all')

plt.figure(figsize=(10,5))
ax = plt.gca()
nx =200
x  =     np.linspace(0,50,nx)
y1 = 1 * np.sin(x)



#overshoot signal
nx2 = 100
x2 = np.linspace(0,3.14    ,nx2)
y2 = 3 * np.sin(x2) ** 4

# storm surge obs
y3 = y1 * 1
ns = 50
y3 [ns:ns+nx2] =  y2[0:nx2] + y1[ns:ns+nx2]
y3 = y3 + 1




# storm surge simulation
y4 = y1 * 1
ns = 50
y2 = 2.5 * np.sin(x2) ** 12
y4 [ns:ns+nx2] =  y2[0:nx2] + y1[ns:ns+nx2]
y4 = y4 + 0.5


line1,  = plt.plot(x,  y1, 'r-', linewidth=2 , label= 'Tide')


line3,  = plt.plot(x,  y3, 'k-', linewidth=3 , label= 'Obs.')
line31, = plt.plot(x,  y3.mean()* np.ones_like(y3), 'k--', linewidth=2 , label= 'mean Obs.')


line4,  = plt.plot(x,  y4, 'g', linewidth=3 , label= 'Pred.')
line41,  = plt.plot(x,  y4.mean()* np.ones_like(y3), 'g--', linewidth=2 , label= 'mean Pred.')
dashes = [10, 5] # 10 points on, 5 off, 100 on, 5 off
#line4.set_dashes(dashes)



line11, = plt.plot(x,  0* np.ones_like(y3), 'k-', linewidth=1 )
plt.setp( ax, 'xticklabels', [] )
set_leg(ax)
plt.ylabel('Elevation [m]')
plt.xlabel('Time')
plt.ylim (-3,7)


plt.savefig('bias_corec.png', dpi=450)
plt.show()



















