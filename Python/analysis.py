import numpy as np # linear algebra
np.set_printoptions(threshold=np.inf)
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
        
### Analysis starts below ###

# Please find required dataset (will also download PDF of methods) at https://www.kaggle.com/datasets/dasmehdixtr/human-gait-phase-dataset 
# If downloading, make sure to change the path for the required files.

f1 = pd.read_csv('../input/human-gait-phase-dataset/data/GP1_1.0_force.csv', header=[0]) # Reads in force plate data.

m1 = pd.read_csv('../input/human-gait-phase-dataset/data/GP1_1.0_marker.csv', header=[0]) # Reads in marker position data. 

foot_length = 0.27 # foot length in metres.
mall_height = 0.1 # height of the lateral malleolus in metres.
mall_width = 0.063 # width of the lateral malleolus in metres. 
mass = 66.6 # subject mass. In this case, uses average of all subjects. 
T = 200 # Sampling frequency used for motion capture. 

##### ONLY CHANGE ABOVE VALUES #####

fm = 0.0083*mass+254.5*foot_length*mall_height*mall_width-0.065 # Calculates mass of the foot. 

f2 = f1[['FP1_x', 'FP1_y', 'FP1_z']] # Specifies only the left foot force plate data.

m2 = m1[['L_FCC_x','L_FM1_x','L_FM2_x','L_FM5_x','L_FCC_y','L_FM1_y','L_FM2_y','L_FM5_y','L_FCC_z','L_FM1_z','L_FM2_z','L_FM5_z']]
# Specifies only the left foot marker data. 

c1 = f2['FP1_x'] 
c2 = f2['FP1_y'] 
c3 = f2['FP1_z']

fx_i = np.interp(np.arange(0,len(c1),len(f1)/len(m1)),np.arange(0,len(c1)),c1) # Uses linear interpolation to scale force curve to length of marker data.
fy_i = np.interp(np.arange(0,len(c2),len(f1)/len(m1)),np.arange(0,len(c2)),c2)
fz_i = np.interp(np.arange(0,len(c3),len(f1)/len(m1)),np.arange(0,len(c3)),c3)
        
for x in range(5,len(fz_i)-1): # Finds index for start of first stance phase.
    if fz_i[x-5] < 1 and fz_i[x-4] < 1 and fz_i[x-3] < 1 and fz_i[x-2] < 1 and fz_i[x-1] < 1 and fz_i[x] > 2:
        a = x
        break

for x in range(a,len(fz_i)-5): # Finds index for end of first stance phase. 
    if fz_i[x+5] < 1 and fz_i[x+4] < 1 and fz_i[x+3] < 1 and fz_i[x+2] < 1 and fz_i[x+1] < 1 and fz_i[x] > 1:
        b = x
        break
        
fx_i2 = fx_i[a:b] # Force plate data of only first stance phase. 
fy_i2 = fy_i[a:b]
fz_i2 = fz_i[a:b]

m3 = m2[a:b] # Marker data of only first stance phase. 

COM_x = (0.44*(m3['L_FM2_x']-m3['L_FCC_x'])+m3['L_FCC_x']) # Calculates position of the foot COM in x-direction (anterior-posterior).
COM_z = (0.44*(m3['L_FM2_z']-m3['L_FCC_z'])+m3['L_FCC_z']) # Same as above, in z-direction (vertical).

vel_x = []
vel_z = []
acc_x = []
acc_z = []

for x in range(a+1,b-1): # Uses central difference method to numerically differentiate COM position data into COM velocity data in the x-direction.
    vel1 = (COM_x[x+1]-COM_x[x-1])/(2*1/T)
    vel_x.append(vel1)

for x in range(a+1,b-1): # Same as above, for z-direction. 
    vel2 = (COM_z[x+1]-COM_z[x-1])/(2*1/T)
    vel_z.append(vel2)

c = round(vel_x[int(round(len(vel_x)/2,0))],1) # Finds fixed velocity of treadmill.

vel_x2 = vel_x - c # Corrects for fixed velocity of treadmill. 
    
