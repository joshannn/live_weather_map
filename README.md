Live Weather Map of Nepal
Overview

Live Weather Map of Nepal is a desktop application built using Python and Pygame that visualizes real-time weather data across Nepal’s districts.
Each district is color-coded based on temperature and displays detailed weather information on hover.

The project uses Open-Meteo API for live weather data and GeoJSON district boundaries for accurate geographic rendering.

Features

District-level weather visualization for Nepal

Temperature-based color gradient map

Smooth and coherent color blending

Hover tooltip showing:

District name

Temperature

Weather condition

Wind speed

Automatic weather refresh every 30 minutes

Real-time weather fetch on hover

Resizable and maximizable application window

Optimized district geometry by merging GaPa/NaPa into districts

Project Structure
live_weather/
│
├── main.py                 # Main Pygame application loop
├── geo.py                  # GeoJSON loading and coordinate transformation
├── weather.py              # Weather fetching logic
├── utils.py                # Color blending and helper functions
│
├── district.geojson        # Original GaPa/Nagarpalika GeoJSON
├── district_merged.geojson # Merged district-level GeoJSON
│
├── merge_gapa_to_district.py  # One-time script to merge GaPa into districts
├── README.md               # Project documentation

Requirements

Python 3.10 or newer

Pygame

Requests

GeoPandas (only required for merging GeoJSON, not for runtime)

Install dependencies:

pip install pygame requests geopandas shapely fiona

GeoJSON Preparation (Important)

The provided district.geojson contains GaPa/Nagarpalika boundaries.
To use district-level polygons, you must merge them once.

Merge GaPa to District

Run this command:

python merge_gapa_to_district.py


This will generate:

district_merged.geojson


The application uses this merged file.

Running the Application

Make sure district_merged.geojson is in the same folder as main.py.

Run:

python main.py

Controls and Interaction

Hover over a district to view weather details

Window can be resized or maximized

Weather data refreshes automatically

Legend shows temperature ranges and color meaning

Weather Data Source

Weather data is fetched from:

Open-Meteo API
https://open-meteo.com/

No API key is required.

Color Logic

Colors follow a continuous gradient from cold to hot

Designed for visual coherence and readability

Hover effect uses smooth blending instead of harsh highlighting

Known Limitations

Requires internet connection for live weather

District centroid is used for weather fetching

No zoom or pan support (planned improvement)

Future Improvements

Mouse wheel zoom and pan

District labels on map

Province-level toggle

Weather parameter switching (rainfall, humidity)

Offline caching

Performance optimizations for low-end systems

License

This project is for educational and learning purposes.
GeoJSON data sources remain under their respective licenses.

Author

Developed by Joshan Dhakal
Nepal
