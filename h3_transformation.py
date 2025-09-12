import h3
import json


class H3Transformation:
    @staticmethod
    def _generate_h3_metadata(h3_cell: str) -> dict:
        """
        Generate the metadata for a given H3 cell as a dict.
        """
        return {
            "h3_idx": h3_cell,
            "h3_is_valid": h3.h3_is_valid(h3_cell),
            "center": h3.h3_to_geo(h3_cell),
            "area_m2": h3.cell_area(h=h3_cell, unit="m^2"),
            "resolution": h3.h3_get_resolution(h3_cell),
        }

    @staticmethod
    def cells_to_geojson(
        h3_cells: set, default_properties=True, as_geometry=False
    ) -> str:
        """
        Convert a set of H3 cells to GeoJSON format.
        - If as_geometry is True, return only geometries without Feature/FeatureCollection structure.
        """
        if as_geometry:
            geometries = [
                {
                    "type": "Polygon",
                    "coordinates": [list(h3.h3_to_geo_boundary(h=cell, geo_json=True))],
                }
                for cell in h3_cells
            ]
            return json.dumps(geometries)

        # Only build features if not as_geometry
        features = [
            {
                "type": "Feature",
                "geometry": {
                    "type": "Polygon",
                    "coordinates": [list(h3.h3_to_geo_boundary(h=cell, geo_json=True))],
                },
                "properties": (
                    H3Transformation._generate_h3_metadata(cell)
                    if default_properties
                    else {}
                ),
            }
            for cell in h3_cells
        ]

        return json.dumps({"type": "FeatureCollection", "features": features})

    @staticmethod
    def cell_to_geojson(
        h3_cell: str, default_properties=True, as_geometry=False
    ) -> str:
        """
        Convert a single H3 cell to GeoJSON format.
        - If geometry_only is True, return only the geometry object.
        """
        geometry = {
            "type": "Polygon",
            "coordinates": [list(h3.h3_to_geo_boundary(h=h3_cell, geo_json=True))],
        }

        if as_geometry:
            return json.dumps(geometry)

        feature = {
            "type": "Feature",
            "geometry": geometry,
            "properties": (
                H3Transformation._generate_h3_metadata(h3_cell)
                if default_properties
                else {}
            ),
        }

        return json.dumps({"type": "FeatureCollection", "features": [feature]})
