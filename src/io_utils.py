import geopandas as gpd

def load_geodata(file_path, crs=None):
    gdf = gpd.read_file(file_path)
    if crs:
        gdf = gdf.to_crs(crs)
    return gdf
