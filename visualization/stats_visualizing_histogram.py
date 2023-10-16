
# ## SECTION: Visualizing data
# ### Histograms
# 

# In[ ]:


# import libraries
import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


## create data for the histogram

# number of data points
n = 1000

# generate data - log-normal distribution
data = np.exp( np.random.randn(n)/2 )


# In[ ]:


# show as a histogram

# number of histogram bins
k = 40

plt.hist(data,bins=k)
plt.show()


# In[ ]:


# another option
y,x = np.histogram(data,bins=k)

# bin centers
xx = (x[1:]+x[:-1])/2

plt.plot(xx,y)
plt.show()


# In[ ]:




