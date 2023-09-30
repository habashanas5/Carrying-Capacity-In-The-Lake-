import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as plt
population = 10
rate = 0.02
Timestep = 0.01
duration = 500
M = 1000
iteration = int(duration/Timestep)
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
plt.show()
