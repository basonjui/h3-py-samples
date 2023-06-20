# h3-py

## About this repository 

Sample notebooks & helper transformation functions of h3-py: Uber's H3 Hexagonal Hierarchical Geospatial Indexing System in Python.

As I continue to work on H3 projects, I will keep updating this repository will useful notebooks and transformation helpers.


## About H3
H3 is a grid system developed by Uber and is currently open source under Apache 2 license. Grid systems are critical to geospatial data analytics, which are used to partition the Earth into identifiable & quantifiable grid cells.

To learn more about H3:
- [H3: Uber’s Hexagonal Hierarchical Spatial Index](https://www.uber.com/en-VN/blog/h3/)
- [H3 Documentation](https://h3geo.org/docs/)
- [h3-py Github](https://github.com/uber/h3-py)

## Notes 

Due to package availability on Conda, the h3-py package being used in this repository is in version 3.7.6 (the latest H3 version is v.4). 

As of now, v4.0.0 beta has been released for h3-py on pip (https://github.com/uber/h3-py#announcement-v400-beta-released). However, for the purpose of the demo, please install h3-py v.3.7.6 for this repository, as h3-py v.4.0.0 has many breaking changes in the API.


## Getting Started

1. Clone this repository to your computer

    ```bash
    git clone https://github.com/basonjui/h3-py-samples.git
    ```

2. Install dependencies

    From [conda](https://anaconda.org/conda-forge/h3-py):

    ```bash
    $ conda create --name <env> --file requirements.txt
    ```

3. Create a .env file in the root directory, it should have the following variables:

   ```
   POSTGRES_HOST=
   POSTGRES_PORT=
   POSTGRES_USERNAME=
   POSTGRES_PASSWORD=
   ```

3. You are ready. Run the notebooks (or use VSCode with Jupyter Notebook extension).


## Descriptions

### Utilities

- h3_transformation: perform data transformation on H3 cells, currently only support H3 -> GeoJSON.
- pg_client: a wrapper of psycopg2 - a Postgres database adapter for Python.

### Notebooks

- h3_gettingstarted: demonstrate several fundamental usages of H3 and H3Transformation.
- h3_polyfill_administrative_pipeline: an end-to-end sample pipeline that generates H3 cells from "polyfilling" (`h3.polyfill`) an administrative geometry (MultiPolygon) from Postgres database, and then saves all H3 cells generated back into a new table in Postgres.


## License

Distributed under the MIT License. See LICENSE.
