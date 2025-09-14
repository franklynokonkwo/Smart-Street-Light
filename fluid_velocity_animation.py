import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches

def velocity(r, R, beta, mu0, n):
    """
    Evaluate the velocity profile for a non-Newtonian fluid in pipe flow.
    
    Parameters:
    r : array_like
        Radial coordinate (distance from centerline)
    R : float
        Pipe radius
    beta : float
        Pressure gradient
    mu0 : float
        Viscosity coefficient
    n : float
        Fluid property parameter (n=1 for Newtonian fluids)
    
    Returns:
    v : array_like
        Velocity at each radial position
    """
    # Prefactor term
    prefactor = (beta / (2 * mu0))**(1/n)
    
    # Main velocity formula
    v = prefactor * (n / (n + 1)) * (R**(1 + 1/n) - r**(1 + 1/n))
    
    return v

# Parameters
R = 1.0
beta = 0.02
mu0 = 0.02

# Part b: Plot v(r) for n = 0.1
r_values = np.linspace(0, R, 1000)
n_specific = 0.1
v_values = velocity(r_values, R, beta, mu0, n_specific)

plt.figure(figsize=(10, 6))
plt.plot(r_values, v_values, 'b-', linewidth=2)
plt.xlabel('Radial position r')
plt.ylabel('Velocity v(r)')
plt.title(f'Velocity profile for n = {n_specific}')
plt.grid(True, alpha=0.3)
plt.xlim(0, R)
plt.show()

# Part c: Animation of v(r) as n varies from 1 to 0.01
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Generate n values from 1 down to 0.01
n_values = np.linspace(1.0, 0.01, 100)

# Initialize plots
line, = ax1.plot([], [], 'b-', linewidth=2)
normalized_line, = ax2.plot([], [], 'r-', linewidth=2)
pipe_visual = ax2.add_patch(patches.Rectangle((-1.1, -1.1), 2.2, 2.2, fill=False, 
                                            edgecolor='gray', linestyle='--', alpha=0.5))
title = ax1.set_title('')
ax1.set_xlabel('Radial position r')
ax1.set_ylabel('Velocity v(r)')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, R)
ax1.set_ylim(0, 0.02)  # Adjust based on observed range

ax2.set_xlabel('Radial position r')
ax2.set_ylabel('Normalized velocity v(r)/v(0)')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0, R)
ax2.set_ylim(0, 1.1)
ax2.set_title('Normalized velocity profile')

def init():
    line.set_data([], [])
    normalized_line.set_data([], [])
    return line, normalized_line

def update(frame):
    n_current = n_values[frame]
    
    # Calculate velocity profile
    v_current = velocity(r_values, R, beta, mu0, n_current)
    
    # Update regular plot
    line.set_data(r_values, v_current)
    ax1.set_ylim(0, max(v_current) * 1.1)
    
    # Update normalized plot
    v0 = velocity(0, R, beta, mu0, n_current)  # Centerline velocity
    normalized_v = v_current / v0 if v0 > 0 else np.zeros_like(v_current)
    normalized_line.set_data(r_values, normalized_v)
    
    # Update title
    title.set_text(f'n = {n_current:.3f}')
    
    return line, normalized_line, title

# Create animation
ani = FuncAnimation(fig, update, frames=len(n_values),
                    init_func=init, blit=True, interval=100)

plt.tight_layout()
plt.show()

# To save the animation (uncomment if needed)
# ani.save('velocity_profile_animation.mp4', writer='ffmpeg', fps=10, dpi=100)

# Additional: Show several key frames
key_n_values = [1.0, 0.5, 0.1, 0.05, 0.01]
colors = ['blue', 'green', 'red', 'purple', 'orange']

plt.figure(figsize=(12, 8))
for i, n_val in enumerate(key_n_values):
    v = velocity(r_values, R, beta, mu0, n_val)
    v0 = velocity(0, R, beta, mu0, n_val)
    normalized_v = v / v0 if v0 > 0 else np.zeros_like(v)
    plt.plot(r_values, normalized_v, color=colors[i], linewidth=2, 
             label=f'n = {n_val}')

plt.xlabel('Radial position r')
plt.ylabel('Normalized velocity v(r)/v(0)')
plt.title('Normalized velocity profiles for different n values')
plt.legend()
plt.grid(True, alpha=0.3)
plt.xlim(0, R)
plt.ylim(0, 1.1)
plt.show()
