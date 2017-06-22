#Load data
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

def bs_replicate(data, func=np.mean):
    """Compute a bootstrap replicate from data."""
    bs_sample = np.random.choice(data, replace=True, size=len(data))
    return func(bs_sample)

#Generate lots of replicates
n_reps = 100000

#Initialize replicates array
bs_reps_2012 = np.empty(n_reps)

#Compute replicates
for i in range(n_reps):
    bs_reps_2012[i] = bs_replicate(bd_2012, func=np.mean)
