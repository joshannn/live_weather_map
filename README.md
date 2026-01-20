# live_weather_map
Here is the content formatted specifically for a GitHub-ready `README.md` file. I have improved the hierarchy, added syntax highlighting for the code blocks, and used a clean structure for better readability.

---

```markdown
# Live Weather Map of Nepal

A real-time desktop visualization tool built with **Python** and **Pygame** that maps weather data across Nepal's districts using geographic data and live API integration.

## Overview
**Live Weather Map of Nepal** renders a dynamic map where each district is color-coded based on its current temperature. By hovering over a district, users can see a detailed breakdown of local conditions. The application uses the **Open-Meteo API** for data and **GeoJSON** for precise district boundaries.

## Features
* **District-Level Visualization:** Detailed map of Nepal's 77 districts.
* **Temperature Gradient:** Smooth, coherent color blending based on thermal data.
* **Interactive Hover Tooltips:**
    * District Name
    * Temperature (°C)
    * Current Weather Condition
    * Wind Speed
* **Live Updates:** Automatic weather refresh every 30 minutes.
* **Responsive UI:** Resizable and maximizable application window.
* **Data Optimization:** Pre-processed geometry that merges local levels (GaPa/NaPa) into unified districts for better performance.

## Project Structure
```text
live_weather/
│
├── main.py                 # Main Pygame application loop
├── geo.py                  # GeoJSON loading and coordinate transformation
├── weather.py              # Weather fetching logic
├── utils.py                # Color blending and helper functions
│
├── district.geojson        # Original GaPa/Nagarpalika GeoJSON
├── district_merged.geojson # Merged district-level GeoJSON (Generated)
│
├── merge_gapa_to_district.py  # Script to preprocess geographic data
└── README.md               # Project documentation

```

## Requirements

* **Python 3.10+**
* **Dependencies:**
* `Pygame` (GUI and rendering)
* `Requests` (API calls)
* `GeoPandas`, `Shapely`, `Fiona` (Only for initial data merging)



### Installation

```bash
pip install pygame requests geopandas shapely fiona

```

## GeoJSON Preparation

The application requires a merged district file to function correctly. If you are starting from the raw GaPa/Nagarpalika data, you must merge them first.

1. **Merge GaPa to District:**
Run the following command:
```bash
python merge_gapa_to_district.py

```


2. This generates `district_merged.geojson`, which the main application uses for rendering.

## Running the Application

Ensure `district_merged.geojson` is in the same directory as `main.py`, then run:

```bash
python main.py

```

### Controls

* **Mouse Hover:** View specific weather details for a district.
* **Resize Window:** The map scales dynamically to fit the window.
* **Legend:** Reference the color scale at the bottom/side for temperature ranges.

## Data Sources

* **Weather:** [Open-Meteo API](https://open-meteo.com/) (No API key required).
* **Geography:** District centroid coordinates are used for precise weather fetching.

##  Known Limitations & Future Improvements

### Current Limitations

* Requires an active internet connection for live data.
* Fixed view (No zoom or pan support currently).
* Fetch logic is tied to district centroids.

## License

This project is for educational purposes. GeoJSON data remains under the license of its respective providers.

---

**Developed by:** Joshan Dhakal

**Location:** Nepal 🇳🇵


