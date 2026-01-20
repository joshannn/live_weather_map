# color scheme
def get_temp_color(temp):
    if temp is None:
        return (60, 60, 70)
    elif temp < 0:
        return (150, 200, 255)
    elif temp < 10:
        return (100, 150, 255)
    elif temp < 20:
        return (100, 200, 150)
    elif temp < 25:
        return (100, 220, 100)
    elif temp < 30:
        return (255, 200, 100)
    elif temp < 35:
        return (255, 150, 80)
    else:
        return (255, 100, 100)


def is_inside_district(x, y, poly):
    n = len(poly)
    inside = False
    p1x, p1y = poly[0]
    for i in range(n + 1):
        p2x, p2y = poly[i % n]
        if y > min(p1y, p2y) and y <= max(p1y, p2y) and x <= max(p1x, p2x):
            if p1y != p2y:
                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
            if p1x == p2x or x <= xinters:
                inside = not inside
        p1x, p1y = p2x, p2y
    return inside
