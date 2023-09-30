import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as plt
initial_population = 1500
rate = 0.5
Timestep = 0.01
duration = 14
M = 1000
iteration = int(duration/Timestep)
population = initial_population
k = rate * Timestep
t = 0
tl = []
pl = []

for i in range (iteration):
    population = population+k*(1-population/M) * population
    pl.append(population)
    t = i*Timestep
    tl.append(t)
    print(t , population )

plt.plot(tl,pl)
plt.ylim(0,1600)
plt.show()