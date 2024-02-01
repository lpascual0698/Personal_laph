import numpy as np 

# Initialize vector to store pi approximation
estim = []

for i in 1:7:
    N = 10^i # Define sample size
    X=np.random.random(N) # Generate first array of N uniform samples
    Y=np.random.random(N) # Generate second array of N uniform samples
    pi_est= 4/N*(sum((np.square(X)+np.square(Y))<=1));
    estim.append(pi_est)

plot(1:7,pi-estim)