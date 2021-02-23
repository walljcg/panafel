import arcpy,ee
import pandas as pd
from datetime import datetime
    
	
def ConvertArcGISPolygonTo_RECT(ArcGISGeo):
    partnum = 0
    allCoords = [] #This will hold the different tuples of coordinates
    for part in ArcGISGeo:
        for pnt in ArcGISGeo.getPart(partnum):
            if pnt:
                xy=[pnt.X,pnt.Y]
                allCoords.append(xy)
        partnum += 1
	max_x = max(allCoords,key=lambda item:item[0])[0]
	min_x = min(allCoords,key=lambda item:item[0])[0]
	max_y = max(allCoords,key=lambda item:item[0])[1]
	min_y = min(allCoords,key=lambda item:item[0])[1]
	return ee.Geometry.Polygon([min_x,min_y,max_x,min_y,max_x,max_y,min_x,max_y,min_x,min_y])


def ConvertPandasDataFrameToFeatureCollection(pdDF):
    allFeatures=[]
    for i in range(0,len(outFeatureDataDF['Shape'])):
        rings=outFeatureDataDF['Shape'][i]
        poly = ee.Geometry.MultiPolygon(rings)
        GEEfeat = ee.Feature(poly,{'FeatName': outFeatureDataDF[nameColumn]})
        allFeatures.append(GEEfeat)
    return ee.FeatureCollection(allFeatures)
	
	#Define the UNIX Epoch start date
epoch = datetime(1970,1,1,0,0,0)

def convertUnixTimeToDateTime(unixTime):
    t=datetime.utcfromtimestamp(int(unixTime/1000))
    return t.strftime('%Y-%m-%d %H:%M:%S')
    
def convertDateTimeToUnixTime(inputTime):
    return int((inputTime-epoch).total_seconds()*1000) 