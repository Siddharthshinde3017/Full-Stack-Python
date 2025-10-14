# Creating a "Happy Diwali" fireworks animation and saving it as a GIF.
# The generated file will be saved to /mnt/data/happy_diwali_fireworks.gif
# You can download it from the link printed after the animation is created.
# NOTE: This uses matplotlib animation and Pillow writer to save a GIF.
# Run-time can take a few seconds depending on the environment.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from PIL import Image, ImageSequence

# Animation parameters
W, H = 10, 6              # figure size ratio
fps = 30
duration_seconds = 8
frames = fps * duration_seconds

# Firework class - handles single launch + explosion
class Firework:
    def __init__(self):
        # launch position (x), starting at bottom
        self.x = random.uniform(1, 9)
        self.y = 0.0
        # launch velocity
        self.vx = random.uniform(-0.02, 0.02)
        self.vy = random.uniform(0.16, 0.26)
        self.exploded = False
        self.particles = []

    def step(self):
        if not self.exploded:
            # rise
            self.x += self.vx
            self.y += self.vy
            # slow down
            self.vy -= 0.004 + random.uniform(0, 0.001)
            # explosion condition (apogee or random)
            if self.vy <= 0.02 or random.random() < 0.01:
                self.explode()
        else:
            # update particles
            for p in self.particles:
                p['x'] += p['vx']
                p['y'] += p['vy']
                p['vy'] -= 0.003  # gravity
                p['life'] -= 1

            # remove dead particles
            self.particles = [p for p in self.particles if p['life'] > 0]

    def explode(self):
        self.exploded = True
        n = random.randint(24, 48)
        speed = random.uniform(0.8, 1.8)
        palette = [
            (1.0, 0.6, 0.2), (1.0, 0.2, 0.6), (0.4, 0.8, 1.0),
            (0.8, 1.0, 0.4), (1.0, 1.0, 0.6), (0.9, 0.5, 1.0)
        ]
        color = random.choice(palette)
        for i in range(n):
            angle = random.uniform(0, 2*np.pi)
            sp = speed * random.uniform(0.3, 1.0)
            self.particles.append({
                'x': self.x,
                'y': self.y,
                'vx': sp * np.cos(angle) * (0.6 + random.random()*0.8),
                'vy': sp * np.sin(angle) * (0.6 + random.random()*0.8),
                'life': random.randint(int(0.4*fps), int(1.4*fps)),
                'size': random.uniform(20, 90),
                'color': color
            })

# Create many fireworks and manage them
fireworks = []

def maybe_launch():
    # randomly launch new firework(s)
    if random.random() < 0.08:
        fireworks.append(Firework())

# Setup figure
fig, ax = plt.subplots(figsize=(W, H))
ax.set_facecolor('black')
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Decorative twinkling lights (top string bulbs)
num_bulbs = 20
bulb_x = np.linspace(0.5, 9.5, num_bulbs)
bulb_y = np.full_like(bulb_x, 5.6)
bulb_sizes = np.linspace(40, 90, num_bulbs)

# Scatter artists for fireworks and bulbs
particle_scatter = ax.scatter([], [], s=[], alpha=0.85)
bulb_scatter = ax.scatter(bulb_x, bulb_y, s=bulb_sizes, alpha=0.9)

# Text: "Happy Diwali"
text = ax.text(5, 3.2, "HAPPY DIWALI", fontsize=36, fontweight='bold',
               ha='center', va='center', color='gold', alpha=1.0)
subtext = ax.text(5, 2.6, "May your life sparkle with joy and light ✨", fontsize=14,
                  ha='center', va='center', color='white', alpha=0.9)

def init():
    particle_scatter.set_offsets([])
    particle_scatter.set_sizes([])
    particle_scatter.set_facecolors([])
    return particle_scatter, bulb_scatter, text, subtext

def animate(frame_num):
    # Possibly launch fireworks
    maybe_launch()

    # Step all fireworks
    for fw in fireworks:
        fw.step()

    def animate(frame_num):
        global fireworks  # ✅ moved here to fix the error

        # Possibly launch fireworks
        maybe_launch()

        # Step all fireworks
        for fw in fireworks:
            fw.step()

        # Remove fully finished fireworks
        fireworks = [fw for fw in fireworks if (not fw.exploded) or len(fw.particles) > 0]

        # Collect particle data for scatter
        xs, ys, sizes, colors = [], [], [], []
        for fw in fireworks:
            if not fw.exploded:
                xs.append(fw.x)
                ys.append(fw.y)
                sizes.append(80)
                colors.append((1.0, 1.0, 1.0, 1.0))
            for p in fw.particles:
                xs.append(p['x'])
                ys.append(p['y'])
                sizes.append(p['size'])
                life_ratio = max(0.05, p['life'] / (fps * 1.2))
                r, g, b = p['color']
                colors.append((r, g, b, life_ratio))

        if len(xs) > 0:
            particle_scatter.set_offsets(np.column_stack([xs, ys]))
            particle_scatter.set_sizes(sizes)
            particle_scatter.set_facecolors(colors)
        else:
            particle_scatter.set_offsets([])
            particle_scatter.set_sizes([])
            particle_scatter.set_facecolors([])

        # Twinkling bulbs
        bulb_colors = []
        palette_bulb = [(1.0, 0.4, 0.4, 0.9), (1.0, 0.9, 0.4, 0.95), (0.4, 1.0, 0.6, 0.92), (0.6, 0.8, 1.0, 0.95),
                        (1.0, 0.5, 0.9, 0.92)]
        for i in range(num_bulbs):
            c = random.choice(palette_bulb)
            bulb_colors.append(c)
        bulb_scatter.set_facecolors(bulb_colors)

        # Text glow
        txt_alpha = 0.7 + 0.3 * np.sin(frame_num * 0.15)
        text.set_alpha(txt_alpha)

        return particle_scatter, bulb_scatter, text, subtext
