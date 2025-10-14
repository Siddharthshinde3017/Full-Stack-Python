import pygame
import random
import math
import sys

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 2500, 850
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🎆 Happy Diwali Fireworks 🎇 may this Diwali Brings You New Opurtunitees and Happyness")

# Clock to control FPS
clock = pygame.time.Clock()

# Colors
COLORS = [
    (255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0),
    (0, 255, 255), (0, 0, 255), (255, 0, 255), (255, 192, 203), (255, 255, 255)
]

# Fonts
font = pygame.font.SysFont("Algerian", 60, bold=True)
small_font = pygame.font.SysFont("Arial", 25, bold=True)

# --- Classes ---

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = random.randint(2, 4)
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.uniform(2, 6)
        self.gravity = 0.08
        self.lifetime = random.randint(50, 90)
        self.opacity = 255

    def update(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed + self.gravity
        self.lifetime -= 1
        self.opacity = max(0, self.opacity - 4)

    def draw(self, surface):
        if self.lifetime > 0:
            surf = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(surf, (*self.color, self.opacity), (self.radius, self.radius), self.radius)
            surface.blit(surf, (self.x - self.radius, self.y - self.radius))


class Firework:
    def __init__(self):
        self.x = random.randint(100, WIDTH - 100)
        self.y = HEIGHT
        self.color = random.choice(COLORS)
        self.speed = random.uniform(8, 12)
        self.exploded = False
        self.explode_height = random.randint(150, 300)
        self.particles = []

    def update(self):
        if not self.exploded:
            self.y -= self.speed
            if self.y <= self.explode_height:
                self.exploded = True
                for _ in range(80):
                    self.particles.append(Particle(self.x, self.y, self.color))
        else:
            for p in self.particles:
                p.update()
            self.particles = [p for p in self.particles if p.lifetime > 0]

    def draw(self, surface):
        if not self.exploded:
            pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), 5)
        else:
            for p in self.particles:
                p.draw(surface)

# --- Main Loop ---

def main():
    fireworks = []
    running = True
    frame = 0

    while running:
        screen.fill((0, 0, 20))  # Night-sky blue background

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Randomly add fireworks
        if random.randint(0, 20) == 0:
            fireworks.append(Firework())

        # Update & draw fireworks
        for fw in fireworks[:]:
            fw.update()
            fw.draw(screen)
            if fw.exploded and len(fw.particles) == 0:
                fireworks.remove(fw)

        # Greeting text animation
        if frame % 50 < 20:
            text = font.render("🎆 HAPPY DIWALI 🎆", True, random.choice(COLORS))
            screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2 - 50))

        msg = small_font.render("May your life sparkle with joy, peace, and prosperity!", True, (255, 215, 0))
        screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT - 40))

        pygame.display.flip()
        clock.tick(60)
        frame += 1

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
