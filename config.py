import pygame

WIDTH, HEIGHT = 1100, 650
COLOR_BG = (15, 15, 20)
COLOR_TEXT = (220, 220, 220)
REFRESH_INTERVAL = 1800 

# Temperature-based color scheme
def get_temp_color(temp):
    if temp is None:
        return (60, 60, 70)  # Gray for no data
    elif temp < 0:
        return (150, 200, 255)  # Light blue - very cold
    elif temp < 10:
        return (100, 150, 255)  # Blue - cold
    elif temp < 20:
        return (100, 200, 150)  # Teal - cool
    elif temp < 25:
        return (100, 220, 100)  # Green - mild
    elif temp < 30:
        return (255, 200, 100)  # Yellow - warm
    elif temp < 35:
        return (255, 150, 80)  # Orange - hot
    else:
        return (255, 100, 100)  # Red - very hot

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Live Weather Map of Nepal")
clock = pygame.time.Clock()
font_name = pygame.font.SysFont("Verdana", 20, bold=True)
font_weather = pygame.font.SysFont("Verdana", 14)
font_status = pygame.font.SysFont("Verdana", 12)
