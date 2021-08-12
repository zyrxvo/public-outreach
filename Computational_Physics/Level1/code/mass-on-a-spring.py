# GlowScript 3.1 VPython

# Open this code in Trinket
# https://trinket.io/library/trinkets/04931fe5c8

# Garett Brown
# Inspired by Daniel Shiffman (https://thecodingtrain.com/CodingChallenges/093-double-pendulum.html)

from vpython import * # Delete this line for Trinket

pi = 3.141592653589793238462643383279502884197

# ***********************************
#  Set the Initial Conditions Here:
# ***********************************

m = 1
k = 1
x = 5
v = 0
a = 0
dt = 0.001
t = 0

# ***********************************

L0 = 2.1*x
L = L0 + x
p = sphere(pos = vector(x,0,0), radius=1)
spring = helix(pos=vector(-L0,0,0), length=L, radius=0.75, coils=k*10 + x)
bottom = box(pos=vector(0,-1.1,0), length=2*L0, height=0.1, width=2.5)
side = box(pos=vector(-L0,0,0), length=-0.1, height=2.3, width=2.5)

while t < 10000:
  rate(7500)
  t += dt
  
# ***********************************
#        Code Solution Here:
# ***********************************
  
  
  a = -(k/m)*x
  v = v + a*dt
  x  = x + v*dt
  
  
# ***********************************

  L = L0 + x
  p.pos = vector(x,0,0)
  spring.length = L

