# GlowScript 3.1 VPython

# Open this code in Trinket
# https://trinket.io/library/trinkets/424bbef5df

from vpython import * # Delete this line for Trinket

# ***********************************
#  Set the Initial Conditions Here:
# ***********************************

# Constants
R = 0.1
M = 1
G = 1
dt = 0.0005
tmax = 30

# Initialize the positions and masses of the objects.
star1 = sphere(pos=vector(0.5,0,0), radius=R, m=M, color=color.yellow)
star2 = sphere(pos=vector(-0.5,0,0), radius=R, m=M, color=color.orange)
planet = sphere(pos=vector(2,0,0), radius=0.5*R, m=M/1000, color=color.cyan)

# Initialize the momenta. Set the momentum of star2 so that the total momentum is zero.
star1.p = vector(0,0.5,0)*star1.m
planet.p = vector(0,1,0)*planet.m
star2.p = -(planet.p + star1.p)


# ***********************************

# Used for showing the orbit paths.
attach_trail(star1)
attach_trail(star2)
attach_trail(planet)

t=0
while t < tmax:
    # Define the animation rate.
    rate(7500)
    

# ***********************************
#        Code Solution Here:
# ***********************************

# Some helpful functions: 
#     norm(v) gives the unit vector of the vector v
#     mag(v) gives the magnitude of the vector v

    # Vector from star 1 to 2.
    r12 = star2.pos-star1.pos
    
    # Vector from star 1 to planet.
    r1p = planet.pos-star1.pos
    
    # Vector from star 2 to planet.
    r2p = planet.pos-star2.pos
    
    # Calculate gravitational force between star 1 and star 2.
    F12 = -G * star1.m * star2.m * norm(r12) / mag(r12)**2
    F21 = -F12

    # Calculate the force on the planet due to star 1.
    F1p = -G * star1.m * planet.m * norm(r1p) / mag(r1p)**2

    # Calculate the force on the planet due to star 2.
    F2p = -G * star2.m * planet.m * norm(r2p) / mag(r2p)**2
    
    # Update the momenta (with total vector force).
    star1.p = star1.p + (F21 - F1p) * dt
    star2.p = star2.p + (F12 - F2p) * dt
    planet.p = planet.p + (F1p + F2p) * dt
    
    # Update position.
    star1.pos = star1.pos + star1.p * dt / star1.m
    star2.pos = star2.pos + star2.p * dt / star2.m
    planet.pos = planet.pos + planet.p * dt / planet.m

# ***********************************

    # Increase the total runtime.
    t = t + dt
