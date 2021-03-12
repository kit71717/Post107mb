# trace generated using paraview version 5.8.0
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

# import the simple module from the paraview
from paraview.simple import *
# disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

import math

"""
    ***********************************************************************************
    *                                                                                 *
    *                                                                                 *
    *                              INITIAL DATA FILE                                  *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    ***********************************************************************************
"""

# # create a new 'Tecplot Reader'
# flocase100dat = TecplotReader(
#     FileNames=['/Users/calvinli/Documents/Beluga/Syn3d_Output/flo.case1.00.dat'])
# flocase100dat.DataArrayStatus = ['RHO', 'RHO-U', 'RHO-V', 'RHO-W', 'RHO-E', 'P', 'T', 'M', 'P', 'UVW', 'U', 'V', 'W', 'TT', 'PT', 'RHOT', 'RLV', 'REV', 'MSTAR',
#                                  'S1', 'S2', 'VR', 'WR', 'UVWR', 'MR', 'TTR', 'PTR', 'RHOR', 'VTAN', 'VRAD', 'D2WALL', 'TKE', 'DISS', 'TKEND', 'TOMND', 'UPLUS', 'YPLUS', 'REVINF', 'F1', 'F2']

# # create a new 'Tecplot Reader'
# flocase167dat = TecplotReader(
#     FileNames=['/Users/calvinli/Documents/Beluga/Syn3d_Output/flo.case1.67.dat'])
# flocase167dat.DataArrayStatus = ['RHO', 'RHO-U', 'RHO-V', 'RHO-W', 'RHO-E', 'P', 'T', 'M', 'P', 'UVW', 'U', 'V', 'W', 'TT', 'PT', 'RHOT', 'RLV', 'REV', 'MSTAR',
#                                  'S1', 'S2', 'VR', 'WR', 'UVWR', 'MR', 'TTR', 'PTR', 'RHOR', 'VTAN', 'VRAD', 'D2WALL', 'TKE', 'DISS', 'TKEND', 'TOMND', 'UPLUS', 'YPLUS', 'REVINF', 'F1', 'F2']

# # create a new 'Tecplot Reader'
# wing_Analysis_100dat = TecplotReader(FileNames=['/Users/calvinli/Documents/Beluga/Fortran_Tutorial/Wing_Analysis_1.00.dat'])
# wing_Analysis_100dat.DataArrayStatus = ['RHO', 'RHO-U', 'RHO-V', 'RHO-W', 'RHO-E', 'P', 'T', 'M', 'C', 'UVW', 'U', 'V', 'W', 'TT', 'PT', 'RHOT', 'RLV', 'REV', 'MSTAR', 'S1', 'S2', 'VR', 'WR', 'UVWR', 'MR', 'TTR', 'PTR', 'RHOR', 'VTAN', 'VRAD', 'D2WALL', 'TKE', 'DISS', 'TKEND', 'TOMND', 'UPLUS', 'YPLUS', 'REVINF', 'F1', 'F2']


# # create a new 'Tecplot Reader'
# wing_Analysis_107dat = TecplotReader(FileNames=['/Users/calvinli/Documents/Beluga/Fortran_Tutorial/Wing_Analysis_1.07.dat'])
# wing_Analysis_107dat.DataArrayStatus = ['RHO', 'RHO-U', 'RHO-V', 'RHO-W', 'RHO-E', 'P', 'T', 'M', 'C', 'UVW', 'U', 'V', 'W', 'TT', 'PT', 'RHOT', 'RLV', 'REV', 'MSTAR', 'S1', 'S2', 'VR', 'WR', 'UVWR', 'MR', 'TTR', 'PTR', 'RHOR', 'VTAN', 'VRAD', 'D2WALL', 'TKE', 'DISS', 'TKEND', 'TOMND', 'UPLUS', 'YPLUS', 'REVINF', 'F1', 'F2']

# # find source
# tecplotReader1 = FindSource('TecplotReader1')

# # set active source
# SetActiveSource(tecplotReader1)

# # rename source object
# RenameSource('Wing_Analysis_1.00.dat', tecplotReader1)

# # find source
# tecplotReader2 = FindSource('TecplotReader2')

# # set active source
# SetActiveSource(tecplotReader2)

# # rename source object
# RenameSource('Wing_Analysis_1.07.dat', tecplotReader2)

# get active source.
file_1 = [k for (k, v) in GetSources().items()][0][0]
file_2 = [k for (k, v) in GetSources().items()][1][0]

print([k for (k, v) in GetSources().items()][0][0])
print([k for (k, v) in GetSources().items()][0][1])
print([k for (k, v) in GetSources().items()][1][0])
print([k for (k, v) in GetSources().items()][1][1])
#print([k for (k, v) in GetSources().items()][2][0])

# txt_3 = int(file_3[16:18:1])
# txt_4 = int(file_4[16:18:1])

# if txt_3 > txt_4:
#     file_1 = file_4
#     file_2 = file_3
# elif txt_4 > txt_3:
#     file_1 = file_3
#     file_2 = file_4

print(file_1)
print(file_2)

flocase100dat = FindSource(file_1)

# set active source
SetActiveSource(flocase100dat)

# Properties modified on flocase100dat
flocase100dat.DataArrayStatus = ['P', 'P0','RHO0', 'U0', 'V0']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1398, 650]

# get layout
layout1 = GetLayout()

# show data in view
flocase100datDisplay = Show(
    flocase100dat, renderView1, 'StructuredGridRepresentation')

# trace defaults for the display properties.
flocase100datDisplay.Representation = 'Outline'
flocase100datDisplay.ColorArrayName = [None, '']
flocase100datDisplay.OSPRayScaleArray = 'P'
flocase100datDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
flocase100datDisplay.SelectOrientationVectors = 'None'
flocase100datDisplay.ScaleFactor = 4.948406028747559
flocase100datDisplay.SelectScaleArray = 'None'
flocase100datDisplay.GlyphType = 'Arrow'
flocase100datDisplay.GlyphTableIndexArray = 'None'
flocase100datDisplay.GaussianRadius = 0.24742030143737795
flocase100datDisplay.SetScaleArray = ['POINTS', 'P']
flocase100datDisplay.ScaleTransferFunction = 'PiecewiseFunction'
flocase100datDisplay.OpacityArray = ['POINTS', 'P']
flocase100datDisplay.OpacityTransferFunction = 'PiecewiseFunction'
flocase100datDisplay.DataAxesGrid = 'GridAxesRepresentation'
flocase100datDisplay.PolarAxes = 'PolarAxesRepresentation'
flocase100datDisplay.ScalarOpacityUnitDistance = 1.2134293650719759

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
flocase100datDisplay.ScaleTransferFunction.Points = [
    0.4505206048488617, 0.0, 0.5, 0.0, 1.3989499807357788, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
flocase100datDisplay.OpacityTransferFunction.Points = [
    0.4505206048488617, 0.0, 0.5, 0.0, 1.3989499807357788, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# set scalar coloring
ColorBy(flocase100datDisplay, ('FIELD', 'vtkBlockColors'))

# show color bar/color legend
flocase100datDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# get active source.
wing_Analysis_100dat = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1470, 650]

"""
    ***********************************************************************************
    *                                                                                 *
    *                                                                                 *
    *                           PRESSURE CONTOUR MACRO                                *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    ***********************************************************************************
"""

# get color transfer function/color map for 'P'
pLUT = GetColorTransferFunction('P')

# get opacity transfer function/opacity map for 'P'
pPWF = GetOpacityTransferFunction('P')

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pLUT.ApplyPreset('jet', True)

# create a new 'Contour'
contour1 = Contour(Input=flocase100dat)
contour1.ContourBy = ['POINTS', 'P']
contour1.Isosurfaces = [0.9247352927923203]
contour1.PointMergeMethod = 'Uniform Binning'

# Properties modified on contour1
contour1.Isosurfaces = [0.4505206048488617, 0.5004379404218573, 0.550355275994853, 0.6002726115678486, 0.6501899471408442, 0.7001072827138399, 0.7500246182868355, 0.7999419538598311, 0.8498592894328267,
                        0.8997766250058225, 0.949693960578818, 0.9996112961518137, 1.0495286317248094, 1.099445967297805, 1.1493633028708006, 1.1992806384437964, 1.2491979740167918, 1.2991153095897876, 1.3490326451627832, 1.3989499807357788]

# show data in view
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.AmbientColor = [0.0, 0.0, 0.0]
contour1Display.ColorArrayName = ['POINTS', 'P']
contour1Display.DiffuseColor = [0.0, 0.0, 0.0]
contour1Display.LookupTable = pLUT
contour1Display.OSPRayScaleArray = 'P'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = 0.15228250026702883
contour1Display.SelectScaleArray = 'P'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'P'
contour1Display.GaussianRadius = 0.007614125013351441
contour1Display.SetScaleArray = ['POINTS', 'P']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = ['POINTS', 'P']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [
    0.5004379153251648, 0.0, 0.5, 0.0, 1.3989499807357788, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [
    0.5004379153251648, 0.0, 0.5, 0.0, 1.3989499807357788, 1.0, 0.5, 0.0]

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# turn off scalar coloring
ColorBy(contour1Display, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView1)

"""
    ***********************************************************************************
    *                                                                                 *
    *                                                                                 *
    *                               Get Wing Span                                     *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    ***********************************************************************************
"""

# find source
extractBlock1 = FindSource(file_1)

# create a new 'Clip'
clip1 = Clip(Input=flocase100dat)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'P']
clip1.Value = 0.9247352927923203

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.7139178766519763,
                         0.002191845327615738, 0.761412501335144]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [
    0.7139178766519763, 0.002191845327615738, 0.761412501335144]

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# Properties modified on clip1
clip1.ClipType = 'Box'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1398, 650]

# get layout
layout1 = GetLayout()

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# get color transfer function/color map for 'P'
pLUT = GetColorTransferFunction('P')

