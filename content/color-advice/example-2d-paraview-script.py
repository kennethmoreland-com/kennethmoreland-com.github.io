# state file generated using paraview version 4.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1038, 638]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.StereoType = 0
renderView1.CameraPosition = [0.0, 0.0, 5464.101615137755]
renderView1.CameraParallelScale = 994.5253668071931
renderView1.Background = [0.32, 0.34, 0.43]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Wavelet'
wavelet1 = Wavelet()
wavelet1.WholeExtent = [-1000, 1000, -1000, 1000, 0, 0]
wavelet1.Center = [500.0, 400.0, 0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'RTData'
rTDataLUT = GetColorTransferFunction('RTData')
rTDataLUT.RGBPoints = [24.71866226196289, 0.231373, 0.298039, 0.752941, 155.53389167785645, 0.865003, 0.865003, 0.865003, 286.34912109375, 0.705882, 0.0156863, 0.14902]
rTDataLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'RTData'
rTDataPWF = GetOpacityTransferFunction('RTData')
rTDataPWF.Points = [24.71866226196289, 0.0, 0.5, 0.0, 286.34912109375, 1.0, 0.5, 0.0]
rTDataPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from wavelet1
wavelet1Display = Show(wavelet1, renderView1)
# trace defaults for the display properties.
wavelet1Display.Representation = 'Slice'
wavelet1Display.ColorArrayName = ['POINTS', 'RTData']
wavelet1Display.LookupTable = rTDataLUT
wavelet1Display.ScalarOpacityUnitDistance = 1.7320508075688779
