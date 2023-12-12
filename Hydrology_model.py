import arcpy
arcpy.ImportToolbox(r"@\Data Management Tools.tbx")
with arcpy.EnvManager(outputCoordinateSystem='PROJCS["NAD_1983_CSRS_Statistics_Canada_Lambert",GEOGCS["GCS_North_American_1983_CSRS",DATUM["D_North_American_1983_CSRS",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",6200000.0],PARAMETER["False_Northing",3000000.0],PARAMETER["Central_Meridian",-91.86666666666666],PARAMETER["Standard_Parallel_1",49.0],PARAMETER["Standard_Parallel_2",77.0],PARAMETER["Latitude_Of_Origin",63.390675],UNIT["Meter",1.0]]'):
    arcpy.management.Dissolve(
        in_features="StreamFea",
        out_feature_class=r"C:\docs\skills\hydrology\Stream\Etobicoke\Etobicoke.gdb\StreamFea_Dissolve",
        dissolve_field="grid_code",
        statistics_fields=None,
        multi_part="MULTI_PART",
        unsplit_lines="DISSOLVE_LINES",
        concatenation_separator=""
    )
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(outputCoordinateSystem='PROJCS["NAD_1983_Statistics_Canada_Lambert",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",6200000.0],PARAMETER["False_Northing",3000000.0],PARAMETER["Central_Meridian",-91.86666666666666],PARAMETER["Standard_Parallel_1",49.0],PARAMETER["Standard_Parallel_2",77.0],PARAMETER["Latitude_Of_Origin",63.390675],UNIT["Meter",1.0]]', mask="Etobicoke_utm"):
with arcpy.EnvManager(outputCoordinateSystem='PROJCS["NAD_1983_Statistics_Canada_Lambert",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",6200000.0],PARAMETER["False_Northing",3000000.0],PARAMETER["Central_Meridian",-91.86666666666666],PARAMETER["Standard_Parallel_1",49.0],PARAMETER["Standard_Parallel_2",77.0],PARAMETER["Latitude_Of_Origin",63.390675],UNIT["Meter",1.0]]', mask="Etobicoke_utm"):
    arcpy.sa.StreamToFeature(
        in_stream_raster="Stream_order",
        in_flow_direction_raster="Flow_dir",
        out_polyline_features=r"C:\docs\skills\hydrology\Stream\Etobicoke\Etobicoke.gdb\StreamFea",
        simplify="SIMPLIFY"
    )
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(mask="Etobicoke_utm", scratchWorkspace=r"C:\docs\skills\hydrology\Stream\Etobicoke\Etobicoke.gdb"):
    out_raster = arcpy.sa.StreamOrder(
        in_stream_raster="FlowAcc_RC",
        in_flow_direction_raster="Flow_dir",
        order_method="STRAHLER"
    )
    out_raster.save(r"C:\docs\skills\hydrology\Stream\Etobicoke\Etobicoke.gdb\Stream_order")
arcpy.ImportToolbox(r"@\Image Analyst Tools.tbx")
with arcpy.EnvManager(mask="Etobicoke_utm", scratchWorkspace=r"C:\docs\skills\hydrology\Stream\Etobicoke\Etobicoke.gdb"):
    output_raster = arcpy.ia.RasterCalculator(
        expression=' "Flow_Acc"<1200'
    )
    output_raster.save(r"C:\docs\skills\hydrology\Stream\Etobicoke\Etobicoke.gdb\FlowAcc_RC")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(outputCoordinateSystem='PROJCS["NAD_1983_CSRS_Statistics_Canada_Lambert",GEOGCS["GCS_North_American_1983_CSRS",DATUM["D_North_American_1983_CSRS",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",6200000.0],PARAMETER["False_Northing",3000000.0],PARAMETER["Central_Meridian",-91.86666666666666],PARAMETER["Standard_Parallel_1",49.0],PARAMETER["Standard_Parallel_2",77.0],PARAMETER["Latitude_Of_Origin",63.390675],UNIT["Meter",1.0]]', mask="Etobicoke_utm", scratchWorkspace=r"C:\docs\skills\hydrology\Stream\Etobicoke\Etobicoke.gdb"):
    out_accumulation_raster = arcpy.sa.FlowAccumulation(
        in_flow_direction_raster="Flow_dir",
        in_weight_raster=None,
        data_type="FLOAT",
        flow_direction_type="D8"
    )
    out_accumulation_raster.save(r"C:\docs\skills\hydrology\Stream\Etobicoke\Etobicoke.gdb\Flow_Acc")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(mask="Etobicoke_utm", scratchWorkspace=r"C:\docs\skills\hydrology\Stream\Etobicoke\Etobicoke.gdb"):
    out_flow_direction_raster = arcpy.sa.FlowDirection(
        in_surface_raster="Fill",
        force_flow="NORMAL",
        out_drop_raster=None,
        flow_direction_type="D8"
    )
    out_flow_direction_raster.save(r"C:\docs\skills\hydrology\Stream\Etobicoke\Etobicoke.gdb\Flow_dir")
arcpy.ImportToolbox(r"@\Spatial Analyst Tools.tbx")
with arcpy.EnvManager(outputCoordinateSystem='PROJCS["NAD_1983_Statistics_Canada_Lambert",GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",6200000.0],PARAMETER["False_Northing",3000000.0],PARAMETER["Central_Meridian",-91.86666666666666],PARAMETER["Standard_Parallel_1",49.0],PARAMETER["Standard_Parallel_2",77.0],PARAMETER["Latitude_Of_Origin",63.390675],UNIT["Meter",1.0]]', mask="Etobicoke_utm", scratchWorkspace=r"C:\docs\skills\hydrology\Stream\Etobicoke\Etobicoke.gdb"):
    out_surface_raster = arcpy.sa.Fill(
        in_surface_raster="etobicoke_dem",
        z_limit=None
    )
    out_surface_raster.save(r"C:\docs\skills\hydrology\Stream\Etobicoke\Etobicoke.gdb\Fill")
