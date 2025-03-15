# RT-python-week06
Ray tracing course week 06

This repository is for 'Raytracing in Entertainment Industry' (01418283).
This course is set to be taught for undergrad students at Dept of Computer Science, Faculty of Science, Kasetsart University.
The codes were rewritten and modified from https://raytracing.github.io/books/RayTracingInOneWeekend.html.

**Prerequisites :**
1. C/C++ or python.
2. Object-Oriented Programming (OOP).
3. Linear algebra for undergrad students.


**Class assignment**

Note that to submit the rendered results, please use the following parameters.
- at least 100 samples per pixel.
- at least 5 max depth.
- resolution width = 480p.
- aspect ratio = 16:9.


1. Implement 'reflect()' function to support a mirror material.
2. Implement Mirror class by using 'reflect()' function.
3. Render a scene with at least 2 mirrors and a point light.
4. Render a scene with at least 2 mirrors and the sky background (no point light).
5. Implement Dielectric class by using 'refract()' function.
6. Render a scene with at least 2 transparent materials and the sky background.
7. Render a scene with the following materials and the sky background.
    - a dielectric material with index of refraction = 1.5
    - a dielectric material with index of refraction = 1.0
    - a dielectric material with index of refraction = 0.5
    - a lambertian material
    - a mirror