for x in range(1,len(vel_x2)-1): # Same differentiation used on velocity to find COM acceleration in x-direction.
    acc1 = (vel_x2[x+1]-vel_x2[x-1])/(2*1/T)
    acc_x.append(acc1)

for x in range(1,len(vel_z)-1): # Same as above, for z-direction. 
    acc2 = (vel_z[x+1]-vel_z[x-1])/(2*1/T)
    acc_z.append(acc2)
    
acc_x2 = np.array(acc_x) # Turns list output of differentiation into numpy array. 

acc_z2 = np.array(acc_z)

fx_i3 = np.delete(fx_i2,[0, 1, len(fx_i2)-2,len(fx_i2)-1]) # Removes the first two and last two entries of force data to synchronise length to acceleration data length.

fz_i3 = np.delete(fz_i2,[0, 1, len(fz_i2)-2,len(fz_i2)-1])

ank_x = acc_x2*fm - fx_i3 # Uses dynamic equilibrium equation to solve for force at the ankle joint in the x-direction.

ank_z = acc_z2*fm - fm*9.81 - fz_i3 # Same as above, for z-direction. 

ank_x2 = np.interp(np.arange(0,len(ank_x),len(ank_x)/100), np.arange(0,len(ank_x)),ank_x) # Uses linear interpolation to scale ankle joint force to 100 data points, each corresponding to 1% of stance phase. 
ank_z2 = np.interp(np.arange(0,len(ank_z),len(ank_z)/100), np.arange(0,len(ank_z)),ank_z)

fz_i4 = np.interp(np.arange(0,len(fz_i3),len(fz_i3)/100), np.arange(0,len(fz_i3)),fz_i3) # Normalised GRF to stance.
fx_i4 = np.interp(np.arange(0,len(fx_i3),len(fx_i3)/100), np.arange(0,len(fx_i3)),fx_i3)

COM_z4 = np.interp(np.arange(0,len(COM_z),len(COM_z)/100), np.arange(0,len(COM_z)),COM_z) # Normalised moving COM position to stance.
COM_x4 = np.interp(np.arange(0,len(COM_x),len(COM_x)/100), np.arange(0,len(COM_x)),COM_x)

d = (b-a)/T # Length of stance phase in seconds. 

COM_x2 = []

vel_x3 = pd.Series(vel_x2)

for x in range(0,len(vel_x3)-1): # Uses trapezoid rule to numerically integrate normalised velocity to find normalised COM in the x-direction.
    if x == 0:
        COM1 = ((x+1)/T-x/T) * 0.5*(vel_x3[x]+vel_x3[x+1])
    else:
        COM1 = ((x+1)/T-x/T) * 0.5*(vel_x3[x]+vel_x3[x+1]) + COM1
    COM_x2.append(COM1)

COM_x2 = np.delete(COM_x2,[0])

vel_x3 = []

COM_x3 = np.interp(np.arange(0,len(COM_x2),len(COM_x2)/100), np.arange(0,len(COM_x2)),COM_x2) # Normalised static COM position to stance.
vel_x4 = np.interp(np.arange(0,len(vel_x2),len(vel_x2)/100), np.arange(0,len(vel_x2)),vel_x2) # Normalised zeroed velocity position to stance.
vel_x5 = np.interp(np.arange(0,len(vel_x),len(vel_x)/100), np.arange(0,len(vel_x)),vel_x) # Normalised velocity position to stance.

for x in range(1,len(COM_x2)-1):  
    vel3 = (COM_x2[x+1]-COM_x2[x-1])/(2*1/T)
    vel_x3.append(vel3)
    
#plt.plot(vel_x2)
#plt.plot(vel_x3)
#plt.plot(vel_x)
#plt.plot(COM_x2)

plt.plot(ank_x2, label = 'Anterior-Posterior') # Plots ankle force figure. 
plt.plot(ank_z2, label = 'Vertical')
plt.legend(loc = 'upper right',bbox_to_anchor=(1.2,1.05))
plt.xlabel('% of Stance Phase')
plt.ylabel('Force (N)')
plt.title('Ankle Force')
#plt.savefig('KNES381')
