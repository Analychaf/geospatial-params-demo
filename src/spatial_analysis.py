def buffer_points(gdf, radius):
    gdf_projected = gdf.to_crs(epsg=3857)  # meters
    gdf_buffered = gdf_projected.buffer(radius)
    return gdf_projected.assign(geometry=gdf_buffered).to_crs(gdf.crs)  # return to original CRS

