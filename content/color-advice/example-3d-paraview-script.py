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
renderView1.ViewSize = [647, 638]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.OrientationAxesVisibility = 0
renderView1.OrientationAxesLabelColor = [0.0, 0.0, 0.0]
renderView1.OrientationAxesOutlineColor = [0.0, 0.0, 0.0]
renderView1.CenterOfRotation = [-3.083369493484497, 0.980888843536377, -15.895963668823242]
renderView1.StereoType = 0
renderView1.CameraPosition = [-3.688172561873803, -4.222090624155089, -42.177539989584695]
renderView1.CameraFocalPoint = [-3.4756156904281363, 2.2471037909309897, -2.268482630488684]
renderView1.CameraViewUp = [-0.49216799618312473, 0.8596944418530357, -0.1367337931167172]
renderView1.CameraParallelScale = 12.79532298858206
renderView1.Background = [1.0, 1.0, 1.0]

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.XTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.YTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.GridColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.XLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.YLabelColor = [0.0, 0.0, 0.0]
renderView1.AxesGrid.ZLabelColor = [0.0, 0.0, 0.0]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# Find the location of the can.ex2 example file
import os
import sys
can_file = os.path.dirname(sys.executable) + '/../examples/can.ex2'

# create a new 'ExodusIIReader'
canex2 = ExodusIIReader(FileName=[can_file])
canex2.ElementVariables = ['EQPS']
canex2.PointVariables = ['DISPL', 'VEL', 'ACCL']
canex2.GlobalVariables = ['KE', 'XMOM', 'YMOM', 'ZMOM', 'NSTEPS', 'TMSTEP']
canex2.NodeSetArrayStatus = []
canex2.SideSetArrayStatus = []
canex2.ElementBlocks = ['Unnamed block ID: 1 Type: HEX']

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'EQPS'
eQPSLUT = GetColorTransferFunction('EQPS')
eQPSLUT.RGBPoints = [0.021583130583167076, 0.231373, 0.298039, 0.752941, 1.4577623857185245, 0.865003, 0.865003, 0.865003, 2.893941640853882, 0.705882, 0.0156863, 0.14902]
eQPSLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'EQPS'
eQPSPWF = GetOpacityTransferFunction('EQPS')
eQPSPWF.Points = [0.021583130583167076, 0.0, 0.5, 0.0, 2.893941640853882, 1.0, 0.5, 0.0]
eQPSPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from canex2
canex2Display = Show(canex2, renderView1)
# trace defaults for the display properties.
canex2Display.AmbientColor = [0.0, 0.0, 0.0]
canex2Display.ColorArrayName = ['CELLS', 'EQPS']
canex2Display.LookupTable = eQPSLUT
