def preprocess(gdf, config):
    if config.get("drop_na", False):
        gdf = gdf.dropna()
    if "columns_to_keep" in config:
        gdf = gdf[config["columns_to_keep"]]
    if "simplify_tolerance" in config:
        gdf["geometry"] = gdf["geometry"].simplify(config["simplify_tolerance"])
    return gdf
