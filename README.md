# h3-py-samples

[![Python: 3.11.3](https://img.shields.io/badge/python-3.11.3-blue.svg)](https://www.python.org/downloads/release/python-3113/)
[![H3: v3.7.6](https://img.shields.io/badge/h3-v3.7.6-blue.svg)](https://github.com/uber/h3/releases/tag/v3.7.6)
[![License: MIT](https://img.shields.io/github/license/basonjui/h3-py-samples)](https://github.com/basonjui/h3-py-samples/blob/main/LICENSE)

> ⚠️ **Note**
>
> - To ensure compatibility, please use **`h3-py v3.7.6`**.  
> - The latest release of **h3-py** can be found [here](https://github.com/uber/h3-py/releases/latest), but it may not be compatible with this repository.

## About

### This repository

This repository contains sample notebooks & helper transformation functions of h3-py: Uber's H3 Hexagonal Hierarchical Geospatial Indexing System in Python.

As I continue to work on H3 projects and learn new things, I will update this repository with useful H3 samples, transformation functions, tips, and perhaps common challenges.

### H3

H3 is an open-source **hexagonal hierarchical geospatial indexing system** created by Uber and released under the Apache 2.0 license.  

It provides a way to partition the surface of the Earth into discrete, identifiable grid cells at multiple resolutions. Unlike traditional square or rectangular grids, H3 uses primarily **hexagons** (with a few pentagons for closure), which offer more uniform adjacency and minimize edge effects.  

H3 is widely used in geospatial analytics and location-based applications, enabling tasks such as:

- Aggregating and visualizing geospatial data at different resolutions.  
- Performing efficient spatial indexing and queries.  
- Supporting large-scale geospatial data pipelines and data warehouses.  
- Enabling real-time analytics in transportation, logistics, urban planning, and mobility platforms.

To learn more about H3:

- [H3: Uber’s Hexagonal Hierarchical Spatial Index](https://www.uber.com/en-VN/blog/h3/)
- [H3 Documentation](https://h3geo.org/docs/)
- [h3-py](https://github.com/uber/h3-py)

## Getting started

### 1. Clone the repository

```console
git clone https://github.com/basonjui/h3-py-samples.git
```

### 2. Installation

#### Using [Conda](https://docs.conda.io/en/latest/)

   1. [Install Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) (if you haven't already).

   2. Create a new Conda environment (with required dependencies) using the `environment.yaml` file:

      ```console
      conda env create -f environment.yaml
      ```

#### Using PIP

   1. [Install Python](https://www.python.org/downloads/) (if you haven't already).

   2. Create and activate a virtual environment named `h3-py`:

      ```console
      python -m venv h3-py
      source h3-py/bin/activate   # On Linux/Mac
      h3-py\Scripts\activate      # On Windows
      ```

   3. Install dependencies from `requirements.txt`:

      ```console
      pip install -r requirements.txt
      ```

### 3. Create a .env file (optional)

This step is only required if you want to run the sample notebook `h3_polyfill_administrative_pipeline.ipynb`, which connects to a PostgreSQL database to fetch administrative geometries.

   1. Ensure you have access to a PostgreSQL database (locally or remotely).

   2. Create a `.env` file in the root directory and add your PostgreSQL connection details:

      ```properties
      POSTGRES_HOST=
      POSTGRES_PORT=
      POSTGRES_USERNAME=
      POSTGRES_PASSWORD=
      ```

### 4. Run the notebooks

Use Jupyter Notebook (or VSCode with Jupyter Notebook extension).

## Usage

### Python scripts

- [h3_transformation](https://github.com/basonjui/h3-py-samples/blob/main/h3_transformation.py): perform data transformation on H3 cells, currently only support H3 -> GeoJSON.
- [pg_client](https://github.com/basonjui/h3-py-samples/blob/main/pg_client.py): a wrapper of psycopg2 - a Postgres database adapter for Python.

### Notebooks

- [h3_gettingstarted](https://github.com/basonjui/h3-py-samples/blob/main/h3_gettingstarted.ipynb): demonstrate several fundamental usages of H3 and H3Transformation.
- [h3_polyfill_administrative_pipeline](https://github.com/basonjui/h3-py-samples/blob/main/h3_polyfill_administrative_pipeline.ipynb): an end-to-end sample pipeline that generates H3 cells from "polyfilling" (`h3.polyfill`) an administrative geometry from PostgreSQL, convert the administrative geometry into GeoJSON polygons, and then save the generated H3 cells into a new table in the database.

## License

Distributed under the MIT License. See LICENSE.
