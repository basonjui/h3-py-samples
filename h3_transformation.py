import h3
import json

class H3Transformation:
    
    @staticmethod
    def cells_to_geojson(h3_cells: set, include_default_properties=True, geometry_only=False) -> str:
        # Store GeoJSON Features:
        features = []
        geometries = []
        # Iterate H3 indexes and Transform into GeoJSON:
        for cell in h3_cells:
            geojson_Geometry = {
                "type": "Polygon", # Cell in H3 is always a GeoJSON Polygon
                "coordinates": [list(h3.h3_to_geo_boundary(h=cell, geo_json=True))]
            }
            geometries.append(geojson_Geometry)

            geojson_Feature = {
                "type": "Feature",
                "geometry": geojson_Geometry,
                "properties": {
                    "h3_idx": cell,
                    "h3_is_valid": h3.h3_is_valid(cell),
                    "center": h3.h3_to_geo(cell),
                    "area_m2": h3.cell_area(h=cell, unit="m^2"),
                    "resolution": h3.h3_get_resolution(cell)
                } if include_default_properties else {}
            }
            
            features.append(geojson_Feature)

        # Wrap Features into a FeatureCollection:
        geojson_FeatureCollection = {
            "type": "FeatureCollection", 
            "features": features
        }
        
        # Serialize to JSON:
        if geometry_only:
            geojson = json.dumps(geometries)
        else:
            geojson = json.dumps(geojson_FeatureCollection)
        
        return geojson
    
    @staticmethod
    def cell_to_geojson(h3_cell: str, include_default_properties=True, geometry_only=False) -> str:
        # Store GeoJSON Features:
        features = []
        
        # Iterate H3 indexes and Transform into GeoJSON:
        geojson_Geometry = {
            "type": "Polygon", # Cell in H3 is always a GeoJSON Polygon
            "coordinates": [list(h3.h3_to_geo_boundary(h=h3_cell, geo_json=True))]
        }

        geojson_Feature = {
            "type": "Feature",
            "geometry": geojson_Geometry,
            "properties": {
                "h3_idx": h3_cell,
                "h3_is_valid": h3.h3_is_valid(h3_cell),
                "center": h3.h3_to_geo(h3_cell),
                "area_m2": h3.cell_area(h=h3_cell, unit="m^2"),
                "resolution": h3.h3_get_resolution(h3_cell)
            } if include_default_properties else {}
        }
        
        features.append(geojson_Feature)

        # Wrap Features into a FeatureCollection:
        geojson_FeatureCollection = {
            "type": "FeatureCollection", 
            "features": features
        }
        
        # Serialize to JSON:
        if geometry_only:
            geojson = json.dumps(geojson_Geometry)
        else:
            geojson = json.dumps(geojson_FeatureCollection)
        
        return geojson