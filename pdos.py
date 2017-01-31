
# coding: utf-8

# In[1]:

get_ipython().magic(u'matplotlib inline')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style


# In[2]:

style.use('seaborn-poster')
style.available


# In[3]:

### Build a list to restore the DOS#ID 
dos=[]
selected=[2,4] #To choose the DOS#ID 
for i in selected:
  dos.append(np.loadtxt('DOS' + str(i)))


# In[4]:

### Read these files and restore the data into array

for i, D in enumerate(dos):
   x=D[:, 0] #the first column is the energy
   l1=D[:, 1] #the second column is the s-up orbital
   l2=D[:, 2] #this is the s-down orbital
   l3=D[:, 3] #this is the py-up orbital
   l4=D[:, 4] #this is the py-down orbital
   l5=D[:, 5] #this is the pz-up orbital
   l6=D[:, 6] #this is the pz-down orbital
   l7=D[:, 7] #the second column is the s-up orbital
   l8=D[:, 8] #this is the s-down orbital
   l9=D[:, 9] #this is the py-up orbital
   l10=D[:, 10] #this is the py-down orbital
   l11=D[:, 11] #this is the pz-up orbital
   l12=D[:, 12] #this is the pz-down orbital
   l13=D[:, 13] #this is the py-down orbital
   l14=D[:, 14] #this is the pz-up orbital
   l15=D[:, 15] #this is the pz-down orbital
   l16=D[:, 16] #this is the py-down orbital
   l17=D[:, 17] #this is the pz-up orbital
   l18=D[:, 18] #this is the pz-down orbital

  ###Set the energy level range
   f = (x < 10) & (x > -8)
   x=x[f]
   l1=l1[f]
   l2=l2[f]
   l3=l3[f]
   l4=l4[f]
   l5=l5[f]
   l6=l6[f]
   l7=l7[f]
   l8=l8[f]
   l9=l9[f]
   l10=l10[f]
   l11=l11[f]
   l12=l12[f]
   l13=l13[f]
   l14=l14[f]
   l15=l15[f]
   l16=l16[f]
   l17=l17[f]
   l18=l18[f]
   s_up=l1
   s_down=l2 
   p_up=l3+l5+l7
   p_down=l4+l6+l8
   d_up=l9+l11+l13+l15+l17
   d_down=l10+l12+l14+l16+l18
  
   plt.plot(x,s_up, label="DOSs-up%d" %i)
   plt.plot(x,s_down, label="DOSs-down%d" %i)
   plt.plot(x,p_up, label="DOSp-up%d" %i)
   plt.plot(x,p_down, label="DOSp-down%d" %i)
   plt.plot(x,d_up, label="DOSd-up%d" %i)
   plt.plot(x,d_down, label="DOSd-down%d" %i)
plt.legend(loc=1,fontsize='medium')
plt.savefig('dos.png',dpi=300)