# get opacity transfer function/opacity map for 'P'
pPWF = GetOpacityTransferFunction('P')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = ['POINTS', 'P']
clip1Display.LookupTable = pLUT
clip1Display.OSPRayScaleArray = 'P'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 0.007614125013351441
clip1Display.SetScaleArray = ['POINTS', 'P']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'P']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = pPWF
clip1Display.ScalarOpacityUnitDistance = 0.20730811928381215
clip1Display.ExtractedBlockIndex = 1

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [
    0.4505206048488617, 0.0, 0.5, 0.0, 1.3989499807357788, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [
    0.4505206048488617, 0.0, 0.5, 0.0, 1.3989499807357788, 1.0, 0.5, 0.0]

# hide data in view
Hide(extractBlock1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# find source
flocase100dat = FindSource(file_1)

# Properties modified on flocase100dat
flocase100dat.DataArrayStatus = ['P', 'P0','RHO0', 'U0', 'V0']

# show data in view
flocase100datDisplay = Show(
    flocase100dat, renderView1, 'StructuredGridRepresentation')

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# trace defaults for the display properties.
flocase100datDisplay.Representation = 'Outline'
flocase100datDisplay.ColorArrayName = ['FIELD', 'vtkBlockColors']
flocase100datDisplay.LookupTable = vtkBlockColorsLUT
flocase100datDisplay.OSPRayScaleArray = 'P'
flocase100datDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
flocase100datDisplay.SelectOrientationVectors = 'None'
flocase100datDisplay.ScaleFactor = 4.948406028747559
flocase100datDisplay.SelectScaleArray = 'None'
flocase100datDisplay.GlyphType = 'Arrow'
flocase100datDisplay.GlyphTableIndexArray = 'None'
flocase100datDisplay.GaussianRadius = 0.24742030143737795
flocase100datDisplay.SetScaleArray = ['POINTS', 'P']
flocase100datDisplay.ScaleTransferFunction = 'PiecewiseFunction'
flocase100datDisplay.OpacityArray = ['POINTS', 'P']
flocase100datDisplay.OpacityTransferFunction = 'PiecewiseFunction'
flocase100datDisplay.DataAxesGrid = 'GridAxesRepresentation'
flocase100datDisplay.PolarAxes = 'PolarAxesRepresentation'
flocase100datDisplay.ScalarOpacityFunction = vtkBlockColorsPWF
flocase100datDisplay.ScalarOpacityUnitDistance = 1.2134293650719759

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
flocase100datDisplay.ScaleTransferFunction.Points = [
    0.4505206048488617, 0.0, 0.5, 0.0, 1.3989499807357788, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
flocase100datDisplay.OpacityTransferFunction.Points = [
    0.4505206048488617, 0.0, 0.5, 0.0, 1.3989499807357788, 1.0, 0.5, 0.0]

# show color bar/color legend
flocase100datDisplay.SetScalarBarVisibility(renderView1, True)

# find source
extractSubset1 = FindSource('ExtractSubset1')

# find source
contour1 = FindSource('Contour1')

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(extractBlock1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# hide data in view
Hide(clip1, renderView1)

#******************************CODE FOR SPAN EXTRACTION********************************

wing_span = clip1Display.ScaleFactor * 10

#******************************CODE FOR SPAN EXTRACTION********************************

# destroy clip1
Delete(clip1)
del clip1

# hide data in view
Hide(flocase100dat, renderView1)

# saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.8288592354896342,
                              2.3045195980984254, 2.626626171583404]
renderView1.CameraFocalPoint = [
    0.8610387645467205, 0.047899751027493234, 0.8429719923745055]
renderView1.CameraViewUp = [0.4184746762481223,
                            0.735041666731778, -0.533472298725247]
renderView1.CameraParallelScale = 1.0447674531991689

# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

"""
    ***********************************************************************************
    *                                                                                 *
    *                                                                                 *
    *                      SLICE MACRO - 2D CROSS SECTION                             *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    ***********************************************************************************
"""

# User Input
cross_num = float(input("How many cross section?"))
cross_num = int(cross_num)

print(cross_num)
print(" ")

user_input_array = []

for x in range(cross_num):

    offset = 0.2
    angle_degrees = 5
    second_offset = 0.4

    angle_num = angle_degrees * ( (x+1) * second_offset )

    span = wing_span

    # User Input
    g = float(input("What is the input?"))

    user_input_array.append(g)

    span_location = (g / 100) * span
    print("Wing Span is")
    print(span)

    print("Percentage is")
    print(g)

    print("location is thus at ")
    print(span_location)

    # create a new 'Slice'
    slice1 = Slice(Input=flocase100dat)
    slice1.SliceType = 'Plane'
    slice1.HyperTreeGridSlicer = 'Plane'
    slice1.SliceOffsetValues = [0.0]

    # init the 'Plane' selected for 'SliceType'
    slice1.SliceType.Origin = [0.7139178766519763,
                               0.002191845327615738, 0.761412501335144]

    # init the 'Plane' selected for 'HyperTreeGridSlicer'
    slice1.HyperTreeGridSlicer.Origin = [
        0.7139178766519763, 0.002191845327615738, 0.761412501335144]

    # Properties modified on slice1.SliceType
    slice1.SliceType.Origin = [0.7139178766519763,
                               0.002191845327615738, span_location]
    slice1.SliceType.Normal = [0.0, 0.0, 1.0]

    # show data in view
    slice1Display = Show(slice1, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    slice1Display.Representation = 'Surface'
    slice1Display.AmbientColor = [0.0, 0.0, 0.0]
    slice1Display.ColorArrayName = ['POINTS', 'P']
    slice1Display.DiffuseColor = [0.0, 0.0, 0.0]
    slice1Display.LookupTable = pLUT
    slice1Display.OSPRayScaleArray = 'P'
    slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice1Display.SelectOrientationVectors = 'None'
    slice1Display.ScaleFactor = 0.07750189006328584
    slice1Display.SelectScaleArray = 'None'
    slice1Display.GlyphType = 'Arrow'
    slice1Display.GlyphTableIndexArray = 'None'
    slice1Display.GaussianRadius = 0.0038750945031642914
    slice1Display.SetScaleArray = ['POINTS', 'P']
    slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice1Display.OpacityArray = ['POINTS', 'P']
    slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
    slice1Display.DataAxesGrid = 'GridAxesRepresentation'
    slice1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    slice1Display.ScaleTransferFunction.Points = [
        0.5479299426078796, 0.0, 0.5, 0.0, 1.3326448202133179, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    slice1Display.OpacityTransferFunction.Points = [
        0.5479299426078796, 0.0, 0.5, 0.0, 1.3326448202133179, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(extractBlock1, renderView1)

    # show color bar/color legend
    slice1Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # hide data in view
    Hide(contour1, renderView1)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=slice1.SliceType)

    # turn off scalar coloring
    ColorBy(slice1Display, None)

    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(pLUT, renderView1)

    # change solid color
    slice1Display.AmbientColor = [1.0, 0.0, 0.0]
    slice1Display.DiffuseColor = [1.0, 0.0, 0.0]

    # hide data in view
    Hide(slice1, renderView1)

    # reset view to fit data
    renderView1.ResetCamera()

    # set active source
    SetActiveSource(contour1)

    # show data in view
    contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

    """
        ***********************************************************************************
        *                                                                                 *
        *                                                                                 *
        *                    CREATE DATA POINTS FOR FIRST AIFOIL                          *
        *                                                                                 *
        *                                                                                 *
        *                                                                                 *
        ***********************************************************************************
    """

    # find source
    slice1 = FindSource('Slice1')

    # set active source
    SetActiveSource(slice1)

    # create a new 'Calculator'
    calculator1 = Calculator(Input=slice1)
    calculator1.Function = ''

    # find source
    flocase100dat = FindSource(file_1)

    # Properties modified on flocase100dat
    flocase100dat.DataArrayStatus = ['P', 'P0','RHO0', 'U0', 'V0']

    # find source
    flocase167dat = FindSource(file_2)

    # find source
    extractBlock1 = FindSource('ExtractBlock1')

    # find source
    extractSubset1 = FindSource('ExtractSubset1')

    #******************************************************* CUSTOM FORMULA FOR X *********************************************************

    # User Input
    #num = float(raw_input("What is the starting angle"))

    angle = angle_num * (math.pi / 180)
    angle_txt = str(angle)

    txt_1 = "cos("

    txt_1 += angle_txt

    txt_2 = ")*(coordsX) - sin("

    txt_1 += txt_2

    txt_1 += angle_txt

    txt_3 = ")*(coordsY)"

    txt_1 += txt_3

    x_text = str(x * offset)

    txt_4 = " + "

    txt_1 += txt_4

    txt_1 += x_text

    dummy_modify_x = "initial_modified_x_" + str(x + 1)

    #******************************************************* CUSTOM FORMULA *********************************************************

    # Properties modified on calculator1
    calculator1.ResultArrayName = dummy_modify_x
    calculator1.Function = txt_1

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    # uncomment following to set a specific view size
    # renderView1.ViewSize = [1464, 650]

    # get layout
    layout1 = GetLayout()

    # show data in view
    calculator1Display = Show(calculator1, renderView1,
                              'GeometryRepresentation')

    # get color transfer function/color map for 'modified_x_1'
    modified_x_1LUT = GetColorTransferFunction('modified_x_1')

    # trace defaults for the display properties.
    calculator1Display.Representation = 'Surface'
    calculator1Display.AmbientColor = [0.0, 0.0, 0.0]
    calculator1Display.ColorArrayName = ['POINTS', 'modified_x_1']
    calculator1Display.DiffuseColor = [0.0, 0.0, 0.0]
    calculator1Display.LookupTable = modified_x_1LUT
    calculator1Display.OSPRayScaleArray = 'modified_x_1'
    calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator1Display.SelectOrientationVectors = 'None'
    calculator1Display.ScaleFactor = 0.08940763026475906
    calculator1Display.SelectScaleArray = 'modified_x_1'
    calculator1Display.GlyphType = 'Arrow'
    calculator1Display.GlyphTableIndexArray = 'modified_x_1'
    calculator1Display.GaussianRadius = 0.004470381513237954
    calculator1Display.SetScaleArray = ['POINTS', 'modified_x_1']
    calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator1Display.OpacityArray = ['POINTS', 'modified_x_1']
    calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator1Display.ScaleTransferFunction.Points = [
        2.178731585561024, 0.0, 0.5, 0.0, 2.9530247232972995, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator1Display.OpacityTransferFunction.Points = [
        2.178731585561024, 0.0, 0.5, 0.0, 2.9530247232972995, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(slice1, renderView1)

    # show color bar/color legend
    calculator1Display.SetScalarBarVisibility(renderView1, True)

    # find source
    contour1 = FindSource('Contour1')

    # update the view to ensure updated data information
    renderView1.Update()

    # get opacity transfer function/opacity map for 'modified_x_1'
    modified_x_1PWF = GetOpacityTransferFunction('modified_x_1')

    # hide data in view
    Hide(calculator1, renderView1)

    # create a new 'Calculator'
    calculator2 = Calculator(Input=calculator1)
    calculator2.Function = ''

    #******************************************************* CUSTOM FORMULA FOR Y *********************************************************

    txt_1 = "sin("

    txt_1 += angle_txt

    txt_2 = ")*(coordsX) + cos("

    txt_1 += txt_2

    txt_1 += angle_txt

    txt_3 = ")*(coordsY)"

    txt_1 += txt_3

    x_text = str(x * offset)

    txt_4 = " + "

    txt_1 += txt_4

    txt_1 += x_text

    #Variable name
    dummy_modify_y = "initial_modified_y_" + str(x + 1)

    #******************************************************* CUSTOM FORMULA *********************************************************

    # Properties modified on calculator2
    calculator2.ResultArrayName = dummy_modify_y
    calculator2.Function = txt_1

    # show data in view
    calculator2Display = Show(calculator2, renderView1,
                              'GeometryRepresentation')

    # get color transfer function/color map for 'modified_y_1'
    modified_y_1LUT = GetColorTransferFunction('modified_y_1')

    # trace defaults for the display properties.
    calculator2Display.Representation = 'Surface'
    calculator2Display.AmbientColor = [0.0, 0.0, 0.0]
    calculator2Display.ColorArrayName = ['POINTS', 'modified_y_1']
    calculator2Display.DiffuseColor = [0.0, 0.0, 0.0]
    calculator2Display.LookupTable = modified_y_1LUT
    calculator2Display.OSPRayScaleArray = 'modified_y_1'
    calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator2Display.SelectOrientationVectors = 'None'
    calculator2Display.ScaleFactor = 0.08940763026475906
    calculator2Display.SelectScaleArray = 'modified_y_1'
    calculator2Display.GlyphType = 'Arrow'
    calculator2Display.GlyphTableIndexArray = 'modified_y_1'
    calculator2Display.GaussianRadius = 0.004470381513237954
    calculator2Display.SetScaleArray = ['POINTS', 'modified_y_1']
    calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator2Display.OpacityArray = ['POINTS', 'modified_y_1']
    calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator2Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator2Display.ScaleTransferFunction.Points = [
        2.094095694749427, 0.0, 0.5, 0.0, 2.550228094988033, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator2Display.OpacityTransferFunction.Points = [
        2.094095694749427, 0.0, 0.5, 0.0, 2.550228094988033, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(calculator1, renderView1)

    # show color bar/color legend
    calculator2Display.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    # get opacity transfer function/opacity map for 'modified_y_1'
    modified_y_1PWF = GetOpacityTransferFunction('modified_y_1')

    # hide data in view
    Hide(calculator2, renderView1)

    # saving camera placements for all active views

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.330858703392007,
                                  2.7327018602834356, 2.9196340581779046]
    renderView1.CameraFocalPoint = [
        0.7139178766519763, 0.002191845327615738, 0.761412501335144]
    renderView1.CameraViewUp = [0.4184746762481223,
                                0.735041666731778, -0.533472298725247]
    renderView1.CameraParallelScale = 1.0447674531991689

    # Change the name
    # find source
    slice1 = FindSource('Slice1')

    # set active source
    SetActiveSource(slice1)

    # Rename the Cross Section
    cross_name = "Initial_Cross_Z_at_"

    cross_name += str(g)

    cross_name += "%"

    # rename source object
    RenameSource(cross_name, slice1)

    # Rename the First data point and Second data point
    modified_x_name = "Initial_Modified_x_"

    modified_x_name += str(x + 1)

    modified_y_name = "Initial_Modified_y_"

    modified_y_name += str(x + 1)

    # find source
    calculator1 = FindSource('Calculator1')

    # set active source
    SetActiveSource(calculator1)

    # rename source object
    RenameSource(modified_x_name, calculator1)

    # find source
    calculator2 = FindSource('Calculator2')

    # set active source
    SetActiveSource(calculator2)

    # rename source object
    RenameSource(modified_y_name, calculator2)

# """
#     ***********************************************************************************
#     *                                                                                 *
#     *                                                                                 *
#     *                    CREATE LAYOUT TWO FOR STORING AIRFOIL                        *
#     *                               PLOTTING DATA                                     *
#     *                                                                                 *
#     *                                                                                 *
#     ***********************************************************************************
# """
CreateLayout('Layout #2')

for k in range(cross_num):

    # Rename the First data point and Second data point
    modified_x_name_2 = "Initial_Modified_x_"

    modified_x_name_2 += str(k + 1)

    modified_y_name_2 = "Initial_Modified_y_"

    modified_y_name_2 += str(k + 1)

    # find source
    modified_y_1 = FindSource(modified_y_name_2)

    # set active source
    SetActiveSource(modified_y_1)

    # create a new 'Plot Data'
    plotData1 = PlotData(Input=modified_y_1)

    # find source
    flocase100dat = FindSource(file_1)

    # Properties modified on flocase100dat
    flocase100dat.DataArrayStatus = ['P', 'P0','RHO0', 'U0', 'V0']

    # find source
    flocase167dat = FindSource(file_2)

    # find source
    modified_x_1 = FindSource(modified_x_name_2)

    if k == 0:
        # Create a new 'Line Chart View'
        lineChartView1 = CreateView('XYChartView')
        # uncomment following to set a specific view size
        # lineChartView1.ViewSize = [400, 400]

    # show data in view
    plotData1Display = Show(plotData1, lineChartView1, 'XYChartRepresentation')

    # get layout
    layout2 = GetLayoutByName("Layout #2")

    # add view to a layout so it's visible in UI
    AssignViewToLayout(view=lineChartView1, layout=layout2, hint=0)

    x_array_name = "initial_modified_x_" + str(k+1)

    # # Properties modified on plotData1Display
    # plotData1Display.XArrayName = x_array_name

    # # Properties modified on plotData1Display
    # plotData1Display.CompositeDataSetIndex = [1, 2]

    # Properties modified on plotData1Display
    plotData1Display.UseIndexForXAxis = 0

    # # Properties modified on plotData1Display
    # plotData1Display.SeriesVisibility = []

    # series_name_1 = "initial_modified_y_"
    # series_name_1 += str(k + 1)
    # series_name_1 += " (zone00001)"

    # series_name_2 = "initial_modified_y_"
    # series_name_2 += str(k + 1)
    # series_name_2 += " (zone00002)"

    # # Properties modified on plotData1Display
    # plotData1Display.SeriesVisibility = [series_name_1]

    # # Properties modified on plotData1Display
    # plotData1Display.SeriesVisibility = [
    #     series_name_1, series_name_2]

    # initial_dummy_x = "initial_modified_x_" + str(k+1) + " (zone00001)"
    # initial_dummy_y = "initial_modified_y_" + str(k+1) + " (zone00001)"

    # initial_dummy_x_zone_2 = "initial_modified_x_" + str(k+1) + " (zone00002)"
    # initial_dummy_y_zone_2 = "initial_modified_y_" + str(k+1) + " (zone00002)"

    # # Properties modified on plotData1Display
    # plotData1Display.SeriesColor = ['C (zone00001)', '0', '0', '0', initial_dummy_x, '0.889998', '0.100008', '0.110002', 'Points_X (zone00001)', '0.300008', '0.689998', '0.289998', 'Points_Y (zone00001)', '0.6', '0.310002', '0.639994', 'Points_Z (zone00001)', '1', '0.500008', '0', 'Points_Magnitude (zone00001)', '0.650004', '0.340002', '0.160006', 'C (zone00002)', '0', '0', '0', initial_dummy_x_zone_2, '0.889998', '0.100008', '0.110002', 'Points_X (zone00002)', '0.300008', '0.689998', '0.289998', 'Points_Y (zone00002)', '0.6', '0.310002', '0.639994', 'Points_Z (zone00002)', '1', '0.500008', '0', 'Points_Magnitude (zone00002)', '0.650004', '0.340002', '0.160006', initial_dummy_y, '1', '0', '0', initial_dummy_y_zone_2, '0', '0', '0']

    # # Properties modified on plotData1Display
    # plotData1Display.SeriesColor = ['C (zone00001)', '0', '0', '0', initial_dummy_x, '0.889998', '0.100008', '0.110002', 'Points_X (zone00001)', '0.300008', '0.689998', '0.289998', 'Points_Y (zone00001)', '0.6', '0.310002', '0.639994', 'Points_Z (zone00001)', '1', '0.500008', '0', 'Points_Magnitude (zone00001)', '0.650004', '0.340002', '0.160006', 'C (zone00002)', '0', '0', '0', initial_dummy_x_zone_2, '0.889998', '0.100008', '0.110002', 'Points_X (zone00002)', '0.300008', '0.689998', '0.289998', 'Points_Y (zone00002)', '0.6', '0.310002', '0.639994', 'Points_Z (zone00002)', '1', '0.500008', '0', 'Points_Magnitude (zone00002)', '0.650004', '0.340002', '0.160006', initial_dummy_y, '1', '0', '0', initial_dummy_y_zone_2, '1', '0', '0']

    print("")
    print("")
    print("********************START OF INITIAL_MOD**********************")

    plotData1Display.CompositeDataSetIndex = []

    m = []
    for i in range(10000):
        m.append(i)

    plotData1Display.CompositeDataSetIndex = m

    myint = 1

    myint = len(plotData1Display.SeriesVisibility)

    print(plotData1Display.SeriesVisibility)
    print("the lenght is")
    print(myint)

    new_array= []
    store = 0
    result = 0

    for i in range(myint):
        result = plotData1Display.SeriesVisibility[i].find('initial_modified_y_')

        if result != -1:
            print(result)
            new_array.append(plotData1Display.SeriesVisibility[i])
            store = store + 1

    a = []
    b = []
    num = 0
    hello = '0'
    red = '1'

    print(myint)

    for i in range(store):

        a.append(new_array[i])
        b.append(new_array[i])

        for k in range(3):
            if k == 0:
                b.append(red)
            else:
                b.append(hello)

    # for x in range(len(plotData5Display.SeriesVisibility)):
    #     print plotData5Display.SeriesVisibility[x]

    print("AFTER")
    print(a)

    plotData1Display.SeriesVisibility = a
    plotData1Display.SeriesColor = b

    print("********************END OF INITIAL_MOD**********************")
    print("")
    print("")

# THE FOLLOWING WILL BE AT THE END FOR HIDING LEGEND AND HIDING THE GRIDS
# Properties modified on lineChartView1
lineChartView1.ShowLegend = 0

# Properties modified on lineChartView1
lineChartView1.ShowLeftAxisGrid = 0

# Properties modified on lineChartView1
lineChartView1.ShowBottomAxisGrid = 0

"""
    ***********************************************************************************
    *                                                                                 *
    *                                                                                 *
    *                               RENAME DATA FILE                                  *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    ***********************************************************************************
"""
# find source
extractSubset1 = FindSource('ExtractSubset1')

# set active source
SetActiveSource(extractSubset1)

# rename source object
RenameSource('Subset_1', extractSubset1)

# find source
extractBlock1 = FindSource('ExtractBlock1')

# set active source
SetActiveSource(extractBlock1)

# rename source object
RenameSource('Wing_Initial_Case', extractBlock1)

# find source
contour1 = FindSource('Contour1')

# set active source
SetActiveSource(contour1)

# rename source object
RenameSource('Pressure_Contour_1', contour1)

"""
    ***********************************************************************************
    *                                                                                 *
    *                                                                                 *
    *                               FINAL DATA FILE                                   *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    ***********************************************************************************
"""

# find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1398, 650]

# get layout
layout1 = GetLayoutByName("Layout #1")

# set active view
SetActiveView(renderView1)

# split cell
layout1.SplitHorizontal(0, 0.5)

#set active view
SetActiveView(None)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraFocalDisk = 1.0
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1
# uncomment following to set a specific view size
# renderView2.ViewSize = [400, 400]

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView2, layout=layout1, hint=2)

# find source
flocase167dat = FindSource(file_2)

# set active source
SetActiveSource(flocase167dat)

# Properties modified on flocase167dat
flocase167dat.DataArrayStatus = ['P', 'P0','RHO0', 'U0', 'V0']

# find source
flocase100dat = FindSource(file_1)

# Properties modified on flocase100dat
flocase100dat.DataArrayStatus = ['P', 'P0','RHO0', 'U0', 'V0']

# update the view to ensure updated data information
renderView1.Update()

# find view
lineChartView1 = FindViewOrCreate('LineChartView1', viewtype='XYChartView')
# uncomment following to set a specific view size
# lineChartView1.ViewSize = [1398, 650]

# get layout
layout2 = GetLayoutByName("Layout #2")

# update the view to ensure updated data information
lineChartView1.Update()

# set active source
SetActiveSource(flocase167dat)

# show data in view
flocase167datDisplay = Show(flocase167dat, renderView2, 'StructuredGridRepresentation')

# trace defaults for the display properties.
flocase167datDisplay.Representation = 'Outline'
flocase167datDisplay.ColorArrayName = [None, '']
flocase167datDisplay.OSPRayScaleArray = 'P'
flocase167datDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
flocase167datDisplay.SelectOrientationVectors = 'None'
flocase167datDisplay.ScaleFactor = 4.948406028747559
flocase167datDisplay.SelectScaleArray = 'None'
flocase167datDisplay.GlyphType = 'Arrow'
flocase167datDisplay.GlyphTableIndexArray = 'None'
flocase167datDisplay.GaussianRadius = 0.24742030143737795
flocase167datDisplay.SetScaleArray = ['POINTS', 'P']
flocase167datDisplay.ScaleTransferFunction = 'PiecewiseFunction'
flocase167datDisplay.OpacityArray = ['POINTS', 'P']
flocase167datDisplay.OpacityTransferFunction = 'PiecewiseFunction'
flocase167datDisplay.DataAxesGrid = 'GridAxesRepresentation'
flocase167datDisplay.PolarAxes = 'PolarAxesRepresentation'
flocase167datDisplay.ScalarOpacityUnitDistance = 1.2134293650719759

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
flocase167datDisplay.ScaleTransferFunction.Points = [0.4926852881908417, 0.0, 0.5, 0.0, 1.4549139738082886, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
flocase167datDisplay.OpacityTransferFunction.Points = [0.4926852881908417, 0.0, 0.5, 0.0, 1.4549139738082886, 1.0, 0.5, 0.0]

# reset view to fit data
renderView2.ResetCamera()

# update the view to ensure updated data information
renderView2.Update()

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# hide data in view
Hide(flocase167dat, renderView2)

# reset view to fit data
renderView2.ResetCamera()

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView2)

# get color transfer function/color map for 'P'
pLUT = GetColorTransferFunction('P')

# get opacity transfer function/opacity map for 'P'
pPWF = GetOpacityTransferFunction('P')

# create a new 'Contour'
contour2 = Contour(Input=flocase167dat)
contour2.ContourBy = ['POINTS', 'P']
contour2.Isosurfaces = [0.9737996309995651]
contour2.PointMergeMethod = 'Uniform Binning'

# Properties modified on contour2
contour2.Isosurfaces = [0.4926852881908417, 0.5327781500915686, 0.5728710119922956, 0.6129638738930225, 0.6530567357937495, 0.6931495976944764, 0.7332424595952034, 0.7733353214959303, 0.8134281833966572, 0.8535210452973843, 0.8936139071981112, 0.9337067690988381, 0.9737996309995651, 1.013892492900292, 1.053985354801019, 1.094078216701746, 1.1341710786024728, 1.1742639405031998, 1.2143568024039268, 1.2544496643046537, 1.2945425262053807, 1.3346353881061077, 1.3747282500068345, 1.4148211119075615, 1.4549139738082886]

# show data in view
contour2Display = Show(contour2, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
contour2Display.Representation = 'Surface'
contour2Display.AmbientColor = [0.0, 0.0, 0.0]
contour2Display.ColorArrayName = ['POINTS', 'P']
contour2Display.DiffuseColor = [0.0, 0.0, 0.0]
contour2Display.LookupTable = pLUT
contour2Display.OSPRayScaleArray = 'P'
contour2Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour2Display.SelectOrientationVectors = 'None'
contour2Display.ScaleFactor = 0.15228250026702883
contour2Display.SelectScaleArray = 'P'
contour2Display.GlyphType = 'Arrow'
contour2Display.GlyphTableIndexArray = 'P'
contour2Display.GaussianRadius = 0.007614125013351441
contour2Display.SetScaleArray = ['POINTS', 'P']
contour2Display.ScaleTransferFunction = 'PiecewiseFunction'
contour2Display.OpacityArray = ['POINTS', 'P']
contour2Display.OpacityTransferFunction = 'PiecewiseFunction'
contour2Display.DataAxesGrid = 'GridAxesRepresentation'
contour2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour2Display.ScaleTransferFunction.Points = [0.5327781438827515, 0.0, 0.5, 0.0, 1.4549139738082886, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour2Display.OpacityTransferFunction.Points = [0.5327781438827515, 0.0, 0.5, 0.0, 1.4549139738082886, 1.0, 0.5, 0.0]

# show color bar/color legend
contour2Display.SetScalarBarVisibility(renderView2, True)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# turn off scalar coloring
ColorBy(contour2Display, None)

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pLUT, renderView2)

#### saving camera placements for all active views

# current camera placement for renderView2
renderView2.CameraPosition = [-1.027335546279149, 3.3710856279737498, 2.2283111946857734]
renderView2.CameraFocalPoint = [0.7139178766519763, 0.005928996950387787, 0.7614125013351438]
renderView2.CameraViewUp = [0.5780605131115787, 0.5584556796961724, -0.5949565505112661]
renderView2.CameraParallelScale = 1.051583863629504

# current camera placement for renderView1
renderView1.CameraPosition = [-1.330858703392007, 2.7327018602834356, 2.9196340581779046]
renderView1.CameraFocalPoint = [0.7139178766519763, 0.002191845327615738, 0.761412501335144]
renderView1.CameraViewUp = [0.4184746762481223, 0.735041666731778, -0.533472298725247]
renderView1.CameraParallelScale = 1.0447674531991689


"""
    ***********************************************************************************
    *                                                                                 *
    *                                                                                 *
    *                      SLICE MACRO - 2D CROSS SECTION                             *
    *                                FINAL DATA                                       *
    *                                                                                 *
    *                                                                                 *
    ***********************************************************************************
"""

for x in range(cross_num):

    angle_num = angle_degrees * ( (x+1) * second_offset )

    span = wing_span

    # User Input
    g = user_input_array[x]

    span_location = (g / 100) * span
    print("Wing Span is")
    print(span)

    print("Percentage is")
    print(g)

    print("location is thus at ")
    print(span_location)

    extractBlock1 = FindSource('ExtractBlock1')

    # create a new 'Slice'
    slice1 = Slice(Input=flocase167dat)
    slice1.SliceType = 'Plane'
    slice1.HyperTreeGridSlicer = 'Plane'
    slice1.SliceOffsetValues = [0.0]

    # init the 'Plane' selected for 'SliceType'
    slice1.SliceType.Origin = [0.7139178766519763,
                               0.002191845327615738, 0.761412501335144]

    # init the 'Plane' selected for 'HyperTreeGridSlicer'
    slice1.HyperTreeGridSlicer.Origin = [
        0.7139178766519763, 0.002191845327615738, 0.761412501335144]

    # Properties modified on slice1.SliceType
    slice1.SliceType.Origin = [0.7139178766519763,
                               0.002191845327615738, span_location]
    slice1.SliceType.Normal = [0.0, 0.0, 1.0]

    # show data in view
    slice1Display = Show(slice1, renderView2, 'GeometryRepresentation')

    # trace defaults for the display properties.
    slice1Display.Representation = 'Surface'
    slice1Display.AmbientColor = [0.0, 0.0, 0.0]
    slice1Display.ColorArrayName = ['POINTS', 'P']
    slice1Display.DiffuseColor = [0.0, 0.0, 0.0]
    slice1Display.LookupTable = pLUT
    slice1Display.OSPRayScaleArray = 'P'
    slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice1Display.SelectOrientationVectors = 'None'
    slice1Display.ScaleFactor = 0.07750189006328584
    slice1Display.SelectScaleArray = 'None'
    slice1Display.GlyphType = 'Arrow'
    slice1Display.GlyphTableIndexArray = 'None'
    slice1Display.GaussianRadius = 0.0038750945031642914
    slice1Display.SetScaleArray = ['POINTS', 'P']
    slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice1Display.OpacityArray = ['POINTS', 'P']
    slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
    slice1Display.DataAxesGrid = 'GridAxesRepresentation'
    slice1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    slice1Display.ScaleTransferFunction.Points = [
        0.5479299426078796, 0.0, 0.5, 0.0, 1.3326448202133179, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    slice1Display.OpacityTransferFunction.Points = [
        0.5479299426078796, 0.0, 0.5, 0.0, 1.3326448202133179, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(extractBlock1, renderView2)

    # show color bar/color legend
    slice1Display.SetScalarBarVisibility(renderView2, True)

    # update the view to ensure updated data information
    renderView2.Update()

    # hide data in view
    Hide(contour1, renderView2)

    # toggle 3D widget visibility (only when running from the GUI)
    Hide3DWidgets(proxy=slice1.SliceType)

    # turn off scalar coloring
    ColorBy(slice1Display, None)

    # Hide the scalar bar for this color map if no visible data is colored by it.
    HideScalarBarIfNotNeeded(pLUT, renderView2)

    # change solid color
    slice1Display.AmbientColor = [1.0, 0.0, 0.0]
    slice1Display.DiffuseColor = [1.0, 0.0, 0.0]

    # hide data in view
    Hide(slice1, renderView2)

    # reset view to fit data
    renderView2.ResetCamera()

    # set active source
    SetActiveSource(contour1)

    # show data in view
    contour1Display = Show(contour1, renderView2, 'GeometryRepresentation')

    """
        ***********************************************************************************
        *                                                                                 *
        *                                                                                 *
        *                    CREATE DATA POINTS FOR FIRST AIFOIL                          *
        *                               CALCULATOR                                        *
        *                                                                                 *
        *                                                                                 *
        ***********************************************************************************
    """

    # find source
    slice1 = FindSource('Slice1')

    # set active source
    SetActiveSource(slice1)

    # create a new 'Calculator'
    calculator1 = Calculator(Input=slice1)
    calculator1.Function = ''

    # find source
    flocase100dat = FindSource(file_1)

    # Properties modified on flocase100dat
    flocase100dat.DataArrayStatus = ['P', 'P0','RHO0', 'U0', 'V0']

    # find source
    flocase167dat = FindSource(file_2)

    # find source
    extractBlock1 = FindSource('ExtractBlock1')

    # find source
    extractSubset1 = FindSource('ExtractSubset1')

    #******************************************************* CUSTOM FORMULA FOR X *********************************************************

    # User Input
    #num = float(raw_input("What is the starting angle"))

    angle = angle_num * (math.pi / 180)
    angle_txt = str(angle)

    txt_1 = "cos("

    txt_1 += angle_txt

    txt_2 = ")*(coordsX) - sin("

    txt_1 += txt_2

    txt_1 += angle_txt

    txt_3 = ")*(coordsY)"

    txt_1 += txt_3

    x_text = str(x * offset)

    txt_4 = " + "

    txt_1 += txt_4

    txt_1 += x_text

    dummy_modify_x = "Final_modified_x_" + str(x + 1)

    #******************************************************* CUSTOM FORMULA *********************************************************

    # Properties modified on calculator1
    calculator1.ResultArrayName = dummy_modify_x
    calculator1.Function = txt_1

    # get active view
    renderView2 = GetActiveViewOrCreate('RenderView')
    # uncomment following to set a specific view size
    # renderView1.ViewSize = [1464, 650]

    # get layout
    layout1 = GetLayout()

    # show data in view
    calculator1Display = Show(calculator1, renderView2,
                              'GeometryRepresentation')

    # get color transfer function/color map for 'modified_x_1'
    modified_x_1LUT = GetColorTransferFunction('modified_x_1')

    # trace defaults for the display properties.
    calculator1Display.Representation = 'Surface'
    calculator1Display.AmbientColor = [0.0, 0.0, 0.0]
    calculator1Display.ColorArrayName = ['POINTS', 'modified_x_1']
    calculator1Display.DiffuseColor = [0.0, 0.0, 0.0]
    calculator1Display.LookupTable = modified_x_1LUT
    calculator1Display.OSPRayScaleArray = 'modified_x_1'
    calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator1Display.SelectOrientationVectors = 'None'
    calculator1Display.ScaleFactor = 0.08940763026475906
    calculator1Display.SelectScaleArray = 'modified_x_1'
    calculator1Display.GlyphType = 'Arrow'
    calculator1Display.GlyphTableIndexArray = 'modified_x_1'
    calculator1Display.GaussianRadius = 0.004470381513237954
    calculator1Display.SetScaleArray = ['POINTS', 'modified_x_1']
    calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator1Display.OpacityArray = ['POINTS', 'modified_x_1']
    calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator1Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator1Display.ScaleTransferFunction.Points = [
        2.178731585561024, 0.0, 0.5, 0.0, 2.9530247232972995, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator1Display.OpacityTransferFunction.Points = [
        2.178731585561024, 0.0, 0.5, 0.0, 2.9530247232972995, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(slice1, renderView2)

    # show color bar/color legend
    calculator1Display.SetScalarBarVisibility(renderView2, True)

    # find source
    contour1 = FindSource('Contour1')

    # update the view to ensure updated data information
    renderView2.Update()

    # get opacity transfer function/opacity map for 'modified_x_1'
    modified_x_1PWF = GetOpacityTransferFunction('modified_x_1')

    # hide data in view
    Hide(calculator1, renderView2)

    # create a new 'Calculator'
    calculator2 = Calculator(Input=calculator1)
    calculator2.Function = ''

    #******************************************************* CUSTOM FORMULA FOR Y *********************************************************

    txt_1 = "sin("

    txt_1 += angle_txt

    txt_2 = ")*(coordsX) + cos("

    txt_1 += txt_2

    txt_1 += angle_txt

    txt_3 = ")*(coordsY)"

    txt_1 += txt_3

    x_text = str(x * offset)

    txt_4 = " + "

    txt_1 += txt_4

    txt_1 += x_text

    dummy_modify_y = "Final_modified_y_" + str(x + 1)

    #******************************************************* CUSTOM FORMULA *********************************************************

    # Properties modified on calculator2
    calculator2.ResultArrayName = dummy_modify_y
    calculator2.Function = txt_1

    # show data in view
    calculator2Display = Show(calculator2, renderView2,
                              'GeometryRepresentation')

    # get color transfer function/color map for 'modified_y_1'
    modified_y_1LUT = GetColorTransferFunction('modified_y_1')

    # trace defaults for the display properties.
    calculator2Display.Representation = 'Surface'
    calculator2Display.AmbientColor = [0.0, 0.0, 0.0]
    calculator2Display.ColorArrayName = ['POINTS', 'modified_y_1']
    calculator2Display.DiffuseColor = [0.0, 0.0, 0.0]
    calculator2Display.LookupTable = modified_y_1LUT
    calculator2Display.OSPRayScaleArray = 'modified_y_1'
    calculator2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator2Display.SelectOrientationVectors = 'None'
    calculator2Display.ScaleFactor = 0.08940763026475906
    calculator2Display.SelectScaleArray = 'modified_y_1'
    calculator2Display.GlyphType = 'Arrow'
    calculator2Display.GlyphTableIndexArray = 'modified_y_1'
    calculator2Display.GaussianRadius = 0.004470381513237954
    calculator2Display.SetScaleArray = ['POINTS', 'modified_y_1']
    calculator2Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator2Display.OpacityArray = ['POINTS', 'modified_y_1']
    calculator2Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator2Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator2Display.PolarAxes = 'PolarAxesRepresentation'

    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator2Display.ScaleTransferFunction.Points = [
        2.094095694749427, 0.0, 0.5, 0.0, 2.550228094988033, 1.0, 0.5, 0.0]

    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator2Display.OpacityTransferFunction.Points = [
        2.094095694749427, 0.0, 0.5, 0.0, 2.550228094988033, 1.0, 0.5, 0.0]

    # hide data in view
    Hide(calculator1, renderView2)

    # show color bar/color legend
    calculator2Display.SetScalarBarVisibility(renderView2, True)

    # update the view to ensure updated data information
    renderView2.Update()

    # get opacity transfer function/opacity map for 'modified_y_1'
    modified_y_1PWF = GetOpacityTransferFunction('modified_y_1')

    # hide data in view
    Hide(calculator2, renderView2)

    # saving camera placements for all active views

    # current camera placement for renderView1
    renderView2.CameraPosition = [-1.330858703392007,
                                  2.7327018602834356, 2.9196340581779046]
    renderView2.CameraFocalPoint = [
        0.7139178766519763, 0.002191845327615738, 0.761412501335144]
    renderView2.CameraViewUp = [0.4184746762481223,
                                0.735041666731778, -0.533472298725247]
    renderView2.CameraParallelScale = 1.0447674531991689

    # Change the name
    # find source
    slice1 = FindSource('Slice1')

    # set active source
    SetActiveSource(slice1)

    # Rename the Cross Section
    cross_name = "Final_Cross_Z_at_"

    cross_name += str(g)

    cross_name += "%"

    # rename source object
    RenameSource(cross_name, slice1)

    # Rename the First data point and Second data point
    modified_x_name = "Final_Modified_x_"

    modified_x_name += str(x + 1)

    modified_y_name = "Final_Modified_y_"

    modified_y_name += str(x + 1)

    # find source
    calculator1 = FindSource('Calculator1')

    # set active source
    SetActiveSource(calculator1)

    # rename source object
    RenameSource(modified_x_name, calculator1)

    # find source
    calculator2 = FindSource('Calculator2')

    # set active source
    SetActiveSource(calculator2)

    # rename source object
    RenameSource(modified_y_name, calculator2)

# find source
wing_Initial_Case = FindSource('Wing_Initial_Case')

# get active view
renderView2 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView2.ViewSize = [694, 650]

# get layout
layout1 = GetLayout()

# hide data in view
Hide(wing_Initial_Case, renderView2)

# find source
pressure_Contour_1 = FindSource('Pressure_Contour_1')

# hide data in view
Hide(pressure_Contour_1, renderView2)


# """
#     ***********************************************************************************
#     *                                                                                 *
#     *                                                                                 *
#     *                    SELECT LAYOUT TWO FOR STORING AIRFOIL                        *
#     *                               PLOTTING DATA                                     *
#     *                                                                                 *
#     *                                                                                 *
#     ***********************************************************************************
# """

for k in range(cross_num):

    # find view
    lineChartView1 = FindViewOrCreate('LineChartView1', viewtype='XYChartView')
    # uncomment following to set a specific view size
    # lineChartView1.ViewSize = [1398, 650]

    # get layout
    layout2 = GetLayoutByName("Layout #2")

    # set active view
    SetActiveView(lineChartView1)

    # Rename the First data point and Second data point
    modified_x_name_2 = "Final_Modified_x_"

    modified_x_name_2 += str(k + 1)

    modified_y_name_2 = "Final_Modified_y_"

    modified_y_name_2 += str(k + 1)

    # find source
    modified_y_1 = FindSource(modified_y_name_2)

    # set active source
    SetActiveSource(modified_y_1)

    # create a new 'Plot Data'
    plotData1 = PlotData(Input=modified_y_1)

    # find source
    flocase100dat = FindSource(file_1)

    # Properties modified on flocase100dat
    flocase100dat.DataArrayStatus = ['P', 'P0','RHO0', 'U0', 'V0']

    # find source
    flocase167dat = FindSource(file_2)

    # find source
    modified_x_1 = FindSource(modified_x_name_2)

    # show data in view
    plotData1Display = Show(plotData1, lineChartView1, 'XYChartRepresentation')

    # get layout
    layout2 = GetLayoutByName("Layout #2")

    # add view to a layout so it's visible in UI
    AssignViewToLayout(view=lineChartView1, layout=layout2, hint=0)

    # x_array_name = "Final_modified_x_" + str(k+1)

    # # Properties modified on plotData1Display
    # plotData1Display.XArrayName = x_array_name

    # # Properties modified on plotData1Display
    # plotData1Display.CompositeDataSetIndex = [1, 2]

    # Properties modified on plotData1Display
    plotData1Display.UseIndexForXAxis = 0

    # # Properties modified on plotData1Display
    # plotData1Display.SeriesVisibility = []

    # series_name_1 = "Final_modified_y_"
    # series_name_1 += str(k + 1)
    # series_name_1 += " (zone00001)"

    # series_name_2 = "Final_modified_y_"
    # series_name_2 += str(k + 1)
    # series_name_2 += " (zone00002)"

    # # Properties modified on plotData1Display
    # plotData1Display.SeriesVisibility = [series_name_1]

    # # Properties modified on plotData1Display
    # plotData1Display.SeriesVisibility = [series_name_1, series_name_2]

    # final_dummy_x = "Final_modified_x_" + str(k+1) + " (zone00001)"
    # final_dummy_y = "Final_modified_y_" + str(k+1) + " (zone00001)"

    # final_dummy_x_zone_2 = "Final_modified_x_" + str(k+1) + " (zone00002)"
    # final_dummy_y_zone_2 = "Final_modified_y_" + str(k+1) + " (zone00002)"

    # # Properties modified on plotData4Display
    # plotData1Display.SeriesColor = [final_dummy_x, '0', '0', '0', 'P (zone00001)', '0.220005', '0.489998', '0.719997', 'Points_X (zone00001)', '0.300008', '0.689998', '0.289998', 'Points_Y (zone00001)', '0.6', '0.310002', '0.639994', 'Points_Z (zone00001)', '1', '0.500008', '0', 'Points_Magnitude (zone00001)', '0.650004', '0.340002', '0.160006', final_dummy_x_zone_2, '0', '0', '0', 'P (zone00002)', '0.220005', '0.489998', '0.719997', 'Points_X (zone00002)', '0.300008', '0.689998', '0.289998', 'Points_Y (zone00002)', '0.6', '0.310002', '0.639994', 'Points_Z (zone00002)', '1', '0.500008', '0', 'Points_Magnitude (zone00002)', '0.650004', '0.340002', '0.160006', final_dummy_y, '0', '0', '0', final_dummy_y_zone_2, '0.889998', '0.100008', '0.110002']

    # # Properties modified on plotData4Display
    # plotData1Display.SeriesColor = [final_dummy_x, '0', '0', '0', 'P (zone00001)', '0.220005', '0.489998', '0.719997', 'Points_X (zone00001)', '0.300008', '0.689998', '0.289998', 'Points_Y (zone00001)', '0.6', '0.310002', '0.639994', 'Points_Z (zone00001)', '1', '0.500008', '0', 'Points_Magnitude (zone00001)', '0.650004', '0.340002', '0.160006', final_dummy_x_zone_2, '0', '0', '0', 'P (zone00002)', '0.220005', '0.489998', '0.719997', 'Points_X (zone00002)', '0.300008', '0.689998', '0.289998', 'Points_Y (zone00002)', '0.6', '0.310002', '0.639994', 'Points_Z (zone00002)', '1', '0.500008', '0', 'Points_Magnitude (zone00002)', '0.650004', '0.340002', '0.160006', final_dummy_y, '0', '0', '0', final_dummy_y_zone_2, '0', '0', '0']

        # Properties modified on plotData9Display

    #GENERELIZATION OF THE PLOT
    plotData1Display.CompositeDataSetIndex = []

    print("")
    print("")
    print("********************START OF FINAL_MOD**********************")

    m = []
    for i in range(10000):
        m.append(i)

    plotData1Display.CompositeDataSetIndex = m

    myint = 1

    myint = len(plotData1Display.SeriesVisibility)

    print(plotData1Display.SeriesVisibility)
    print("the lenght is")
    print(myint)


    new_array= []
    store = 0
    result = 0

    for i in range(myint):
        result = plotData1Display.SeriesVisibility[i].find('Final_modified_y_')

        if result != -1:
            print(result)
            new_array.append(plotData1Display.SeriesVisibility[i])
            store = store + 1

    a = []
    b = []
    num = 0
    hello = '0'

    for i in range(store):

        a.append(new_array[i])
        b.append(new_array[i])

        for k in range(3):
            b.append(hello)

    # for x in range(len(plotData5Display.SeriesVisibility)):
    #     print plotData5Display.SeriesVisibility[x]

    print("AFTER")
    print(a)

    plotData1Display.SeriesVisibility = a
    plotData1Display.SeriesColor = b

    print("********************END OF FINAL_MOD**********************")
    print("")
    print("")

# THE FOLLOWING WILL BE AT THE END FOR HIDING LEGEND AND HIDING THE GRIDS
# Properties modified on lineChartView1
lineChartView1.ShowLegend = 0

# Properties modified on lineChartView1
lineChartView1.ShowLeftAxisGrid = 0

# Properties modified on lineChartView1
lineChartView1.ShowBottomAxisGrid = 0

"""
    ***********************************************************************************
    *                                                                                 *
    *                                                                                 *
    *                               RENAME DATA FILE                                  *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    ***********************************************************************************
"""
# find source
extractSubset1 = FindSource('ExtractSubset1')

# set active source
SetActiveSource(extractSubset1)

# rename source object
RenameSource('Subset_2', extractSubset1)

# find source
extractBlock1 = FindSource('ExtractBlock1')

# set active source
SetActiveSource(extractBlock1)

# rename source object
RenameSource('Wing_Final_Case', extractBlock1)

# find source
contour1 = FindSource('Contour1')

# set active source
SetActiveSource(contour1)

# rename source object
RenameSource('Pressure_Contour_2', contour1)


"""
    ***********************************************************************************
    *                                                                                 *
    *                                                                                 *
    *                       CALCULATOR FOR COEFF PRESSURE                             *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    ***********************************************************************************
"""

for k in range(cross_num):

    for j in range(2):

        if j == 0:
            # find source
            calculator_name_1 = "Initial_Cross_Z_at_" + str(user_input_array[k]) + "%"
            calculator_name_2 = 'Initial_Coefficient_Of_Pressure_at_' + str(user_input_array[k]) + "%"

            initial_Cross_Z_at_100 = FindSource(calculator_name_1)

            # set active source
            SetActiveSource(initial_Cross_Z_at_100)

            # create a new 'Calculator'
            calculator1 = Calculator(Input=initial_Cross_Z_at_100)
            calculator1.Function = '(P-P0)/(0.5*RHO0*((U0^2)+(V0^2)))'

            # rename source object
            RenameSource(calculator_name_2, calculator1)
            # Properties modified on calculator1
            calculator1.ResultArrayName = "CP"
            #calculator1.ResultArrayName = 'Initial_Coefficient_Of_Pressure_at_' + str(user_input_array[k]) + "%"

            print("this ran first")

        if j == 1:
            calculator_name_1 = "Final_Cross_Z_at_" + str(user_input_array[k]) + "%"
            calculator_name_2 = 'Final_Coefficient_Of_Pressure_at_' + str(user_input_array[k]) + "%"

            final_Cross_Z_at_100 = FindSource(calculator_name_1)

            # set active source
            SetActiveSource(final_Cross_Z_at_100)

            # create a new 'Calculator'
            calculator1 = Calculator(Input=final_Cross_Z_at_100)
            calculator1.Function = '(P-P0)/(0.5*RHO0*((U0^2)+(V0^2)))'

            # rename source object
            RenameSource(calculator_name_2, calculator1)
            # Properties modified on calculator1
            calculator1.ResultArrayName = "CP"
            #calculator1.ResultArrayName = 'Final_Coefficient_Of_Pressure_at_' + str(user_input_array[k]) + "%"

            print("this ran second")

"""
    ***********************************************************************************
    *                                                                                 *
    *                                                                                 *
    *                            CREATE PRESSURE PLOTS                                *
    *                                 NEW LAYOUT                                      *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    ***********************************************************************************
"""

for k in range(cross_num):

    y_variable_1 = 'CP' + ' (zone00001)'
    y_variable_2 = 'CP' + ' (zone00002)'

    # trace generated using paraview version 5.8.0
    #
    # To ensure correct image size when batch processing, please search
    # for and uncomment the line `# renderView*.ViewSize = [*,*]`

    # import the simple module from the paraview
    from paraview.simple import *
    # disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    layout_name = "Layout #" + str(k + 3)

    CreateLayout(layout_name)

    # set active view
    SetActiveView(None)

    ######################################################  PLOT 1 ###############################################################

    #name_1 = "Initial_Cross_Z_at_" + str(user_input_array[k]) +"%"
    name_1 = 'Initial_Coefficient_Of_Pressure_at_' + \
        str(user_input_array[k]) + "%"

    # find source
    initial_Cross_Z_at_100 = FindSource(name_1)

    # set active source
    SetActiveSource(initial_Cross_Z_at_100)

    # create a new 'Plot Data'
    plotData9 = PlotData(Input=initial_Cross_Z_at_100)

    # find source
    wing_Final_Case = FindSource('Wing_Final_Case')

    # find source
    subset_1 = FindSource('Subset_1')

    # find source
    wing_Initial_Case = FindSource('Wing_Initial_Case')

    # Create a new 'Line Chart View'
    lineChartView2 = CreateView('XYChartView')
    # uncomment following to set a specific view size
    # lineChartView2.ViewSize = [400, 400]

    # show data in view
    plotData9Display = Show(plotData9, lineChartView2, 'XYChartRepresentation')

    # get layout
    layout3 = GetLayoutByName(layout_name)

    # add view to a layout so it's visible in UI
    AssignViewToLayout(view=lineChartView2, layout=layout3, hint=0)

    # Properties modified on plotData9Display

    plotData9Display.CompositeDataSetIndex = []

    print("")
    print("")

    print("****************************** START OF CP *****************************")
    m = []
    for i in range(10000):
        m.append(i)

    plotData9Display.CompositeDataSetIndex = m

    myint = 1

    myint = len(plotData9Display.SeriesVisibility)

    print(plotData9Display.SeriesVisibility)
    print(myint)

    new_array= []
    store = 0
    result = 0

    for i in range(myint):
        result = plotData9Display.SeriesVisibility[i].find('CP')

        if result != -1:
            print(result)
            new_array.append(plotData9Display.SeriesVisibility[i])
            store = store + 1

    a = []
    b = []
    c = []
    num = 0
    hello = '0'
    dash = '1'

    print(myint)

    print(plotData9Display.SeriesVisibility)

    for i in range(store):
        a.append(new_array[i])
        b.append(new_array[i])
        c.append(new_array[i])
        c.append(dash)

        for s in range(3):
            b.append(hello)

    # for x in range(len(plotData5Display.SeriesVisibility)):
    #     print plotData5Display.SeriesVisibility[x]

    plotData9Display.SeriesVisibility = a
    plotData9Display.SeriesColor = b
    plotData9Display.SeriesLineStyle = c

    print("")
    print("AFTER")
    print(a)

    print("****************************** END OF CP *****************************")
    print("")
    print("")
    # Properties modified on plotData9Display
    plotData9Display.UseIndexForXAxis = 0

    # Properties modified on plotData9Display
    plotData9Display.XArrayName = 'Points_X'

    ##################################################### PLOT 2 ###############################################################

    #name_2 = "Final_Cross_Z_at_" + str(user_input_array[k]) +"%"
    name_2 = 'Final_Coefficient_Of_Pressure_at_' + \
        str(user_input_array[k]) + "%"

    # find source
    final_Cross_Z_at_100 = FindSource(name_2)

    # set active source
    SetActiveSource(final_Cross_Z_at_100)

    # create a new 'Plot Data'
    plotData10 = PlotData(Input=final_Cross_Z_at_100)

    # show data in view
    plotData10Display = Show(
        plotData10, lineChartView2, 'XYChartRepresentation')

    # Properties modified on plotData9Display

    print("****************************** START OF CP *****************************")

    plotData10Display.CompositeDataSetIndex = []

    m = []
    for i in range(10000):
        m.append(i)

    plotData10Display.CompositeDataSetIndex = m

    myint = 1

    myint = len(plotData10Display.SeriesVisibility)

    new_array= []
    store = 0
    result = 0

    for i in range(myint):
        result = plotData10Display.SeriesVisibility[i].find('CP')

        if result != -1:
            new_array.append(plotData10Display.SeriesVisibility[i])
            store = store + 1

    print(plotData10Display.SeriesVisibility)

    a = []
    b = []
    c = []
    num = 0
    hello = '0'
    dash = '2'

    print(myint)

    for i in range(store):

        a.append(new_array[i])
        b.append(new_array[i])
        c.append(new_array[i])
        c.append(dash)

        for s in range(3):
            b.append(hello)

    # for x in range(len(plotData5Display.SeriesVisibility)):
    #     print plotData5Display.SeriesVisibility[x]

    print("")
    print("AFTER")
    print(a)

    plotData10Display.SeriesVisibility = a
    plotData10Display.SeriesColor = b
    plotData10Display.SeriesLineStyle = c


    # Properties modified on plotData10Display
    plotData10Display.UseIndexForXAxis = 0

    print("****************************** END OF CP *****************************")

    print("")
    print("")
    # Properties modified on plotData10Display
    plotData10Display.XArrayName = 'Points_X'

    # Properties modified on lineChartView2
    lineChartView2.ShowLegend = 0

    # Adding the span location to title                              --------CODE-------
    g_position_str = str(user_input_array[k])
    okay = "Coefficient of Pressure versus Chord Length Position"

    Z_text = " at Z = "
    percent_text = "%"

    okay += Z_text
    okay += g_position_str
    okay += percent_text

    lineChartView2.ChartTitle = okay

    # Properties modified on lineChartView2
    lineChartView2.LeftAxisTitle = 'CP'

    # Properties modified on lineChartView2
    lineChartView2.BottomAxisTitle = 'X'

    # Properties modified on lineChartView2
    lineChartView2.LeftAxisUseCustomRange = 1

    # Properties modified on lineChartView2
    lineChartView2.LeftAxisRangeMinimum = 1.0

    # Properties modified on lineChartView2
    lineChartView2.LeftAxisRangeMaximum = -1.0

    # saving camera placements for all active views

    # current camera placement for renderView1
    renderView1.CameraPosition = [-1.330858703392007,
                                  2.7327018602834356, 2.9196340581779046]
    renderView1.CameraFocalPoint = [
        0.7139178766519763, 0.002191845327615738, 0.761412501335144]
    renderView1.CameraViewUp = [0.4184746762481223,
                                0.735041666731778, -0.533472298725247]
    renderView1.CameraParallelScale = 1.0447674531991689

    # current camera placement for renderView2
    renderView2.CameraPosition = [-1.344199506041666,
                                  2.7542537676100607, 2.9337150135962515]
    renderView2.CameraFocalPoint = [
        0.7139178766519763, 0.005928996950387955, 0.761412501335144]
    renderView2.CameraViewUp = [0.4184746762481223,
                                0.735041666731778, -0.533472298725247]
    renderView2.CameraParallelScale = 1.0447674531991689

    # get layout
    layout1 = GetLayoutByName(layout_name)

    layout_rename = "Pressure_Plot_at_Z = " + str(user_input_array[k]) + "%"

    RenameLayout(layout_rename, layout1)


# RENAME LAYOUT
# get layout
layout1 = GetLayoutByName("Layout #1")

RenameLayout("Comparison of Initial and Final Design Iteration", layout1)

# get layout
layout1 = GetLayoutByName("Layout #2")

RenameLayout("Airfoil - 2D Cross Section View ", layout1)


"""
    ***********************************************************************************
    *                                                                                 *
    *                                                                                 *
    *                                   END HERE                                      *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    *                                                                                 *
    ***********************************************************************************
"""



# RESET VIEW
# find view
# find source

# find view
renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [694, 650]

# get layout
comparisonofInitialandFinalDesignIteration = GetLayoutByName("Comparison of Initial and Final Design Iteration")

# set active view
SetActiveView(renderView1)

# get color transfer function/color map for 'P'
pLUT = GetColorTransferFunction('P')

# get opacity transfer function/opacity map for 'P'
pPWF = GetOpacityTransferFunction('P')


wing_Analysis_100dat = FindSource('Wing_Analysis_1.00.dat')

# set active source
SetActiveSource(wing_Analysis_100dat)

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [694, 650]

# get layout
comparisonofInitialandFinalDesignIteration = GetLayout()

# show data in view
wing_Analysis_100datDisplay = Show(wing_Analysis_100dat, renderView1, 'StructuredGridRepresentation')

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction('vtkBlockColors')

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction('vtkBlockColors')

# trace defaults for the display properties.
wing_Analysis_100datDisplay.Representation = 'Outline'
wing_Analysis_100datDisplay.ColorArrayName = ['FIELD', 'vtkBlockColors']
wing_Analysis_100datDisplay.LookupTable = vtkBlockColorsLUT
wing_Analysis_100datDisplay.OSPRayScaleArray = 'P'
wing_Analysis_100datDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
wing_Analysis_100datDisplay.SelectOrientationVectors = 'None'
wing_Analysis_100datDisplay.ScaleFactor = 4.948406028747559
wing_Analysis_100datDisplay.SelectScaleArray = 'None'
wing_Analysis_100datDisplay.GlyphType = 'Arrow'
wing_Analysis_100datDisplay.GlyphTableIndexArray = 'None'
wing_Analysis_100datDisplay.GaussianRadius = 0.24742030143737795
wing_Analysis_100datDisplay.SetScaleArray = ['POINTS', 'P']
wing_Analysis_100datDisplay.ScaleTransferFunction = 'PiecewiseFunction'
wing_Analysis_100datDisplay.OpacityArray = ['POINTS', 'P']
wing_Analysis_100datDisplay.OpacityTransferFunction = 'PiecewiseFunction'
wing_Analysis_100datDisplay.DataAxesGrid = 'GridAxesRepresentation'
wing_Analysis_100datDisplay.PolarAxes = 'PolarAxesRepresentation'
wing_Analysis_100datDisplay.ScalarOpacityFunction = vtkBlockColorsPWF
wing_Analysis_100datDisplay.ScalarOpacityUnitDistance = 1.2134293650719759

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
wing_Analysis_100datDisplay.ScaleTransferFunction.Points = [0.4505206048488617, 0.0, 0.5, 0.0, 1.3989499807357788, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
wing_Analysis_100datDisplay.OpacityTransferFunction.Points = [0.4505206048488617, 0.0, 0.5, 0.0, 1.3989499807357788, 1.0, 0.5, 0.0]

# show color bar/color legend
wing_Analysis_100datDisplay.SetScalarBarVisibility(renderView1, True)

# set scalar coloring
ColorBy(wing_Analysis_100datDisplay, ('POINTS', 'P'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(vtkBlockColorsLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
wing_Analysis_100datDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
wing_Analysis_100datDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'P'
pLUT = GetColorTransferFunction('P')

# get opacity transfer function/opacity map for 'P'
pPWF = GetOpacityTransferFunction('P')

# change representation type
wing_Analysis_100datDisplay.SetRepresentationType('Surface')

# find view
renderView2 = FindViewOrCreate('RenderView2', viewtype='RenderView')
# uncomment following to set a specific view size
# renderView2.ViewSize = [693, 650]

# set active view
SetActiveView(renderView2)

# find source
wing_Analysis_167dat = FindSource('Wing_Analysis_1.67.dat')

# set active source
SetActiveSource(wing_Analysis_167dat)

# show data in view
wing_Analysis_167datDisplay = Show(flocase167dat, renderView2, 'StructuredGridRepresentation')

# trace defaults for the display properties.
wing_Analysis_167datDisplay.Representation = 'Outline'
wing_Analysis_167datDisplay.ColorArrayName = ['POINTS', '']
wing_Analysis_167datDisplay.OSPRayScaleArray = 'P'
wing_Analysis_167datDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
wing_Analysis_167datDisplay.SelectOrientationVectors = 'None'
wing_Analysis_167datDisplay.ScaleFactor = 4.948406028747559
wing_Analysis_167datDisplay.SelectScaleArray = 'None'
wing_Analysis_167datDisplay.GlyphType = 'Arrow'
wing_Analysis_167datDisplay.GlyphTableIndexArray = 'None'
wing_Analysis_167datDisplay.GaussianRadius = 0.24742030143737795
wing_Analysis_167datDisplay.SetScaleArray = ['POINTS', 'P']
wing_Analysis_167datDisplay.ScaleTransferFunction = 'PiecewiseFunction'
wing_Analysis_167datDisplay.OpacityArray = ['POINTS', 'P']
wing_Analysis_167datDisplay.OpacityTransferFunction = 'PiecewiseFunction'
wing_Analysis_167datDisplay.DataAxesGrid = 'GridAxesRepresentation'
wing_Analysis_167datDisplay.PolarAxes = 'PolarAxesRepresentation'
wing_Analysis_167datDisplay.ScalarOpacityUnitDistance = 1.2134293650719759

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
wing_Analysis_167datDisplay.ScaleTransferFunction.Points = [0.4926852881908417, 0.0, 0.5, 0.0, 1.4549139738082886, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
wing_Analysis_167datDisplay.OpacityTransferFunction.Points = [0.4926852881908417, 0.0, 0.5, 0.0, 1.4549139738082886, 1.0, 0.5, 0.0]

# set scalar coloring
ColorBy(wing_Analysis_167datDisplay, ('POINTS', 'P'))

# rescale color and/or opacity maps used to include current data range
wing_Analysis_167datDisplay.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
wing_Analysis_167datDisplay.SetScalarBarVisibility(renderView2, True)

# change representation type
wing_Analysis_167datDisplay.SetRepresentationType('Surface')

# set active view
SetActiveView(renderView1)

# get color legend/bar for pLUT in view renderView1
pLUTColorBar = GetScalarBar(pLUT, renderView1)

# change scalar bar placement
pLUTColorBar.WindowLocation = 'AnyLocation'
pLUTColorBar.Position = [0.8141210374639769, 0.012307692307692297]
pLUTColorBar.ScalarBarLength = 0.33000000000000007

#### saving camera placements for all active views

# current camera placement for renderView2
renderView2.CameraPosition = [-1.344199506041666, 2.7542537676100607, 2.9337150135962515]
renderView2.CameraFocalPoint = [0.7139178766519763, 0.005928996950387955, 0.761412501335144]
renderView2.CameraViewUp = [0.4184746762481223, 0.735041666731778, -0.533472298725247]
renderView2.CameraParallelScale = 1.0447674531991689

# current camera placement for renderView1
renderView1.CameraPosition = [-1.330858703392007, 2.7327018602834356, 2.9196340581779046]
renderView1.CameraFocalPoint = [0.7139178766519763, 0.002191845327615738, 0.761412501335144]
renderView1.CameraViewUp = [0.4184746762481223, 0.735041666731778, -0.533472298725247]
renderView1.CameraParallelScale = 1.0447674531991689

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [694, 650]

# get layout
comparisonofInitialandFinalDesignIteration = GetLayout()

# reset view to fit data
renderView1.ResetCamera()

# find view
renderView2 = FindViewOrCreate('RenderView2', viewtype='RenderView')
# uncomment following to set a specific view size
# renderView2.ViewSize = [693, 650]

# set active view
SetActiveView(renderView2)

# reset view to fit data
renderView2.ResetCamera()

#### saving camera placements for all active views

print("")
print("")
print("")
print("************************ SYN3D MACRO OUTPUT COMPLETED ****************************")










#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

# for k in range(cross_num):

#     layout_index = "Layout #" + str((k+3))

#     CreateLayout(layout_index)

#     # set active view
#     SetActiveView(None)

#     name_1 = "Initial_Cross_Z_at_" + str(user_input_array[k]) + "%"

#     # find source
#     initial_Cross_Z_at_100 = FindSource(name_1)

#     # create a new 'Plot Data'
#     plotData13 = PlotData(Input=initial_Cross_Z_at_100)

#     # Create a new 'Line Chart View'
#     lineChartView2 = CreateView('XYChartView')
#     # uncomment following to set a specific view size
#     # lineChartView2.ViewSize = [400, 400]

#     # show data in view
#     plotData13Display = Show(plotData13, lineChartView2, 'XYChartRepresentation')

#     # trace defaults for the display properties.
#     plotData13Display.XArrayName = 'P'
#     plotData13Display.SeriesVisibility = ['P (zone00001)']
#     plotData13Display.SeriesLabel = ['P (zone00001)', 'P (zone00001)', 'Points_X (zone00001)', 'Points_X (zone00001)', 'Points_Y (zone00001)', 'Points_Y (zone00001)', 'Points_Z (zone00001)', 'Points_Z (zone00001)', 'Points_Magnitude (zone00001)', 'Points_Magnitude (zone00001)']
#     plotData13Display.SeriesColor = ['P (zone00001)', '0', '0', '0', 'Points_X (zone00001)', '0.89', '0.1', '0.11', 'Points_Y (zone00001)', '0.22', '0.49', '0.72', 'Points_Z (zone00001)', '0.3', '0.69', '0.29', 'Points_Magnitude (zone00001)', '0.6', '0.31', '0.64']
#     plotData13Display.SeriesPlotCorner = ['P (zone00001)', '0', 'Points_X (zone00001)', '0', 'Points_Y (zone00001)', '0', 'Points_Z (zone00001)', '0', 'Points_Magnitude (zone00001)', '0']
#     plotData13Display.SeriesLabelPrefix = ''
#     plotData13Display.SeriesLineStyle = ['P (zone00001)', '1', 'Points_X (zone00001)', '1', 'Points_Y (zone00001)', '1', 'Points_Z (zone00001)', '1', 'Points_Magnitude (zone00001)', '1']
#     plotData13Display.SeriesLineThickness = ['P (zone00001)', '2', 'Points_X (zone00001)', '2', 'Points_Y (zone00001)', '2', 'Points_Z (zone00001)', '2', 'Points_Magnitude (zone00001)', '2']
#     plotData13Display.SeriesMarkerStyle = ['P (zone00001)', '0', 'Points_X (zone00001)', '0', 'Points_Y (zone00001)', '0', 'Points_Z (zone00001)', '0', 'Points_Magnitude (zone00001)', '0']
#     plotData13Display.SeriesMarkerSize = ['P (zone00001)', '4', 'Points_X (zone00001)', '4', 'Points_Y (zone00001)', '4', 'Points_Z (zone00001)', '4', 'Points_Magnitude (zone00001)', '4']

#     # get layout
#     layout3 = GetLayoutByName(layout_index)

#     # add view to a layout so it's visible in UI
#     AssignViewToLayout(view=lineChartView2, layout=layout3, hint=0)

#     # find source
#     flocase100dat = FindSource(file_1)

#     # Properties modified on flocase100dat
#     flocase100dat.DataArrayStatus = ['P']

#     # find source
#     flocase167dat = FindSource(file_2)

#     # Properties modified on flocase167dat
#     flocase167dat.DataArrayStatus = ['P']

#     # find view
#     renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
#     # uncomment following to set a specific view size
#     # renderView1.ViewSize = [694, 650]

#     # Properties modified on plotData13Display
#     plotData13Display.SeriesColor = ['P (zone00001)', '0', '0', '0', 'Points_X (zone00001)', '0.889998', '0.100008', '0.110002', 'Points_Y (zone00001)', '0.220005', '0.489998', '0.719997', 'Points_Z (zone00001)', '0.300008', '0.689998', '0.289998', 'Points_Magnitude (zone00001)', '0.6', '0.310002', '0.639994', 'P (zone00002)', '1', '0.500008', '0', 'Points_X (zone00002)', '0.650004', '0.340002', '0.160006', 'Points_Y (zone00002)', '0', '0', '0', 'Points_Z (zone00002)', '0.889998', '0.100008', '0.110002', 'Points_Magnitude (zone00002)', '0.220005', '0.489998', '0.719997']
#     plotData13Display.SeriesPlotCorner = ['P (zone00001)', '0', 'P (zone00002)', '0', 'Points_Magnitude (zone00001)', '0', 'Points_Magnitude (zone00002)', '0', 'Points_X (zone00001)', '0', 'Points_X (zone00002)', '0', 'Points_Y (zone00001)', '0', 'Points_Y (zone00002)', '0', 'Points_Z (zone00001)', '0', 'Points_Z (zone00002)', '0']
#     plotData13Display.SeriesLineStyle = ['P (zone00001)', '1', 'P (zone00002)', '1', 'Points_Magnitude (zone00001)', '1', 'Points_Magnitude (zone00002)', '1', 'Points_X (zone00001)', '1', 'Points_X (zone00002)', '1', 'Points_Y (zone00001)', '1', 'Points_Y (zone00002)', '1', 'Points_Z (zone00001)', '1', 'Points_Z (zone00002)', '1']
#     plotData13Display.SeriesLineThickness = ['P (zone00001)', '2', 'P (zone00002)', '2', 'Points_Magnitude (zone00001)', '2', 'Points_Magnitude (zone00002)', '2', 'Points_X (zone00001)', '2', 'Points_X (zone00002)', '2', 'Points_Y (zone00001)', '2', 'Points_Y (zone00002)', '2', 'Points_Z (zone00001)', '2', 'Points_Z (zone00002)', '2']
#     plotData13Display.SeriesMarkerStyle = ['P (zone00001)', '0', 'P (zone00002)', '0', 'Points_Magnitude (zone00001)', '0', 'Points_Magnitude (zone00002)', '0', 'Points_X (zone00001)', '0', 'Points_X (zone00002)', '0', 'Points_Y (zone00001)', '0', 'Points_Y (zone00002)', '0', 'Points_Z (zone00001)', '0', 'Points_Z (zone00002)', '0']
#     plotData13Display.SeriesMarkerSize = ['P (zone00001)', '4', 'P (zone00002)', '4', 'Points_Magnitude (zone00001)', '4', 'Points_Magnitude (zone00002)', '4', 'Points_X (zone00001)', '4', 'Points_X (zone00002)', '4', 'Points_Y (zone00001)', '4', 'Points_Y (zone00002)', '4', 'Points_Z (zone00001)', '4', 'Points_Z (zone00002)', '4']

#     # Properties modified on plotData13Display
#     plotData13Display.CompositeDataSetIndex = [2, 1]

#     # Properties modified on plotData13Display
#     plotData13Display.UseIndexForXAxis = 0

#     # Properties modified on plotData13Display
#     plotData13Display.XArrayName = 'Points_X'

#     # Properties modified on plotData13Display
#     plotData13Display.SeriesColor = ['P (zone00001)', '0', '0', '0', 'Points_X (zone00001)', '0.889998', '0.100008', '0.110002', 'Points_Y (zone00001)', '0.220005', '0.489998', '0.719997', 'Points_Z (zone00001)', '0.300008', '0.689998', '0.289998', 'Points_Magnitude (zone00001)', '0.6', '0.310002', '0.639994', 'P (zone00002)', '0', '0', '0', 'Points_X (zone00002)', '0.650004', '0.340002', '0.160006', 'Points_Y (zone00002)', '0', '0', '0', 'Points_Z (zone00002)', '0.889998', '0.100008', '0.110002', 'Points_Magnitude (zone00002)', '0.220005', '0.489998', '0.719997']

#     name_2 = "Fnitial_Cross_Z_at_" + str(user_input_array[k]) + "%"

#     # find source
#     final_Cross_Z_at_100 = FindSource(name_2)

#     # set active source
#     SetActiveSource(final_Cross_Z_at_100)

#     # create a new 'Plot Data'
#     plotData14 = PlotData(Input=final_Cross_Z_at_100)

#     # show data in view
#     plotData14Display = Show(plotData14, lineChartView2, 'XYChartRepresentation')

#     # trace defaults for the display properties.
#     plotData14Display.XArrayName = 'P'
#     plotData14Display.SeriesVisibility = ['P (zone00001)']
#     plotData14Display.SeriesLabel = ['P (zone00001)', 'P (zone00001)', 'Points_X (zone00001)', 'Points_X (zone00001)', 'Points_Y (zone00001)', 'Points_Y (zone00001)', 'Points_Z (zone00001)', 'Points_Z (zone00001)', 'Points_Magnitude (zone00001)', 'Points_Magnitude (zone00001)']
#     plotData14Display.SeriesColor = ['P (zone00001)', '0', '0', '0', 'Points_X (zone00001)', '0.89', '0.1', '0.11', 'Points_Y (zone00001)', '0.22', '0.49', '0.72', 'Points_Z (zone00001)', '0.3', '0.69', '0.29', 'Points_Magnitude (zone00001)', '0.6', '0.31', '0.64']
#     plotData14Display.SeriesPlotCorner = ['P (zone00001)', '0', 'Points_X (zone00001)', '0', 'Points_Y (zone00001)', '0', 'Points_Z (zone00001)', '0', 'Points_Magnitude (zone00001)', '0']
#     plotData14Display.SeriesLabelPrefix = ''
#     plotData14Display.SeriesLineStyle = ['P (zone00001)', '1', 'Points_X (zone00001)', '1', 'Points_Y (zone00001)', '1', 'Points_Z (zone00001)', '1', 'Points_Magnitude (zone00001)', '1']
#     plotData14Display.SeriesLineThickness = ['P (zone00001)', '2', 'Points_X (zone00001)', '2', 'Points_Y (zone00001)', '2', 'Points_Z (zone00001)', '2', 'Points_Magnitude (zone00001)', '2']
#     plotData14Display.SeriesMarkerStyle = ['P (zone00001)', '0', 'Points_X (zone00001)', '0', 'Points_Y (zone00001)', '0', 'Points_Z (zone00001)', '0', 'Points_Magnitude (zone00001)', '0']
#     plotData14Display.SeriesMarkerSize = ['P (zone00001)', '4', 'Points_X (zone00001)', '4', 'Points_Y (zone00001)', '4', 'Points_Z (zone00001)', '4', 'Points_Magnitude (zone00001)', '4']

#     # update the view to ensure updated data information
#     lineChartView2.Update()

#     # Properties modified on plotData14Display
#     plotData14Display.UseIndexForXAxis = 0

#     # Properties modified on plotData14Display
#     plotData14Display.XArrayName = 'Points_X'

#     # Properties modified on plotData14Display
#     plotData14Display.SeriesColor = ['P (zone00001)', '0', '0', '0', 'Points_X (zone00001)', '0.889998', '0.100008', '0.110002', 'Points_Y (zone00001)', '0.220005', '0.489998', '0.719997', 'Points_Z (zone00001)', '0.300008', '0.689998', '0.289998', 'Points_Magnitude (zone00001)', '0.6', '0.310002', '0.639994', 'P (zone00002)', '1', '0.500008', '0', 'Points_X (zone00002)', '0.650004', '0.340002', '0.160006', 'Points_Y (zone00002)', '0', '0', '0', 'Points_Z (zone00002)', '0.889998', '0.100008', '0.110002', 'Points_Magnitude (zone00002)', '0.220005', '0.489998', '0.719997']
#     plotData14Display.SeriesPlotCorner = ['P (zone00001)', '0', 'P (zone00002)', '0', 'Points_Magnitude (zone00001)', '0', 'Points_Magnitude (zone00002)', '0', 'Points_X (zone00001)', '0', 'Points_X (zone00002)', '0', 'Points_Y (zone00001)', '0', 'Points_Y (zone00002)', '0', 'Points_Z (zone00001)', '0', 'Points_Z (zone00002)', '0']
#     plotData14Display.SeriesLineStyle = ['P (zone00001)', '1', 'P (zone00002)', '1', 'Points_Magnitude (zone00001)', '1', 'Points_Magnitude (zone00002)', '1', 'Points_X (zone00001)', '1', 'Points_X (zone00002)', '1', 'Points_Y (zone00001)', '1', 'Points_Y (zone00002)', '1', 'Points_Z (zone00001)', '1', 'Points_Z (zone00002)', '1']
#     plotData14Display.SeriesLineThickness = ['P (zone00001)', '2', 'P (zone00002)', '2', 'Points_Magnitude (zone00001)', '2', 'Points_Magnitude (zone00002)', '2', 'Points_X (zone00001)', '2', 'Points_X (zone00002)', '2', 'Points_Y (zone00001)', '2', 'Points_Y (zone00002)', '2', 'Points_Z (zone00001)', '2', 'Points_Z (zone00002)', '2']
#     plotData14Display.SeriesMarkerStyle = ['P (zone00001)', '0', 'P (zone00002)', '0', 'Points_Magnitude (zone00001)', '0', 'Points_Magnitude (zone00002)', '0', 'Points_X (zone00001)', '0', 'Points_X (zone00002)', '0', 'Points_Y (zone00001)', '0', 'Points_Y (zone00002)', '0', 'Points_Z (zone00001)', '0', 'Points_Z (zone00002)', '0']
#     plotData14Display.SeriesMarkerSize = ['P (zone00001)', '4', 'P (zone00002)', '4', 'Points_Magnitude (zone00001)', '4', 'Points_Magnitude (zone00002)', '4', 'Points_X (zone00001)', '4', 'Points_X (zone00002)', '4', 'Points_Y (zone00001)', '4', 'Points_Y (zone00002)', '4', 'Points_Z (zone00001)', '4', 'Points_Z (zone00002)', '4']

#     # Properties modified on plotData14Display
#     plotData14Display.CompositeDataSetIndex = [2, 1]

#     # Properties modified on plotData14Display
#     plotData14Display.SeriesColor = ['P (zone00001)', '0', '0', '0', 'Points_X (zone00001)', '0.889998', '0.100008', '0.110002', 'Points_Y (zone00001)', '0.220005', '0.489998', '0.719997', 'Points_Z (zone00001)', '0.300008', '0.689998', '0.289998', 'Points_Magnitude (zone00001)', '0.6', '0.310002', '0.639994', 'P (zone00002)', '0', '0', '0', 'Points_X (zone00002)', '0.650004', '0.340002', '0.160006', 'Points_Y (zone00002)', '0', '0', '0', 'Points_Z (zone00002)', '0.889998', '0.100008', '0.110002', 'Points_Magnitude (zone00002)', '0.220005', '0.489998', '0.719997']

#     # Properties modified on plotData14Display
#     plotData14Display.SeriesLineStyle = ['P (zone00001)', '2', 'P (zone00002)', '2', 'Points_Magnitude (zone00001)', '1', 'Points_Magnitude (zone00002)', '1', 'Points_X (zone00001)', '1', 'Points_X (zone00002)', '1', 'Points_Y (zone00001)', '1', 'Points_Y (zone00002)', '1', 'Points_Z (zone00001)', '1', 'Points_Z (zone00002)', '1']

#     # Properties modified on lineChartView2
#     lineChartView2.ShowLegend = 0

#     #Adding the span location to title                              --------CODE-------
#     g_position_str = str(g)
#     okay = lineChartView1.ChartTitle

#     Z_text = " at Z = "
#     percent_text = "%"

#     okay += Z_text
#     okay += g_position_str
#     okay += percent_text
#     # Properties modified on lineChartView2
#     lineChartView2.LeftAxisTitle = 'P'

#     # Properties modified on lineChartView2
#     lineChartView2.BottomAxisTitle = 'X'

#     #### saving camera placements for all active views

#     # current camera placement for renderView1
#     renderView1.CameraPosition = [-1.330858703392007, 2.7327018602834356, 2.9196340581779046]
#     renderView1.CameraFocalPoint = [0.7139178766519763, 0.002191845327615738, 0.761412501335144]
#     renderView1.CameraViewUp = [0.4184746762481223, 0.735041666731778, -0.533472298725247]
#     renderView1.CameraParallelScale = 1.0447674531991689

#     # current camera placement for renderView2
#     renderView2.CameraPosition = [-1.344199506041666, 2.7542537676100607, 2.9337150135962515]
#     renderView2.CameraFocalPoint = [0.7139178766519763, 0.005928996950387955, 0.761412501335144]
#     renderView2.CameraViewUp = [0.4184746762481223, 0.735041666731778, -0.533472298725247]
#     renderView2.CameraParallelScale = 1.0447674531991689

#     # get layout
#     layout3 = GetLayoutByName(layout_index)

#     layout_name = "Pressure_Cross_Z_at_" + str(user_input_array[k]) + "%"

#     RenameLayout('Pressure_Cross_Z_at_10.0%', layout3)
















