import numpy as np

#Load data
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

def bs_replicate(data, func=np.mean):
    """Compute a bootstrap replicate from data."""
    bs_sample = np.random.choice(data, replace=True, size=len(data))
    return func(bs_sample)

def draw_bs_reps(data, func=np.mean, size=10000):
    """Draw bootstrap replicates from 1d data."""
    return np.array([bs_replicate(data, func=func) for _ in range(size)])
