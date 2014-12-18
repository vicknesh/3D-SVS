3D-SVS
======

Three Dimensional Subsurface Visualization System

3D-SVS TOOL
(Refer Chapter 4 of Thesis)

This will be the basic building block of the overall 3D-SVS, a minimalist version that could be build upon to form more complex models. It's called the Layer Cake Model (LKM). The Python code "LayerCakeModel.py" uses NumPy and vtk libraries to render a simple voxel data-sets into its 3D representation.

The code is separated into 3 sections as follow :

#### GRIDDING ALGORITHM

Here the LKM is first parameterized with a general dimension of 100 x 100 x 100. NumPy, a numeric extension for Python that provides a homogenous and multidimensional array, is used to generate the discrete empty voxel containers. This array container structure is then filled with scalar values to separate the containers into three distinct layers with values ranging from 100 - 300. These values will act as makers and not as any particular measured quantity. The reasons behind selecting these values will be made more clear when the color transfer function is manipulated in the next section.

#### MAPPING ALGORITHM

Here is where the transfer functions are assigned to the scalar values (100 - 300). The assignment of a transfer funtion is a tedious and manual process. The combination of scalar values with its corresponding RGB values are a trial and error process. The values used here were adjusted real time while re-executing the script until distinct color differentiating the individual layers is obtained.

#### RENDERING ALGORITHM

Here is where the Ray Casting process takes place; the GPUs programmable functions are hosted in this algorithm. Once the models are assigned with the transfer function, the algorithm will invoke the rendering integral within the processor to produce the rendered output image.

Once executed within a Python terminal, a new window shall open with the LKM fully rendered. The model can be rotated, and zoom in and out using the mouse. 

If the above runs well then we will be able to move on the the next stage.
    
