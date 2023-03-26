from arcgis.gis import GIS
from arcgis.geocoding import geocode
from arcgis.geometry import Point

gis = GIS()

geocode_result = geocode(address="Hollywood sign", as_featureset=True)
geocode_result.features

m = gis.map("Los Angeles, CA", zoomlevel=11)
m