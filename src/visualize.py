import folium
from folium import GeoJson, LayerControl, TileLayer, FeatureGroup, Popup

def plot_leaflet(gdf):
    # Reproject for Folium (WGS84)
    gdf_latlon = gdf.to_crs(epsg=4326)

    # Calculate centroid from projected geometry
    gdf_proj = gdf.to_crs(epsg=3857)
    center = gdf_proj.geometry.centroid.to_crs(epsg=4326)
    center_coords = [center.y.mean(), center.x.mean()]

    # Initialize map
    m = folium.Map(location=center_coords, zoom_start=15)

    # Add base tiles
    # Add base tiles
     
    TileLayer("OpenStreetMap").add_to(m)
    
    TileLayer(
    tiles="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
    attr='© OpenStreetMap contributors © CARTO',
    name="CartoDB Positron").add_to(m)
    
    TileLayer(
    tiles="https://stamen-tiles.a.ssl.fastly.net/terrain/{z}/{x}/{y}.jpg",
    attr='Map tiles by Stamen Design, CC BY 3.0 — Map data © OpenStreetMap',
    name="Stamen Terrain").add_to(m)

    # Group: Buffered Geometry (Polygon)
    poly_group = FeatureGroup(name="Buffered Zones")
    GeoJson(
        gdf_latlon,
        name="buffered",
        style_function=lambda feature: {
            "fillColor": "#ff7800",
            "color": "#ff0000",
            "weight": 2,
            "fillOpacity": 0.5
        }
    ).add_to(poly_group)
    poly_group.add_to(m)

    # Group: Points (Centroids or original points)
    if gdf.geometry.geom_type.iloc[0] != "Point":
        points = gdf.copy()
        points["geometry"] = gdf.geometry.centroid
        points = points.set_geometry("geometry").to_crs(epsg=4326)
    else:
        points = gdf_latlon

    point_group = FeatureGroup(name="Sample Points")
    for _, row in points.iterrows():
        folium.CircleMarker(
            location=[row.geometry.y, row.geometry.x],
            radius=8,  # Control size
            color='blue',
            fill=True,
            fill_opacity=0.7,
            popup=Popup(str(row.get("id", "Point")), parse_html=True)
        ).add_to(point_group)
    point_group.add_to(m)

    # Add Layer Control
    LayerControl(collapsed=False).add_to(m)

    return m
