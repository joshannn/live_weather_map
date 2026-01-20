import pygame, threading, time
from config import *
from utils import is_inside_district
from geo import load_districts
from weather import fetch_all_weather

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Live Weather Map of Nepal")
clock = pygame.time.Clock()


districts = load_districts("district.geojson")


threading.Thread(target=fetch_all_weather, args=(districts, REFRESH_INTERVAL), daemon=True).start()

running = True
current_hover_id = None
hover_timer = 0
hover_weather_cache = {}
hover_fetch_lock = threading.Lock()

while running:
    mx, my = pygame.mouse.get_pos()
    current_hover = None
    dt = clock.tick(30)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(COLOR_BG)

    
    for d in districts:
        hovered = False
        for poly in d['polys']:
            if is_inside_district(mx, my, poly):
                hovered = True
                current_hover = d
                break
        color = tuple(min(255, c+60) for c in d['color']) if hovered else d['color']
        for poly in d['polys']:
            pygame.draw.polygon(screen, color, poly)
            pygame.draw.polygon(screen, (80,80,90), poly, 1)

    
    if current_hover:
        w = current_hover['weather_base'] or {"temp_str":"Loading...", "condition":"Fetching...", "wind":0}
        tooltip_w = 240
        pygame.draw.rect(screen, (30,30,40), (mx+15, my+15, tooltip_w, 100))
        pygame.draw.rect(screen, (0,150,255), (mx+15, my+15, tooltip_w, 100), 2)
        screen.blit(font_name.render(current_hover['name'], True, COLOR_TEXT), (mx+25, my+25))
        screen.blit(font_weather.render(f"Temp: {w['temp_str']}", True, (255,165,0)), (mx+25, my+50))
        screen.blit(font_weather.render(f"Weather: {w['condition']}", True, (0,255,150)), (mx+25, my+70))
        screen.blit(font_weather.render(f"Wind: {w['wind']:.1f} km/h", True, (150,200,255)), (mx+25, my+90))

# legend
# legend_x = WIDTH - 180
# legend_y = 20

# pygame.draw.rect(screen, (30, 30, 40), (legend_x, legend_y, 160, 180))
# pygame.draw.rect(screen, (100, 100, 110), (legend_x, legend_y, 160, 180), 1)

# legend_title = font_weather.render("Temperature", True, COLOR_TEXT)
# screen.blit(legend_title, (legend_x + 10, legend_y + 10))

# temp_ranges = [
#     ("<0°C", get_temp_color(-5)),
#     ("0–10°C", get_temp_color(5)),
#     ("10–20°C", get_temp_color(15)),
#     ("20–25°C", get_temp_color(22)),
#     ("25–30°C", get_temp_color(27)),
#     ("30–35°C", get_temp_color(32)),
#     (">35°C", get_temp_color(38))
# ]

# for i, (label, color) in enumerate(temp_ranges):
#     y_pos = legend_y + 40 + i * 20
#     pygame.draw.rect(screen, color, (legend_x + 10, y_pos, 20, 15))
#     label_txt = font_status.render(label, True, COLOR_TEXT)
#     screen.blit(label_txt, (legend_x + 35, y_pos))


    pygame.display.flip()

pygame.quit()
