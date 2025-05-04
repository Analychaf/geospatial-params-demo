# Geospatial Parameters Demo

## Project Goal

This project demonstrates a **parameterized and modular geospatial pipeline** that dynamically:

- Loads parameters from YAML files.
- Generates or loads geospatial data (e.g., GeoJSON).
- Applies preprocessing steps (e.g., re-projection, cleaning).
- Performs spatial analysis (e.g., buffer creation).
- Visualizes outputs interactively using `folium` and Leaflet maps.

Everything is **fully configurable** through parameter files and designed for easy extension to real-world spatial data automation and monitoring workflows.

---

## Development Environment

### Recommended Tools

- [VS Code](https://code.visualstudio.com/)
- [Python 3.9+](https://www.python.org/)
- [JupyterLab](https://jupyter.org/)
- [GeoPandas & Folium](https://geopandas.org/) for spatial manipulation and visualization

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

git clone https://github.com/your-username/geospatial-params-demo.git
cd geospatial-params-demo


### 2. Create and Activate a Virtual Environment

python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate


### 3. Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt


### 4. Set Up Jupyter Kernel for VS Code

pip install ipykernel
python -m ipykernel install --user --name=geo-env --display-name "Python (.venv) - Geospatial"
Then, in VS Code or JupyterLab, switch to the kernel named:
Python (.venv) - Geospatial


### Project Structure

geospatial-params-demo/

├── data/

│   └── sample_points.geojson          # Sample data (auto-generated if missing)

├── notebooks/

│   └── preprocessing.ipynb           # Main notebook to run the pipeline

├── params/

│   ├── config.yml                    # Path and CRS definitions

│   └── preprocessing.yml            # Preprocessing configuration

├── src/

│   ├── __init__.py

│   ├── data_generator.py            # Sample data generation logic

│   ├── io_utils.py                  # Load functions

│   ├── preprocessing.py             # Clean/transform GeoDataFrames

│   ├── spatial_analysis.py          # Buffering and spatial logic

│   └── visualize.py                 # Leaflet/Folium visualization

├── requirements.txt

└── README.md


### How to Run the Project

From Jupyter Notebook:

1. Open notebooks/preprocessing.ipynb
2. Ensure correct kernel (.venv) is selected
3. Run the cells in order


### Testing & Extending

All functions are modular and reusable.
Replace sample_points.geojson with your own dataset.
Modify params/config.yml and params/preprocessing.yml to test different scenarios.


### Known Warnings and Fixes

**CRS Warning Fix:**

gdf_proj = gdf.to_crs(epsg=3857)
centroid = gdf_proj.centroid.to_crs(gdf.crs)
Avoid using .centroid directly on EPSG:4326; project first!

### To-Do / Next Steps

Add unit tests (pytest, unittest)
Add polygon/line handling
Export output maps and KPIs


**Developed by Canalytics — Data & AI Engineering Solutions for Spatial Analytics.**
