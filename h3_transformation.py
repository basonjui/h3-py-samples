import h3
import json

class H3Transformation:
    @staticmethod
    def h3_to_geojson(h3_cells: set) -> str:
        # Store GeoJSON Features:
        features = []
        
        # Iterate H3 indexes and Transform into GeoJSON:
        for cell in h3_cells:
            geometry = {
                "type": "Polygon", # Cell in H3 is always a GeoJSON Polygon
                "coordinates": [list(h3.h3_to_geo_boundary(h=cell, geo_json=True))]
            }

            feature = {
                "type": "Feature",
                "geometry": geometry,
                "properties": {
                    "h3_idx": cell,
                    "is_valid_cell": h3.h3_is_valid(cell),
                    "center": h3.h3_to_geo(cell),
                    "area_m2": h3.cell_area(h=cell, unit="m^2"),
                    "resolution": h3.h3_get_resolution(cell)
                }
            }
            
            features.append(feature)

        # Wrap Features into a FeatureCollection:
        geojson_FeatureCollection = {
            "type": "FeatureCollection", 
            "features": features
        }
        
        # Serialize to JSON:
        geojson = json.dumps(geojson_FeatureCollection)
        
        return geojson