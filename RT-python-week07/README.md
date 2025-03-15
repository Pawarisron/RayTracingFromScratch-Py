# RT-python-week07
Ray tracing course week 07

This repository is for 'Raytracing in Entertainment Industry' (01418283).
This course is set to be taught for undergrad students at Dept of Computer Science, Faculty of Science, Kasetsart University.
The codes were rewritten and modified from https://raytracing.github.io/books/RayTracingInOneWeekend.html.

**Prerequisites :**
1. C/C++ or python.
2. Object-Oriented Programming (OOP).
3. Linear algebra for undergrad students.


**Class assignment**
Note that to submit the rendered results, please use the following parameters, otherwise stated.
- at least 128 samples per pixel.
- at least 5 max depth.
- resolution width = 480p.
- aspect ratio = 16:9.
- No light is needed. 

1. Complete the 'intersect()' in the Quad class to support texture mapping.

2. Complete the 'renderProceduralTexture()' in main.py by creating textuers and use them accordingly. The scene is lit up by the sky as a background. Submit the rendered result as 'week07_texture_sky.png'.
3. Complete the 'renderEarth()' in main.py by creating textures, loaded up from files, and use them accordingly. The scene is lit up by the sky as a background. Submit the rendered result as 'week07_texture_earth_sky.png'.
4. Complete the metal class in RT_material.py. The reflected ray must be calculated based on the roughness parameter.
5. Submit the rendered result from (3.). by setting up a scene with 6 matal balls. The submitted file name is 'week07_metal_balls.png'. The parameters are as follows.
    5.1 Roughness paramters = 0.0001, 0.0005, 0.05, 0.1, 0.8, 1.0. 
    5.2 Use a quad(area) light source above all of the balls.
    5.3 The background is almost black.



