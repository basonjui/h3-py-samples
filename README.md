# h3-py

[TOC]

## About

### This repository

This repository contains sample notebooks & helper transformation functions of h3-py: Uber's H3 Hexagonal Hierarchical Geospatial Indexing System in Python. 

As I continue to work on H3 projects, I will update this repository with useful H3 samples and transformation functions.

### H3

H3 is a **Grid System** developed by Uber and is currently open source under Apache 2 license. Grid systems are critical to geospatial data analytics, which can be used to partition the Earth into identifiable & quantifiable grid cells.

To learn more about H3:

- [H3: Uber’s Hexagonal Hierarchical Spatial Index](https://www.uber.com/en-VN/blog/h3/)
- [H3 Documentation](https://h3geo.org/docs/)
- [h3-py Github](https://github.com/uber/h3-py)

## Notes 

Due to package availability on Conda, the h3-py package being used in this repository is in  `v3.7.6` (the latest H3 version is v.4). 

As of now, `v4.0.0 beta` has been released for h3-py on pip (https://github.com/uber/h3-py#announcement-v400-beta-released). However, to use the samples in this repo, please install h3-py `v.3.7.6` as v.4.0.0 has many breaking changes in the API.

## Getting started

1. Clone this repository to your computer

   ```bash
   git clone https://github.com/basonjui/h3-py-samples.git
   ```

2. Install dependencies

   Using [Conda](https://docs.conda.io/en/latest/):

   ```bash
   $ conda create --name <h3-py-env> --file requirements.txt
   ```

3. Create a .env file in the root directory, it should have the following variables:

   ```properties
   POSTGRES_HOST=
   POSTGRES_PORT=
   POSTGRES_USERNAME=
   POSTGRES_PASSWORD=
   ```

4. You are ready, run the notebooks (or use VSCode with Jupyter Notebook extension).

## Descriptions

### Utilities

- [h3_transformation](https://github.com/basonjui/h3-py-samples/blob/main/h3_transformation.py): perform data transformation on H3 cells, currently only support H3 -> GeoJSON.
- [pg_client](https://github.com/basonjui/h3-py-samples/blob/main/pg_client.py): a wrapper of psycopg2 - a Postgres database adapter for Python.

### Notebooks

- [h3_gettingstarted](https://github.com/basonjui/h3-py-samples/blob/main/h3_gettingstarted.ipynb): demonstrate several fundamental usages of H3 and H3Transformation.
- [h3_polyfill_administrative_pipeline](https://github.com/basonjui/h3-py-samples/blob/main/h3_polyfill_administrative_pipeline.ipynb): an end-to-end sample pipeline that generates H3 cells from "polyfilling" (`h3.polyfill`) an administrative geometry (in GeoJSON::MultiPolygon) from PostgreSQL, and then saves all H3 cells generated back into a new table in the database.

## License

Distributed under the MIT License. See LICENSE.