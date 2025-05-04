# Geospatial Parameters Demo

## 🧭 Project Goal

This project showcases a **parameterized and modular geospatial data pipeline** that allows:

- 📁 Loading settings from YAML configuration files
- 🌐 Generating or loading geospatial data (GeoJSON)
- 🧼 Applying preprocessing (CRS transformation, cleaning)
- 📏 Performing spatial analysis (buffering)
- 🗺️ Visualizing data using interactive Leaflet maps (via `folium`)

Everything is fully **driven by parameter files** and is organized for clarity, reusability, and extensibility across spatial workflows and automation scenarios.

---

## ⚙️ Development Environment

### Recommended Tools

- [VS Code](https://code.visualstudio.com/)
- [Python 3.9+](https://www.python.org/)
- [JupyterLab](https://jupyter.org/)
- [GeoPandas](https://geopandas.org/) and [Folium](https://python-visualization.github.io/folium/) for spatial processing & mapping

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

│   └── sample_points.geojson          # Auto-generated if missing

├── notebooks/

│   └── pipeline.ipynb                 # Main execution notebook

├── params/

│   ├── config.yml                     # Path to data, CRS, etc.

│   └── preprocessing.yml             # Rules for preprocessing

├── src/

│   ├── __init__.py

│   ├── data_generator.py             # Generate test points

│   ├── io_utils.py                   # Load functions

│   ├── preprocessing.py              # Cleaning/preprocessing

│   ├── spatial_analysis.py           # Buffering, etc.

│   └── visualize.py                  # Leaflet map plotting

├── .gitignore                        # Excludes .venv, cache, etc.

├── requirements.txt                  # Python dependencies

└── README.md                         # This file


### How to Run the Pipeline

1. Open notebooks/pipeline.ipynb:

2. Select the proper kernel: Python (.venv) - Geospatial
3. Run all cells from top to bottom

It will:

1. Load parameters
2. Generate or read GeoJSON
3. Reproject and clean the data
4. Create buffer zones
5. Display an interactive Leaflet map

### Testing & Extending

You can:

* Replace data/sample_points.geojson with your own .geojson
* Modify the YAMLs in params/ to alter logic and behavior
* Extend src/ modules (e.g., more preprocessing rules, more complex spatial joins)

### Known Warnings and Fixes

**CRS Warning Fix:**

gdf_proj = gdf.to_crs(epsg=3857)
centroid = gdf_proj.centroid.to_crs(gdf.crs)
Avoid using .centroid directly on EPSG:4326; project first!

### To-Do / Next Steps

* Add unit tests (pytest, unittest)
* Add polygon/line handling
* Export output maps and KPIs
* Deploy the results through streamlit or shiny dashboards.


**Developed by Canalytics — Data & AI Engineering Solutions for Spatial Analytics.**
