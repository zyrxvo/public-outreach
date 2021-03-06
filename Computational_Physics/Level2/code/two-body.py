# GlowScript 3.1 VPython

# Open this code in Trinket
# https://trinket.io/library/trinkets/0f411818d9

from vpython import * # Delete this line for Trinket

# ***********************************
#  Set the Initial Conditions Here:
# ***********************************

# Constants
R = 0.1
M = 1
G = 1
dt = 0.001
tmax = 150

# Initialize the positions and masses of the objects.
star1 = sphere(pos=vector(0,0,0), radius=R, m=M, color=color.yellow)
star2 = sphere(pos=vector(1,0,0), radius=R/2, m=M/1000, color=color.cyan)

# Initialize the momenta. Set the momentum so that the total momentum is zero.
star2.p = vector(0,1,0)*star2.m
star1.p = -star2.p

# ***********************************

# Used for showing the orbit paths.
attach_trail(star1)
attach_trail(star2)

t=0
while t < tmax:
    # Define the animation rate.
    rate(10000)
    

# ***********************************
#        Code Solution Here:
# ***********************************

# Some helpful functions: 
#     norm(v) gives the unit vector of the vector v
#     mag(v) gives the magnitude of the vector v

    # Vector from star 1 to 2.
    r12 = star2.pos-star1.pos
    
    # Calculate gravitational force between star 1 and star 2.
    F12 = -G * star1.m * star2.m * norm(r12) / mag(r12)**2
    F21 = -F12
    
    # Update the momenta (with total vector force).
    star1.p = star1.p + F21 * dt
    star2.p = star2.p + F12 * dt
    
    # Update position.
    star1.pos = star1.pos + star1.p * dt / star1.m
    star2.pos = star2.pos + star2.p * dt / star2.m

# ***********************************

    # Increase the total runtime.
    t = t + dt
