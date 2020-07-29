import numpy as np
import matplotlib.pyplot as plt
x = 5
print(np.square(x))
print(pow(x,3))
theta = 30
print('sin(theta) =',np.sin(theta)) #so the degree is in radians
print('sin(pi /6) =',np.sin(np.pi /6))
print('cos(theta) =',np.cos(theta))
meshPoints = np.linspace(-1,1,500)
print('meshPoints[53] =',meshPoints[53])
plt.plot(meshPoints,np.sin(2 * np.pi * meshPoints))