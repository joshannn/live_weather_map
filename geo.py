import geopandas as gpd
from config import WIDTH, HEIGHT

def transform(lon, lat):
    """Convert geo coordinates to screen coordinates"""
    BBOX = [80.060, 26.347, 88.204, 30.467]
    x = (lon - BBOX[0]) * (WIDTH / (BBOX[2] - BBOX[0]))
    y = HEIGHT - (lat - BBOX[1]) * (HEIGHT / (BBOX[3] - BBOX[1]))
    return int(x), int(y)

def load_districts(geojson_path):
    """Load districts with polygons and centroids"""
    gdf = gpd.read_file(geojson_path)
    districts = []

    for i, row in gdf.iterrows():
        poly_set = []
        geom = row['geometry']

        if geom.type == "Polygon":
            poly_set = [[transform(x, y) for x, y in geom.exterior.coords]]
        elif geom.type == "MultiPolygon":
            for p in geom.geoms:
                poly_set.append([[transform(x, y) for x, y in p.exterior.coords]])

        centroid = geom.centroid
        avg_lon = centroid.x
        avg_lat = centroid.y

        districts.append({
            'id': i,
            'name': row['DISTRICT'],
            'polys': poly_set,
            'lat': avg_lat,
            'lon': avg_lon,
            'weather_base': None,
            'weather_hover': None,
            'color': (60, 60, 70)
        })
    return districts
