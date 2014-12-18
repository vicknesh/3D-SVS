# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 14:50:52 2014

@author:    VICK
"""
#### GRIDDING ALGORITHM

# Initialize numpy
from numpy import *

# setup 3D array containers
N = 100
i = ones((N,N,N))

# fill the containers with scalar values
a = i
a = a.astype(uint8)
a[:N/2, :N, :N] = 200
a[N/2:80, :N, :N] = 300
a[80:N, :N, :N] = 100

#### MAPPING ALGORITHM

import vtk

# Step 1
dataReader = vtk.vtkImageImport()
string = a.tostring()
dataReader.CopyImportVoidPointer(string,len(string))
dataReader.SetDataScalarTypeToUnsignedChar()
dataReader.SetNumberOfScalarComponents(1)
dataReader.SetDataExtent(0,N-1,0,N-1,0,N-1)
dataReader.SetWholeExtent(0,N-1,0,N-1,0,N-1)

# Step 2
alphaFunc = vtk.vtkPiecewiseFunction()
alphaFunc.AddPoint(0, 0.0)
alphaFunc.AddPoint(30, 0.0)
alphaFunc.AddPoint(255, 0.5)

colorFunc = vtk.vtkColorTransferFunction()
colorFunc.AddRGBPoint(0, 1.0, 1.0, 1.0)
colorFunc.AddRGBPoint(30, 1.0, 1.0, 1.0)
colorFunc.AddRGBPoint(255, 0.1, 0.1, 0.1)

opticalProperty = vtk.vtkVolumeProperty()
opticalProperty.SetColor(colorFunc)
opticalProperty.SetScalarOpacity(alphaFunc)

####RENDERING ALGORITHM

# Step 3

compositeFunction = vtk.vtkVolumeRayCastCompositeFunction()
volumeMapper = vtk.vtkVolumeRayCastMapper()
volumeMapper.SetVolumeRayCastFunction(compositeFunction)
volumeMapper.SetInputConnection(dataReader.GetOutputPort())

volume = vtk.vtkVolume()
volume.SetMapper(volumeMapper)
volume.SetProperty(opticalProperty)

# Step 4

renderer = vtk.vtkRenderer()
renderWin = vtk.vtkRenderWindow()
renderWin.AddRenderer(renderer)
renderInteractor = vtk.vtkRenderWindowInteractor()
renderInteractor.SetRenderWindow(renderWin)
renderer.AddVolume(volume)
renderer.SetBackground(1,1,1)
renderWin.SetSize(500, 500)
renderWin.SetWindowName("3D SVS")
renderInteractor.Initialize()
renderWin.Render()
renderInteractor.Start()
    
