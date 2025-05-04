import geopandas as gpd
from shapely.geometry import Point
import os

def generate_sample_points(output_path):
    points = [
        {"id": 1, "geometry": Point(-73.5673, 45.5017)},
        {"id": 2, "geometry": Point(-73.5670, 45.5020)},
        {"id": 3, "geometry": Point(-73.5665, 45.5023)}
    ]
    gdf = gpd.GeoDataFrame(points, crs="EPSG:4326")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    gdf.to_file(output_path, driver="GeoJSON")
