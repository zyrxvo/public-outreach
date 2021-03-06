# GlowScript 3.1 VPython

# Open this code in Trinket
# https://trinket.io/library/trinkets/f0de22daa9

# Daniel Shiffman
# https://thecodingtrain.com/CodingChallenges/093-double-pendulum.html
# https://youtu.be/uWzPe_S-RVE

# Modifications by Garett Brown

from vpython import * # Delete this line for Trinket

pi = 3.141592653589793238462643383279502884197

# ***********************************
#  Set the Initial Conditions Here:
# ***********************************

r1 = 10
r2 = 10
m1 = 10
m2 = 10
theta1 = pi/2
theta2 = pi/2
omega1 = 0
omega2 = 0
g = 9.8
dt = 0.001
t = 0

# ***********************************

L = r1+r2
x1 = r1 * sin(theta1)
y1 = -r1 * cos(theta1)
x2 = x1 + r2 * sin(theta2)
y2 = y1 - r2 * cos(theta2)
c1 = curve(vector(0,0,0), vector(x1,y1,0))
p1 = sphere(pos = vector(x1,y1,0), radius=1)
c2 = curve(vector(x1,y1,0), vector(x2,y2,0))
p2 = sphere(pos = vector(x2,y2,0), radius=1)
bx = box(pos = vector(0,0,0), length=L, height=0.1, width=L)
attach_trail(p2)

while t < 200:
  rate(7900)
  t += dt
  
  num1 = -g * (2 * m1 + m2) * sin(theta1)
  num2 = -m2 * g * sin(theta1 - 2 * theta2)
  num3 = -2 * sin(theta1 - theta2) * m2
  num4 = omega2 * omega2 * r2 + omega1 * omega1 * r1 * cos(theta1 - theta2)
  den = r1 * (2 * m1 + m2 - m2 * cos(2 * theta1 - 2 * theta2))
  alpha1 = (num1 + num2 + num3 * num4) / den

  num1 = 2 * sin(theta1 - theta2)
  num2 = (omega1 * omega1 * r1 * (m1 + m2))
  num3 = g * (m1 + m2) * cos(theta1)
  num4 = omega2 * omega2 * r2 * m2 * cos(theta1 - theta2)
  den = r2 * (2 * m1 + m2 - m2 * cos(2 * theta1 - 2 * theta2))
  alpha2 = (num1 * (num2 + num3 + num4)) / den

  omega1 += alpha1*dt
  omega2 += alpha2*dt
  theta1 += omega1*dt
  theta2 += omega2*dt

  #omega1 *= 0.99
  #omega2 *= 0.99

  x1 = r1 * sin(theta1);
  y1 = -r1 * cos(theta1);
  x2 = x1 + r2 * sin(theta2);
  y2 = y1 - r2 * cos(theta2);


  c1.modify(1, pos = vector(x1,y1,0))
  p1.pos = vector(x1,y1,0)
  c2.modify(0, pos = vector(x1,y1,0))
  c2.modify(1, pos = vector(x2,y2,0))
  p2.pos = vector(x2,y2,0)
  

