#-------------------------------------------------------------------------------
# Name:        Convert from layer -to- .lyr
# Purpose:     intern
#
# Author:      rnicolescu
#
# Created:     30/06/2022
# Copyright:   (c) rnicolescu 2022
# Licence:     <your license here>
#-------------------------------------------------------------------------------

import arcpy, os


#Set the working directory to where the Python file is stored
cwd = os.getcwd()
mxd_path = raw_input("Enter mxd path where layers are stored:")
#Set the location of the MXD file
mxdPath = os.path.join(cwd, mxd_path)
#Set the location to store LYR files
layersOutPath = os.path.join(cwd,"export")
#Get the MXD and layers
mxd = arcpy.mapping.MapDocument(mxdPath)
layers = arcpy.mapping.ListLayers(mxd)
for layer in layers:
    if str(layer.name) == str(layer.longName):
        tempOutName = str(layer.name).replace("/","-")
        tempOutName = str(tempOutName).replace(":","-")
        fn = os.path.join(layersOutPath, str(tempOutName) + ".lyr")
        layer.saveACopy(fn)

print "LYR Extraction Complete"

