# Scattering setup figure: incoming beam, impact parameter b, hyperbolic trajectory, and scattering angle Θ.
# You can tweak these:
m = 1.0          # mass
v_inf = 1.2      # speed at infinity
k = 1.0          # force constant (repulsive Coulomb-like)
b = 1.0          # impact parameter

import numpy as np
import matplotlib.pyplot as plt

# Invariants
L = m * v_inf * b
E = 0.5 * m * v_inf**2
e = np.sqrt(1.0 + (2*E*L**2)/(m*k**2))          # eccentricity (>1)
p = L**2 / (m * k)                               # semi-latus rectum
Theta = 2.0 * np.arctan(k / (m * b * v_inf**2))  # scattering angle

# Hyperbolic trajectory r(θ) = p / (1 + e cos θ), periapsis at θ=0
theta_inf = np.arccos(-1.0/e)                    # where r → ∞
eps = 1e-3
theta = np.linspace(-theta_inf+eps, theta_inf-eps, 800)
r = p / (1.0 + e*np.cos(theta))
x = r * np.cos(theta)
y = r * np.sin(theta)

# Incoming straight-line path (asymptote) at y = b from x = -X to 0
X = 6.0
xin = np.linspace(-X, 0.0, 200)
yin = np.full_like(xin, b)

# Outgoing asymptote: rotate x-axis by Θ (clockwise), pass through origin
phi = -Theta  # clockwise from +x
xout = np.linspace(0.0, X, 200)
yout = np.tan(phi) * xout

# Closest approach
r_min = p/(1.0 + e)
x_min, y_min = r_min, 0.0

# Plot
fig, ax = plt.subplots(figsize=(8,6))

# Incoming path
ax.plot(xin, yin, linewidth=2, label="Incoming beam (impact line)")

# Scattered trajectory
ax.plot(x, y, linewidth=2, label="Actual trajectory")

# Outgoing asymptote
ax.plot(xout, yout, linestyle="--", linewidth=2, label="Outgoing asymptote")

# Center
ax.scatter([0],[0], s=40)

# Impact parameter arrow
ax.annotate("", xy=(-3.5, b), xytext=(-3.5, 0), arrowprops=dict(arrowstyle="<->", linewidth=1.8))
ax.text(-3.7, b/2, r"$b$", rotation=90, va="center", ha="right")

# Mark closest approach
ax.scatter([x_min],[y_min], s=35)
ax.text(x_min*1.05, y_min+0.12, r"$r_{\min}$", va="bottom")

# Draw scattering angle at origin between incoming (+x direction) and outgoing asymptote
# We'll draw two unit vectors and an arc showing Θ
r_arc = 1.2
ang1 = 0.0       # along +x (incoming direction near the center)
ang2 = -Theta    # outgoing direction
t = np.linspace(ang2, ang1, 100)
ax.plot(r_arc*np.cos(t), r_arc*np.sin(t), linewidth=2)
ax.text(1.1*np.cos(-Theta/2), 1.1*np.sin(-Theta/2), r"$\Theta$", ha="center", va="center")

# Labels and cosmetics
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-X, X)
ax.set_ylim(-2.5, 2.5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Classical Scattering Setup: Impact Parameter, Trajectory, and Deflection Angle $\\Theta$")
ax.legend(loc="upper right")

plt.show()
