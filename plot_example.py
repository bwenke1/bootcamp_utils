import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#Load data
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

#Define ECDF function
def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(data)+1) / len(data)
    return x, y

x, y = ecdf(xa_high)

#Make smooth x-values
x2 = np.linspace(1600, 2500, 400)

#Compute theoretical Normal distribution
fig, ax = plt.subplots(1,1)
cdf_theor = sp.stats.norm.cdf(x2, loc=np.mean(xa_high), scale=np.std(xa_high))
ax.set_xlabel('egg cross sectional area (sq. µm)')
ax.set_ylabel('CDF')
ax.plot(x2, cdf_theor, color='gray')

#Plot real data
#fig, ax = plt.subplots(1,1)
_ = ax.plot(x, y, marker='.', linestyle='none', color='gray', label='high food')


#Make a legend
plt.legend()

plt.show()
