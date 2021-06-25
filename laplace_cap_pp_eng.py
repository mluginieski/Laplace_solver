import math as m
import numpy as np
import matplotlib.pyplot as plt

####### System's definitions and parameters #######

# Number max of iterations
maxIter = 1000

# Definition of box and delta
lenX  = lenY = 51      # Square box
delta = 1
mpx   = m.ceil(lenX/2) # x mid point
mpy   = m.ceil(lenY/2) # y mid point

# Definition of vector V and guess value
V = np.empty((lenX, lenY)) # Vector numpy of shape(lenX, lenY)
Vguess = 0.5               # Guess of V
V.fill(Vguess)             # Fill V with Vguess

# Boundary conditions of the box
Vtop    = 0
Vbottom = 0
Vleft   = 0
Vright  = 0

# Applaing the BC on V
V[(lenY-1):, :] = Vtop
V[:1, :]        = Vbottom
V[:, (lenX-1):] = Vright
V[:, :1]        = Vleft

## Definition of plates
length_plate = 25            # Length of the plates (grid points)
lp = m.floor(length_plate/2) # Midpoint os plates length

plate_position = 7           # Distance between mpx and the plate
pp1 = mpx + plate_position   # Plate 1
pp2 = mpx - plate_position   # Plate 2

# Definition of  the grid
X, Y = np.meshgrid(np.arange(0, lenX), np.arange(0, lenY))

####### Calculations #######

## Electric potential
for iteration in range(0, maxIter):
    for i in range(1, lenX-1, delta):
        for j in range(1, lenY-1, delta):

            V[mpy-lp:mpy+lp,pp1] =  1 # Fixed potential of right plate
            V[mpy-lp:mpy+lp,pp2] = -1 # Fixed potential of left plate

            # Laplace's equation
            V[i, j] = 0.25 * (V[i+1][j] + V[i-1][j] + V[i][j+1] + V[i][j-1])

## Electric field
E  = np.gradient(-V) # E = -grad(V)
Ex = E[1]            # Ex
Ey = E[0]            # Ey
Emag = np.sqrt(np.power(Ex, 2) + np.power(Ey, 2)) # Electric field magnitude

ExN = Ex/Emag # Normalized Ex
EyN = Ey/Emag # Normalized Ey

####### Graphs #######

colorinterpolation = 50
colourMap = plt.cm.jet

# Electric potential
plt.title("Electric Potential")
plt.contourf(X, Y, V, colorinterpolation, cmap=colourMap)
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()
plt.show()

# Electric field
plt.title('Magnitude of E')
plt.contourf(X, Y, Emag, colorinterpolation, cmap=colourMap)
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()
plt.show()

# Electric field and field vectors
plt.title('Magnitude of E and field vectors')
plt.contourf(X, Y, Emag, colorinterpolation, cmap=colourMap)
plt.colorbar()
plt.quiver(X, Y, ExN, EyN, scale=50, color='k')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
