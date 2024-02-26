import geedim
import json

def read_polygon(geojson):
    """Reads a polygon identifying an area of interest from a GeoJSON file.

    Parameters
    ----------
    geojson: str
        A path to a valid GeoJSON file with a single polygon identifying an 
        area of interest.
    
    Returns
    -------
    dict
        A dictionary with the polygon.
    """
    with open(geojson, 'r') as fd:
        data = json.load(fd)
    return data["features"][0]["geometry"]

if __name__ == '__main__':
    pass
