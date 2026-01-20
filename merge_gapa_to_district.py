import geopandas as gpd

# Load GaPa-level GeoJSON
gdf = gpd.read_file("district.geojson")

# Make sure DISTRICT column exists
print(gdf.columns)

# Dissolve (merge) by DISTRICT
district_gdf = gdf.dissolve(by="DISTRICT", as_index=False)

# Save merged district-level GeoJSON
district_gdf.to_file("district_merged.geojson", driver="GeoJSON")

print(" Merged GeoJSON saved as district_merged.geojson")
print(district_gdf.head())
